# importaciones
from utils.get_phase import main as get_phase
import flet as ft

# Dicionario de estilos de los componentes
styles: dict = {
    "main": {"expand": True},
    "card_main": {
        "padding": ft.Padding(10, 10, 10, 10),
        "margin": ft.Margin(0, 0, 0, 0),
        "border_radius": ft.BorderRadius(10, 10, 10, 10),
        "bgcolor": ft.colors.SURFACE,
    },
    "card_alt": {
        "padding": ft.Padding(20, 20, 20, 20),
        "margin": ft.Margin(0, 0, 0, 0),
        "border_radius": ft.BorderRadius(10, 10, 10, 10),
        "bgcolor": ft.colors.SECONDARY,
    },
    "sidebar": {
        "bgcolor": ft.colors.SURFACE_VARIANT,
        "width": 220,
        "alignment": ft.alignment.center,
        "border_radius": ft.BorderRadius(10, 10, 10, 10),
        "padding": ft.Padding(left=20, top=30, right=20, bottom=0),
    },
    "field": {
        "height": 30,
    },
    "view": {
        "expand": True,
        "padding": ft.Padding(20, 20, 20, 20),
        "border_radius": ft.BorderRadius(10, 10, 10, 10),
        "bgcolor": ft.colors.SURFACE_VARIANT,
    },
}

chart_styles: dict = {
    "fec": {
        "max_y": 1600,
        "min_y": 20,
        "max_x": 6.67,
        "min_x": 0,
        "interactive": True,
        "expand": True,
        "border": ft.border.all(1, ft.colors.GREY_400),
        "left_axis": ft.ChartAxis(labels_size=40),
        "bottom_axis": ft.ChartAxis(labels_size=40),
        "horizontal_grid_lines": ft.ChartGridLines(
            interval=100,
            color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE),
            width=1,
            dash_pattern=[2],
        ),
        "vertical_grid_lines": ft.ChartGridLines(
            interval=1,
            color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE),
            dash_pattern=[2],
        ),
    }
}


# Componentes que pertenecen a la interface de la aplicacion
# gui
appbar = ft.AppBar(
    leading=ft.Icon(ft.icons.ABC),
    leading_width=40,
    title=ft.Text("FecGraph"),
    center_title=False,
    bgcolor=ft.colors.SURFACE_VARIANT,
    actions=[
        ft.IconButton(ft.icons.DARK_MODE_OUTLINED, tooltip="modo"),
        ft.PopupMenuButton(
            tooltip="Opciones",
            items=[ft.PopupMenuItem(icon=ft.icons.DOWNLOAD, text="Descargar Manual")],
        ),
    ],
    elevation=1,
)


def Compoundcard():  # tarjeta superior de la barra derecha, muestra la estructura crristalina del compuesto
    return ft.Container(**styles.get("card_main"), height=170)


class InfoCard(ft.Container):  # musetra informacion de una variable en la barra lateral
    def __init__(self, val_info=0, val_suf="", var_name=""):
        super().__init__(**styles.get("card_main"))

        self.var_name = var_name
        self.val_suf = val_suf
        self.val_info = val_info

        self.var_text = ft.Text(  # variable en la esquina izquiera
            self.var_name,
            color=ft.colors.SURFACE_TINT,
            weight=ft.FontWeight.W_900,
        )
        self.val_text = ft.Text(  # valor actual en el centro
            f"{self.val_info}{self.val_suf}",
            color=ft.colors.SURFACE_TINT,
            weight=ft.FontWeight.W_700,
            size=50,
        )

        self.content = ft.Column(
            controls=[
                ft.Container(height=20, content=self.var_text),
                ft.Container(
                    bgcolor=ft.colors.SECONDARY_CONTAINER,
                    border_radius=ft.BorderRadius(10, 10, 10, 10),
                    alignment=ft.alignment.center,
                    content=self.val_text,
                ),
            ]
        )

    def updateValue(self, new_value):  # actualizar valor, recibe un valor y lo añade
        self.val_info = new_value
        self.val_text.value = f"{self.val_info}{self.val_suf}"
        self.val_text.update()


