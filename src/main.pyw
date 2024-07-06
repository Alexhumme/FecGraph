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
        super().__init__(master)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)

        # configuracion de la grafica
        self.ax.set_xlabel("Porcentaje de carbono (C%)")
        self.ax.set_ylabel("Temperatura (°F)")
        self.ax.set_xlim(0, 7)
        self.ax.set_ylim(20, 1600)
        self.ax.grid()

        # Add data from phases as polygons
        self.polygons = []
        for phase in phases:
            # Crear polígonos con datos de las fases
            if phase.get('color'):
                polygon = self.ax.fill_between(
                        phase.get('line_x'),
                        phase.get('line_y'),
                        alpha=0.4,
                        #edgecolor=phase.get('color'),
                        #facecolor=phase.get('color'),
                        linewidth=2
                    )
                self.polygons.append((polygon, phase))

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
                tip = f"{phase['name']}"
                polygon.set_alpha(0.7) # rellenar poligonos
            else: tip = f"x={x:.2f}, y={y:.2f}"

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
        super().__init__(master, borderwidth=2, relief="solid")
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=3)

        self.fig, self.ax = plt.subplots(figsize=(2, 1))
        self.ax.pie(
            [1],
            #explode=self.explode,
            #labels=self.labels,
            #colors=self.colors,
            #autopct='%1.1f%%',
            #shadow=True,
            #startangle=140
        )
        self.ax.axis('equal')  # Asegurar que el diagrama de pastel es circular
        self.create_controls()

    def create_controls(self):
        p_icon = ImageTk.PhotoImage(Image.open(r'./src/resources/icons/porc.png').resize((10,10)))
        self.porc_label = ttk.Label(self, text='porc', image=p_icon)
        self.porc_label.grid(row=0, column=0, sticky="e")

        t_icon = ImageTk.PhotoImage(Image.open(r'./src/resources/icons/temp.png'))
        self.temp_label = ttk.Label(self, text="temp", image=t_icon)
        self.temp_label.grid(row=0, column=1, sticky="w")

        self.plot = FigureCanvasTkAgg(self.fig, master=self)
        self.plot.draw()
        self.plot.get_tk_widget().grid(row=1, column=0, columnspan=2,sticky="nsew")


class Sidebar(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=3)
        self.create_controls()

    def create_controls(self):
        self.name_card = ttk.Label(self, text='Seleccionar', borderwidth=2, relief="solid")
        self.name_card.grid(row=0,column=0, sticky="nsew")

        self.perc_card = PercPlot(self)
        self.perc_card.grid(row=1, column=0, sticky="nsew")

        self.image_card = ttk.Label(self, text="imagen de la fase seleccionada", borderwidth=2, relief="solid")
        self.image_card.grid(row=2, column=0, sticky="nsew")

        self.info_card = ttk.Label(self, text="info de la fase seleccionada", borderwidth=2, relief="solid")
        self.info_card.grid(row=3, column=0, sticky="nsew")

    def handle_graph_click(self, event):
        x, y = event.xdata, event.ydata
        print(f'evento:({x},{y})')

    def load_data(pos):
        porc, temp = pos
        data = get_phase()

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Diagrama Hierro Carbono Interactivo")
        self.geometry("1000x600")

        # layout principal
        app_container: ttk.Frame = ttk.Frame(self)
        app_container.pack(fill=tk.BOTH, expand=True)

        # configurar layout principal
        app_container.rowconfigure(0, weight=1)
        app_container.columnconfigure(0, weight=3)
        app_container.columnconfigure(1, weight=1)

        # componentes

        self.sidebar = Sidebar(app_container)
        self.sidebar.grid(row=0, column=1, sticky="nsew")

        self.plot_frame = InteractivePlot(app_container)
        self.plot_frame.grid(row=0, column=0, sticky="nsew")
        self.plot_frame.canvas.mpl_connect(
            "button_press_event", 
            self.sidebar.handle_graph_click
        )
        #self.update_image_button = tk.Button(self, text="Update Image", command=self.update_image)
        #self.update_image_button.pack()

        #self.image_label = tk.Label(self)
        #self.image_label.pack()
        #self.image = None

        # Tema de estilo
        sv_ttk.set_theme("light")

    #def update_image(self):
        # Your logic to update image goes here
        #route = "path_to_your_image.png"
        #img = Image.open(route)
        #img = img.resize((200, 200), Image.ANTIALIAS)
        #self.image = ImageTk.PhotoImage(img)
        #self.image_label.config(image=self.image)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

