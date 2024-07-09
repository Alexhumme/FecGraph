import tkinter as tk
import sv_ttk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from utils.get_phase import main as get_phase
from utils.phases_data import data as phases
import numpy as np

class InteractivePlot(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, width=800, padding=20)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.ax.set_facecolor("#FAFAFA")
        self.fig.set_facecolor("#FAFAFA")
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)

        # configuracion de la grafica
        plt.title("Diagrama hierro carbono")
        self.ax.set_xlabel("Porcentaje de carbono (C%)")
        self.ax.set_ylabel("Temperatura (°F)")
        self.ax.set_xlim(0, 7)
        self.ax.set_ylim(20, 1600)
        self.ax.grid()
        self.labels = []

        # Add data from phases as polygons
        self.polygons = []
        for phase in phases:
            # Crear polígonos con datos de las fases
            if phase.get('color'):
                polygon = self.ax.fill_between(
                        phase.get('line_x'),
                        phase.get('line_y'),
                        alpha=0.5,
                        edgecolor='black',
                        facecolor=phase.get('color'),
                        linewidth=2
                    )
                self.polygons.append((polygon, phase))
                x_center = np.mean(phase.get('line_x'))
                y_center = np.mean(phase.get('line_y'))
                label = self.ax.annotate(phase["name"], xy=(x_center, y_center), ha='center', va='center', fontsize=10, color='black', weight='bold')
                self.labels.append(label)

        self.canvas.mpl_connect("motion_notify_event", self.on_hover)
        self.tooltip = None

        pass

    def on_hover(self, event):
        if event.inaxes == self.ax:
            x, y = event.xdata, event.ydata
            hovered_phase = None

            # determina si alguna de lass fases esta hover
            for polygon, phase in self.polygons:
                if polygon.contains(event)[0]:
                    hovered_phase = (polygon, phase)
                    break
                else: polygon.set_alpha(0.5)

            # remueve el tooltip actual
            if self.tooltip: self.tooltip.remove()

            # si hay hover, cambia el tooltip colorea la fase, sino muestra las coordenadas
            if hovered_phase:
                tip = f"C%={x:.2f}, T°={y:.2f} : {phase['name']}"
                polygon.set_alpha(1) # rellenar poligonos
            else: tip = f"C%={x:.2f}, T°={y:.2f}"

            self.tooltip = self.ax.annotate(
                tip,
                xy=(x, y), xytext=(20, 20),
                textcoords="offset points", ha="center", va="bottom",
                bbox=dict(boxstyle="round,pad=0.5", fc="yellow", alpha=0.5),
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0")
            )

            # si el tooltip no esta limpio actualizar
            self.canvas.draw_idle()
        else:
            if self.tooltip:
                self.tooltip.remove()
                self.tooltip = None
                self.canvas.draw_idle()
    def on_click(self, event):
        x, y = event.xdata, event.ydata
        return (x,y)

class PercPlot(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, style="Card.TFrame", padding=15)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=3)

        self.fig, self.ax = plt.subplots(figsize=(2, 1))
        self.ax.set_facecolor("#FAFAFA")
        self.fig.set_facecolor("#FAFAFA")
        self.ax.pie([1])
        self.ax.axis('equal')  # Asegurar que el diagrama de pastel es circular
        self.create_controls()

    def create_controls(self):
        self.p_icon = ImageTk.PhotoImage(Image.open('src/resources/icons/porc.png').resize((30,30)))
        self.porc_label = ttk.Label(self, text='porc', image=self.p_icon)
        self.porc_label.grid(row=0, column=0, sticky="e")

        self.t_icon = ImageTk.PhotoImage(Image.open('src/resources/icons/temp.png').resize((30,30)))
        self.temp_label = ttk.Label(self, text="temp", image=self.t_icon)
        self.temp_label.grid(row=0, column=1, sticky="w")

        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        self.fig = plt.gcf()
        self.fig.gca().add_artist(centre_circle)
 
        self.plot:FigureCanvasTkAgg = FigureCanvasTkAgg(self.fig, master=self)
        self.plot.draw()
        self.plot.get_tk_widget().grid(row=1, column=0, columnspan=2,sticky="nsew")
    
    def load_phases(self,phases,i,point):
        p, t = point
        self.ax.clear()
        self.ax.pie(
            [item.get('porc') for item in phases],
            labels=[item.get('symbol') for item in phases],
            colors=[item.get('color') for item in phases],           
            autopct='%1.1f%%',
            explode=[0.1 if i == o-1 else 0 for o in range(len(phases))]
        )
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        self.temp_label.config(text=f'{t}')
        self.porc_label.config(text=f'{p}')
        self.fig = plt.gcf()
        self.fig.gca().add_artist(centre_circle)
        
        self.plot.draw_idle()

class Sidebar(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, style="Card.TFrame", width=200, padding=15)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=3)
        self.create_controls()
        self.phases_data = None

    def create_controls(self):
        self.name_card = ttk.Label(
            self, 
            text='Seleccionar', 
            borderwidth=2, 
            relief="solid", 
            justify='center',
            anchor='center'
        )
        self.name_card.grid(row=0,column=0, sticky="nsew")

        self.perc_card = PercPlot(self)
        self.perc_card.grid(row=1, column=0, sticky="nsew")

        self.image_card = ttk.Label(self, borderwidth=2, relief="solid")
        self.image_card.grid(row=2, column=0, sticky="nsew")

        self.info_card = tk.Text(
            self,  
            wrap=tk.WORD, 
            state=tk.DISABLED,
            borderwidth=2, 
            relief="solid",
            width=10,
            height=10
        )
        self.info_card.grid(row=3, column=0, sticky="nsew")

    def handle_graph_click(self, event):
        self.point = (event.xdata, event.ydata)
        x, y = self.point
        self.phases_data = get_phase(x, y)
        self.load_data(0)

    def load_data(self, index):
        data:dict = self.phases_data[index]

        self.name_card.config(
            text=f"{data.get('name')} {'pura' if data.get('pure') else ''} {data.get('num') or ''}")
        
        self.perc_card.load_phases(self.phases_data, index, self.point)

        if data.get('img'): 
            img = Image.open(f"./src/resources/images/{data.get('img')}")
            img = img.resize((120,120))
            self.img = ImageTk.PhotoImage(img)
            self.image_card.config(image=self.img)
        
        self.info_card.config(state = tk.NORMAL)
        self.info_card.delete(1.0, tk.END)
        self.info_card.insert(tk.END, f"{data.get('description')}")
        self.info_card.config(state = tk.DISABLED)

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Diagrama Hierro Carbono Interactivo")
        self.geometry("1000x600")

        # layout principal
        app_container: ttk.Frame = ttk.Frame(self, padding=20, style='Card.TFrame')
        app_container.pack(expand=True)

        # componentes

        self.sidebar = Sidebar(app_container)
        self.sidebar.pack(side=tk.RIGHT)

        self.plot_frame = InteractivePlot(app_container)
        self.plot_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.plot_frame.canvas.mpl_connect(
            "button_press_event", 
            self.sidebar.handle_graph_click
        )

        # Tema de estilo
        sv_ttk.set_theme("light")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