def Infobar(
    var="None", value="--"
):  # barras al derecho del grafico, muestran informacion de la seleccion actual
    return ft.Container(
        bgcolor=ft.colors.SURFACE_VARIANT,
        border_radius=ft.BorderRadius(10, 10, 10, 10),
        content=ft.Row(
            controls=[
                ft.Container(
                    padding=ft.Padding(20, 10, 0, 10),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    expand=True,
                    content=ft.Text(var, weight=ft.FontWeight.W_600),
                ),
                ft.Container(
                    padding=ft.Padding(0, 10, 0, 10),
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.SECONDARY_CONTAINER,
                    expand=True,
                    content=ft.Text(value, color=ft.colors.SURFACE_TINT),
                ),
            ]
        ),
    )


# phases: Listado de informacion sobre cada fase
phases: list = [
    {
        "name": "Austenita",
        "symbol": "y",
        "crystal": "",
        "description": "En este estado, los aceros son maleabes y faciles de manipular, las altas temperaturas ayudan a su uso.",
        "properties": {"p1": "Dúctil", "Rigidez": "Blanda", "p3": "Tenaz"},
        "line": [(0, 1390), (0.3, 1450), (2.11, 1147), (0.8, 723), (0, 900)],
        "line_properties": {
            "color": ft.colors.RED,
        },
    },
    {
        "name": "Ferrita",
        "symbol": "a",
        "crystal": "",
        "description": "Es a fase mas banda que aparece a temperatura abiente, ,lo que la hace muy importante a pesar de su poca cantidad.",
        "properties": {"solubilidad": "0.02%", "Rigidez": "Blanda"},
        "line": [(0, 900), (0.15, 780), (0.2, 723), (0.15, 630), (0, 0)],
        "line_properties": {
            "color": ft.colors.BLUE_100,
        },
    },
    {
        "name": "Cementita",
        "symbol": "Fe3C",
        "crystal": "",
        "description": "Compuesto intermetalico no apropiado para procesos de deformacion plastico",
        "properties": {"Dureza": "Duro", "Rigidez": "Fragil"},
        "line": [(0.2, 723), (6.67, 723), (6.67, 0)],
        "line_properties": {
            "color": ft.colors.GREEN_400,
        },
    },
    {
        "name": "Perlita",
        "symbol": "a + Fe3C",
        "crystal": "",
        "description": "Se forma por la minas alternas de ferrita y cementita a menos de 723°C, posee posee propiedades de ambos.",
        "properties": {"Resistencia": "Alta"},
        "line": [(0.8, 723), (0.8, 0)],
        "line_properties": {"color": ft.colors.YELLOW_200, "dash_pattern": [5, 5]},
    },
]


class PhaseLine(ft.LineChartData):
    def __init__(self, phaseData: dict):
        super().__init__()
        self.stroke_width = (2,)
        self.curved = (True, True)
        self.phase_data = phaseData
        self.color = self.phase_data["line_properties"]["color"]
        self.data_points = self.convert_to_chart_data(self.phase_data["line"])

    def convert_to_chart_data(
        self, line_data: list[tuple[float, float]]
    ) -> list[ft.LineChartDataPoint]:
        chart_data_points = []
        for point in line_data:
            x, y = point
            data_point = ft.LineChartDataPoint(
                x=x, y=y, show_tooltip=True, tooltip=self.phase_data["name"]
            )
            chart_data_points.append(data_point)
        return chart_data_points


phase_lines: list = [PhaseLine(phaseData=phase_data) for phase_data in phases]


# chart
class FecChart(ft.LineChart):
    def __init__(self):
        super().__init__(**chart_styles.get("fec"))

        self.data_series = phase_lines

    def create_data_point(self, x, y):
        self.test_points.append(ft.LineChartDataPoint(x, y))
        self.update()


