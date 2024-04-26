# importaciones
from utils.get_phase import main as get_phase
import utils.styles as styles
import flet as ft

# Componentes que pertenecen a la interface de la aplicacion
# gui
appbar = ft.AppBar(
    **styles.interface.get("appbar"),
    title=ft.Text("FecGraph"),
    actions=[
        ft.IconButton(ft.icons.DARK_MODE_OUTLINED, tooltip="modo"),
        ft.PopupMenuButton(
            tooltip="Opciones",
            items=[ft.PopupMenuItem(icon=ft.icons.DOWNLOAD, text="Descargar Manual")],
        ),
    ],
)


class Compoundcard(ft.Container):  # tarjeta superior de la barra derecha, muestra la estructura crristalina del compuesto
    def __init__(self):
        super().__init__(**styles.interface.get("card_main"), height=170)
        pass


class InfoCard(ft.Container):  # musetra informacion de una variable en la barra lateral
    def __init__(self, val_info=0, val_suf="", var_name=""):
        super().__init__(**styles.interface.get("card_main"))

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
            size=45,
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


class InfoSnack(
    ft.Container
):  # barras al derecho del grafico, muestran informacion de la seleccion actual
    def __init__(self, var="None", value="--"):
        super().__init__(**styles.interface.get("infosnack"))
        self.content = ft.Row(
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
        )


