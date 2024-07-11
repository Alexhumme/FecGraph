import tkinter as tk
import sv_ttk
from tkinter import ttk
from tkinter.font import Font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from utils.get_phase import main as get_phase
from utils.phases_data import data as phases
import numpy as np

class InteractivePlot(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, width=800, padding=20)

        self.fig, self.ax = plt.subplots()
        
        # configuracion de la grafica
        plt.title("Diagrama hierro carbono")
        self.ax.set_xlabel("Porcentaje de carbono (C%)")
        self.ax.set_ylabel("Temperatura (°F)")
        self.ax.set_xlim(0, 7)
        self.ax.set_ylim(20, 1600)
        self.ax.grid()
        self.labels = []

        self.create_controls()
        
        pass
    def create_controls(self):
        self.create_data_bar()
        self.create_plot()

    def create_data_bar(self):
        data_bar = ttk.Frame(self)
        data_bar.pack(side=tk.TOP, fill="x", expand=True)

        t_card = ttk.Frame(data_bar, style='Card.TFrame', padding=(10,5))
        t_card.pack(side=tk.RIGHT)
        self.t_label = ttk.Label(t_card, text="0°F")
        self.t_label.pack(expand=True, fill=tk.BOTH)

        p_card = ttk.Frame(data_bar, style='Card.TFrame', padding=(10,5))
        p_card.pack(side=tk.RIGHT, padx=5)
        self.p_label = ttk.Label(p_card, text="0%")
        self.p_label.pack(expand=True, fill=tk.BOTH)
        pass

    def create_plot(self):

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.ax.set_facecolor("#FAFAFA")
        self.fig.set_facecolor("#FAFAFA")
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

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
                label = self.ax.annotate(
                    f'{phase["name"]}\n{phase["symbol"]}', 
                    xy=(x_center, y_center), 
                    ha='center', 
                    va='center', 
                    fontsize=10, 
                    color='black', 
                    weight='bold'
                )
                self.labels.append(label)

        self.canvas.mpl_connect("motion_notify_event", self.on_hover)
        self.tooltip = None

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

    def update_cards(self, event):
        p, t = (event.xdata, event.ydata)

        self.t_label.config(text=f'{t:.2f}°F')
        self.p_label.config(text=f'{p:.2f}%')       

class PercPlot(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, style="Card.TFrame", padding=15)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.f_buttons = []

        self.fig, self.ax = plt.subplots(figsize=(1.5, 1.5))
        self.ax.set_facecolor("#FAFAFA")
        self.fig.set_facecolor("#FAFAFA")
        self.ax.pie([1])
        self.ax.axis('equal')  # Asegurar que el diagrama de pastel es circular
        self.create_controls()

    def create_controls(self):

        self.f_buttons = [
            tk.Button(self),
            tk.Button(self),
            tk.Button(self)
        ]

        [button.grid(row=i, column=2, sticky="ew") for i, button in enumerate(self.f_buttons)]
        
        separator = ttk.Separator(self)
        separator.grid(row=0, column=1, sticky="ns", rowspan=3)

        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        self.fig = plt.gcf()
        self.fig.gca().add_artist(centre_circle)
 
        self.plot:FigureCanvasTkAgg = FigureCanvasTkAgg(self.fig, master=self)
        self.plot.draw()
        self.plot.get_tk_widget().grid(row=0, column=0, rowspan=3,sticky="nsew")
    
    def load_phases(self,phases,i):

        if len(phases) > 1:explode = [0.1 if i == o else 0 for o, phase in enumerate(phases)]
        else: explode = [0]

        self.ax.clear()
        # volver a crear el pastel
        wedges, texts = self.ax.pie(
            [item.get('porc') for item in phases],
            colors=[item.get('color') for item in phases],           
            explode=explode)
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        
        # resaltar rebanada seleccionada
        for index, wedge in enumerate(wedges):
            if index == i:
                wedge.set_edgecolor('grey')
                wedge.set_linewidth(1)
        
        # añadir circulo para hacerlo dona
        self.fig.gca().add_artist(centre_circle)
        
        self.plot.draw_idle()
        
        for i, button in enumerate(self.f_buttons):
            if i < len(phases):
                button.config(
                    text=f"{phases[i].get('porc'):.1f}%", 
                    state=tk.NORMAL,
                    bg=phases[i].get('color') or '#1f75b4'
                )
            else:
                button.config(
                    text="",
                    state=tk.DISABLED,
                    bg="#FAFAFA"
                )
    
class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, width="260")
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

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
        title_font = Font(weight='bold')
        self.name_card = ttk.Label(
            self, 
            text='Seleccionar', 
            borderwidth=2, 
            relief="solid", 
            justify='center',
            anchor='center',
            font = title_font
        )
        self.name_card.grid(row=0,column=0, sticky="nsew", ipady = 20)

        self.perc_card = PercPlot(self)
        self.perc_card.grid(row=1, column=0, sticky="nsew", pady=20)

        self.perc_card.f_buttons[0].config(command=lambda :self.load_data(0))
        self.perc_card.f_buttons[1].config(command=lambda :self.load_data(1))
        self.perc_card.f_buttons[2].config(command=lambda :self.load_data(2))


        scrollable = ScrollableFrame(self)

        desc_frame = ttk.Frame(scrollable.scrollable_frame, style = 'Card.TFrame', padding=15)
        desc_frame.pack(expand=True, fill=tk.BOTH, padx=(0,10))
        scrollable.grid(row=2, rowspan=2, column=0, sticky="nsew")

        self.image_card = ttk.Label(desc_frame, borderwidth=2, relief="solid")
        self.image_card.grid(row=0, column=0, sticky="")
        
        desc_sep = ttk.Separator(desc_frame)
        desc_sep.grid(row=1, column=0,pady=10, sticky="ew")

        self.info_card = ttk.Label(desc_frame, wrap=250)
        self.info_card.grid(row=2, column=0, sticky="nsew")



    def handle_graph_click(self, event):
        self.point = (event.xdata, event.ydata)
        x, y = self.point
        self.phases_data = get_phase(x, y)
        self.load_data(0)

    def load_data(self, index):
        data:dict = self.phases_data[index]

        self.name_card.config(
            text=f"{data.get('name')} {'pura' if data.get('pure') else ''} {data.get('num') or ''}")
        
        self.perc_card.load_phases(self.phases_data, index)

        if data.get('img'): 
            img = Image.open(f"./src/resources/images/{data.get('img')}")
            img = img.resize((120,120))
            self.img = ImageTk.PhotoImage(img)
            self.image_card.config(image=self.img)
        
        self.info_card.config(text=f"{data.get('description')}")

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
            self.handle_graph_click
        )

        # Tema de estilo
        sv_ttk.set_theme("light")
    
    def handle_graph_click(self, event):
        self.sidebar.handle_graph_click(event)
        self.plot_frame.update_cards(event)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