# view
class ViewUpperpart(ft.Container):
    def __init__(self):
        super().__init__(**styles.get("card_alt"), height=150)

        self.content = ft.Row(
            controls=[
                ft.Column(
                    expand=True,
                    controls=[
                        ft.Text(
                            "Fase",
                            color=ft.colors.SURFACE,
                            size=20,
                            weight=ft.FontWeight.W_900,
                        ),
                        ft.Text(
                            "Descripcion de la Fase Lorem inpsum dalur dolores armin del  galardium merte colorde ajisto.",
                            color=ft.colors.SURFACE,
                        ),
                    ],
                ),
                ft.Column(
                    expand=True,
                    controls=[
                        ft.Text("", color=ft.colors.SURFACE),
                        ft.Text(
                            "Informacion adicional dalur dolores armin del forsen cancede ilumi tente o mais galardium merte  ajisto.",
                            color=ft.colors.SURFACE,
                        ),
                    ],
                ),
            ]
        )


class ViewLowerpart(ft.Container):
    def __init__(self):
        super().__init__(expand=True)
        self.chart: FecChart = FecChart()
        self.content = ft.Row(
            controls=[
                ft.Container(
                    expand=True, padding=ft.Padding(10, 10, 10, 10), content=self.chart
                ),
                ft.Container(
                    **styles.get("card_main"),
                    width=200,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            Infobar(),
                            Infobar(),
                            Infobar(),
                            Infobar(),
                        ],
                    ),
                ),
            ]
        )


class View(ft.Container):
    def __init__(self):
        super().__init__(**styles.get("view"))
        self.upperpart: ViewUpperpart = ViewUpperpart()
        self.lowerpart: ViewLowerpart = ViewLowerpart()
        self.content = ft.Column(controls=[self.upperpart, self.lowerpart])

    pass


class Sidebar(ft.Container):
    def __init__(self):
        super().__init__(**styles.get("sidebar"))

        self.temperature = InfoCard(val_info=20, val_suf="°F", var_name="T°")
        self.percentage = InfoCard(val_suf="%", var_name="C%")

        self.t_input = ft.Slider(
            **styles.get("field"),
            min=20,
            max=1600,
            divisions=15,
            label="{value}°F",
            value=20,
            round=1,
        )
        self.p_input = ft.Slider(
            **styles.get("field"),
            min=0,
            max=6.67,
            divisions=6,
            label="{value}%",
            value=0,
        )

        self.content = ft.Column(
            scroll=ft.ScrollMode.ADAPTIVE,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.VerticalAlignment.CENTER,
            controls=[
                Compoundcard(),
                self.temperature,
                self.t_input,
                self.percentage,
                self.p_input,
            ],
        )


class FecGraph(ft.Container):
    def __init__(self, view: View, sidebar: Sidebar):

        self.phases = phases

        self.t_counter = 0
        self.p_counter = 0

        self.view: View = view
        self.sidebar: Sidebar = sidebar

        self.sidebar.t_input.on_change_end = lambda e: self.update_values(e)
        self.sidebar.p_input.on_change_end = lambda e: self.update_values(e)

        self.view.lowerpart.phases = self.phases
        self.view.upperpart.phases = self.phases
        self.sidebar.phases = self.phases
        self.view.phases = self.phases

        super().__init__(
            **styles.get("main"),
            content=ft.Row(controls=[self.view, self.sidebar], expand=True),
        )

    def update_values(self, event):

        t_delta: str = self.sidebar.t_input.value
        p_delta: str = self.sidebar.p_input.value

        if t_delta <= 1600 and t_delta >= 20:
            self.t_counter = t_delta
            self.sidebar.temperature.updateValue("%.0f" % self.t_counter)

        if p_delta <= 6.67 and p_delta >= 0:
            self.p_counter = p_delta
            self.sidebar.percentage.updateValue("%.1f" % self.p_counter)

        print(p_delta, t_delta, get_phase(p_delta, t_delta))

    pass


# main
def main(page: ft.Page):
    page.title = "FecGraph"
    page.appbar = appbar

    view: ft.Container = View()
    sidebar: ft.Container = Sidebar()
    app: ft.Container = FecGraph(view=view, sidebar=sidebar)

    page.add(app)


ft.app(target=main)