# phases: Listado de informacion sobre cada fase
phases: list = [
    {
        "name": "Austenita",
        "symbol": "y",
        "crystal": "",
        "description": "En este estado, los aceros son maleabes y faciles de manipular, las altas temperaturas ayudan a su uso.",
        "properties": [
            {"val": "Dúctil"},
            {"name": "Rigidez", "val": "Blanda"},
            {"val": "Tenaz"},
        ],
        "line": [(0, 1390), (0.3, 1450), (2.11, 1147), (0.8, 723), (0, 900)],
        "line_properties": {"color": ft.colors.RED},
    },
    {
        "name": "Ferrita",
        "symbol": "a",
        "crystal": "",
        "description": "Es a fase mas banda que aparece a temperatura abiente, ,lo que la hace muy importante a pesar de su poca cantidad.",
        "properties": [
            {"name": "solubilidad", "val": "0.02%"},
            {"name": "Rigidez", "val": "Blanda"},
        ],
        "line": [(0, 900), (0.15, 780), (0.2, 723), (0.15, 630), (0, 0)],
        "line_properties": {"color": ft.colors.BLUE_100},
    },
    {
        "name": "Cementita",
        "symbol": "Fe3C",
        "crystal": "",
        "description": "Compuesto intermetalico no apropiado para procesos de deformacion plastico",
        "properties": [
            {"name": "Dureza", "val": "Duro"},
            {"name": "Rigidez", "val": "Fragil"},
        ],
        "line": [(0.2, 723), (6.67, 723), (6.67, 0)],
        "line_properties": {"color": ft.colors.GREEN_400},
    },
    {
        "name": "Perlita",
        "symbol": "a + Fe3C",
        "crystal": "",
        "description": "Se forma por la minas alternas de ferrita y cementita a menos de 723°C, posee posee propiedades de ambos.",
        "properties": [{"name": "Resistencia", "val": "Alta"}],
        "line": [(0.8, 723), (0.8, 0)],
        "line_properties": {"color": ft.colors.YELLOW_200, "dash_pattern": [5, 5]},
    },
    {
        "name": "Liquido",
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


phase_lines: list = [
    PhaseLine(phaseData=phase_data)
    for phase_data in phases
    if phase_data.get("line_properties")
]


# chart
class FecChart(ft.LineChart):
    def __init__(self):
        super().__init__(**styles.chart_styles.get("fec"))

        self.data_series = phase_lines

    def create_data_point(self, x, y):
        self.test_points.append(ft.LineChartDataPoint(x, y))
        self.update()


# view
class ViewUpperpart(ft.Tabs):
    def __init__(self):
        super().__init__(height=200)

        self.container = ft.Container(**styles.interface.get("panel"))
        self.tabs = [ft.Tab(content=self.container)]

    def updateInfo(self, data):
        self.data = data
        self.tabs = self._build_tabs()
        self.update()

    def _build_tabs(self):
        return [
            ft.Tab(
                text=self._format_tab_text(item),
                content=ft.Container(
                    **styles.interface.get("panel"),
                    content=ft.Text(
                        self._get_phase_description(item["name"]),
                        color=ft.colors.SURFACE,
                    ),
                ),
            )
            for item in self.data
        ]

    def _format_tab_text(self, item):
        pure_text = 'pura' if item.get('pure') else ''
        num_text = str(item.get('num') or '')
        porc_text = '%.1f' % (item.get('porc') or 0)
        return f"{item['name']} {pure_text} {num_text} ({porc_text})%"

    def _get_phase_description(self, phase_name):
        return next(
            filter(lambda phase: phase.get("name") == phase_name, self.phases),
            {}
        ).get("description")



class ViewLowerpart(ft.Container):
    def __init__(self):
        super().__init__(expand=True)
        self.chart = FecChart()
        self.props_list_view = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.content = ft.Row(
            controls=[
                ft.Container(expand=True, padding=ft.Padding(10, 10, 10, 10), content=self.chart),
                ft.Container(**styles.interface.get("card_main"), width=220, content=self.props_list_view),
            ]
        )

    def updateProperties(self, data):
        info_snacks = [InfoSnack(prop.get("name"), prop.get("val")) for prop in data]
        self.props_list_view.controls.clear()
        self.props_list_view.controls.extend(info_snacks)
        self.props_list_view.update()


class View(ft.Container):
    def __init__(self):
        super().__init__(**styles.interface.get("view"))
        self.upperpart: ViewUpperpart = ViewUpperpart()
        self.lowerpart: ViewLowerpart = ViewLowerpart()
        self.content = ft.Column(controls=[self.upperpart, self.lowerpart])

    pass


class Sidebar(ft.Container):
    def __init__(self):
        super().__init__(**styles.interface.get("sidebar"))

        self.phase_card = Compoundcard()

        self.temperature = InfoCard(val_info=20, val_suf="°F", var_name="T°")
        self.percentage = InfoCard(val_suf="%", var_name="C%")

        self.t_input = ft.Slider(**styles.interface.get("field_t"), label="{value}°F")
        self.p_input = ft.Slider(**styles.interface.get("field_p"), label="{value}%")

        self.content = ft.Column(
            scroll=ft.ScrollMode.ADAPTIVE,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.VerticalAlignment.CENTER,
            controls=[
                self.phase_card,
                self.temperature,
                self.t_input,
                self.percentage,
                self.p_input,
            ],
        )
    
    def set_image():
        
        pass


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

        self.view.upperpart.on_change = lambda e: self.update_properties(int(e.data))

        super().__init__(
            **styles.interface.get("main"),
            content=ft.Row(controls=[self.view, self.sidebar], expand=True),
        )

    def update_values(self, event):

        t_delta: str = self.sidebar.t_input.value
        p_delta: str = self.sidebar.p_input.value

        self.t_counter = t_delta
        self.sidebar.temperature.updateValue("%.0f" % self.t_counter)

        self.p_counter = p_delta
        self.sidebar.percentage.updateValue(self.p_counter)

        self.current_data = get_phase(p_delta, t_delta) or [{"name": "None"}]
        self.view.upperpart.updateInfo(self.current_data)
        self.update_properties()
        self.update_chart()

    def update_properties(self, index=0):

        properties: list = next(
            filter(
                lambda phase: phase.get("name") == self.current_data[index].get("name"),
                self.phases,
            ), {}
        ).get("properties")
        self.view.lowerpart.updateProperties(properties)

    def update_chart(self):
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
