import tkinter as tk
import sv_ttk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

# phases: Listado de informacion sobre cada fase
phases = [
    {
        "name": "Austenita",
        "symbol": "y",
        "crystal": "",
        "description": "En este estado, los aceros son maleables y fáciles de manipular, las altas temperaturas ayudan a su uso.",
        "properties": [
            {"name":"","val": "Dúctil"},
            {"name": "Rigidez", "val": "Blanda"},
            {"name":"","val": "Tenaz"},
        ],
        "line_x": [0, 0.3, 2.11, 0.8, 0],
        "line_y": [1390, 1450, 1147, 723, 900],
        "line_properties": {"color": 'r'},
        "img": "austenita.png"
    },
    {
        "name": "Ledeburita",
        "symbol": "y",
        "crystal": "",
        "description": "En este estado, los aceros son maleables y fáciles de manipular, las altas temperaturas ayudan a su uso.",
        "properties": [
            {"name":"","val": "Dúctil"},
            {"name": "Rigidez", "val": "Blanda"},
            {"name":"","val": "Tenaz"},
        ],
        "line_x": [0, 0.3, 2.11, 0.8, 0],
        "line_y": [1390, 1450, 1147, 723, 900],
        "line_properties": {"color": 'r'},
        "img": "ledeburita.png"
    },
    {
        "name": "Ferrita",
        "symbol": "a",
        "crystal": "",
        "description": "Es la fase más blanda que aparece a temperatura ambiente, lo que la hace muy importante a pesar de su poca cantidad.",
        "properties": [
            {"name": "solubilidad", "val": "0.02%"},
            {"name": "Rigidez", "val": "Blanda"},
        ],
        "line_x": [0, 0.15, 0.2, 0.15, 0],
        "line_y": [900, 780, 723, 630, 0],
        "line_properties": {"color": 'b'},
        "img": "ferrita.png"
    },
    {
        "name": "Cementita",
        "symbol": "Fe3C",
        "crystal": "",
        "description": "Compuesto intermetálico no apropiado para procesos de deformación plástica",
        "properties": [
            {"name": "Dureza", "val": "Duro"},
            {"name": "Rigidez", "val": "Frágil"},
        ],
        "line_x": [0.2, 6.67, 6.67],
        "line_y": [723, 723, 0],
        "line_properties": {"color": 'g'},
        "img": "cementita.png"
    },
    {
        "name": "Perlita",
        "symbol": "a + Fe3C",
        "crystal": "",
        "description": "Se forma por las láminas alternas de ferrita y cementita a menos de 723°C, posee propiedades de ambos.",
        "properties": [{"name": "Resistencia", "val": "Alta"}],
        "line_x": [0.8, 0.8],
        "line_y": [723, 0],
        "line_properties": {"color": 'y'},#"dash_pattern": [5, 5]},
        "img": "austenita.png"
    },
    {
        "name": "Líquido",
        "img": "liquido.png"
    },
]

class InfoPanel(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.label = ttk.Label(self, text="Información de la Fase")
        self.label.pack()

    def update_info(self, phase):
        properties_str = "\n".join([f"{prop['name']}: {prop['val']}" for prop in phase.get('properties', [])])
        self.label.config(text=f"Nombre: {phase['name']}\nDescripción: {phase['description']}\nPropiedades:\n{properties_str}")

class InteractivePlot(ttk.Frame):
    def __init__(self, master, panel):
        super().__init__(master)
        self.pack()
        self.panel = panel  # Panel para mostrar información adicional
        
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.ax.set_xlabel("Porcentaje de carbono (C%)")
        self.ax.set_ylabel("Temperatura (°F)")
        self.ax.set_xlim(0, 7)
        self.ax.set_ylim(20, 1600)
        self.ax.grid()

        # Add data from phases
        self.lines = []
        for phase in phases:
            line, = self.ax.plot(phase.get("line_x", []), phase.get("line_y", []), label=phase.get("name", ""), **phase.get("line_properties", {}))
            self.lines.append((line, phase))

        self.canvas.mpl_connect("motion_notify_event", self.on_hover)
        self.canvas.mpl_connect("button_press_event", self.on_click)
        self.tooltip = None

    def on_hover(self, event):
        if event.inaxes == self.ax:
            x, y = event.xdata, event.ydata
            if self.tooltip:
                self.tooltip.remove()
            self.tooltip = self.ax.annotate(
                f"x={x:.2f}, y={y:.2f}",
                xy=(x, y), xytext=(20, 20),
                textcoords="offset points", ha="center", va="bottom",
                bbox=dict(boxstyle="round,pad=0.5", fc="yellow", alpha=0.5),
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0")
            )
            self.canvas.draw_idle()
        else:
            if self.tooltip:
                self.tooltip.remove()
                self.tooltip = None
                self.canvas.draw_idle()

    def on_click(self, event):
        if event.inaxes == self.ax:
            for line, phase in self.lines:
                if line.contains(event)[0]:
                    x, y = event.xdata, event.ydata
                    if self.tooltip:
                        self.tooltip.remove()
                    self.tooltip = self.ax.annotate(
                        f"{phase['name']}",
                        xy=(x, y), xytext=(20, 20),
                        textcoords="offset points", ha="center", va="bottom",
                        bbox=dict(boxstyle="round,pad=0.5", fc="yellow", alpha=0.5),
                        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0")
                    )
                    self.panel.update_info(phase)
                    self.canvas.draw_idle()
                    break

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        sv_ttk.set_theme("dark")

        self.title("Interactive Plot Example")

        self.panel = InfoPanel(self)
        self.panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

        self.plot_frame = InteractivePlot(self, self.panel)
        self.plot_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.update_image_button = ttk.Button(self, text="Update Image", command=self.update_image)
        self.update_image_button.pack()

        self.image_label = ttk.Label(self)
        self.image_label.pack()
        self.image = None

    def update_image(self):
        # Your logic to update image goes here
        route = "src/resources/images/austenita.png"
        img = Image.open(route)
        img = img.resize((200, 200))
        self.image = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.image)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

