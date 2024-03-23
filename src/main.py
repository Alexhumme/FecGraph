import flet as ft

# styles
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
        # "height": 30,
        "filled": True,
        "border_radius": ft.BorderRadius(10, 10, 10, 10),
        "border_color": ft.colors.TRANSPARENT,
        "bgcolor": ft.colors.SURFACE,
        "text_style": ft.TextStyle(color=ft.colors.SECONDARY),  # , size=12),
        "text_align": ft.TextAlign.CENTER,
        "height": 30,
        "text_size": 12,
        "text_vertical_align": ft.VerticalAlignment.START,
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


# interface
def Compoundcard():
    return ft.Container(
        **styles.get("card_main"),
        height=170,
    )


class InfoCard(ft.Container):
    def __init__(self, val_info=0, val_suf="", var_name=""):
        super().__init__(**styles.get("card_main"))

        self.var_name = var_name
        self.val_suf = val_suf
        self.val_info = val_info

        self.var_text = ft.Text(
            self.var_name,
            color=ft.colors.SURFACE_TINT,
            weight=ft.FontWeight.W_900,
        )
        self.val_text = ft.Text(
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

    def updateValue(self, new_value):
        self.val_info = new_value
        self.val_text.value = f"{self.val_info}{self.val_suf}"
        self.val_text.update()


def Infobar(value="--", var="None"):
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


class PhaseLine(ft.LineChartData):
    def __init__(self, color, points=[]):
        super().__init__()
        self.color = color
        self.stroke_width = (2,)
        self.curved = (True,True)
        self.stroke_cap_round = (True,True)
        self.below_line_bgcolor = color


# chart
class FecChart(ft.LineChart):
    def __init__(self):
        super().__init__(**chart_styles.get("fec"))

        self.test_points: list = []

        self.test_line: ft.LineChartData = PhaseLine(color=ft.colors.RED)
        self.test_line.data_points = self.test_points

        self.data_series = [self.test_line]

    def create_data_point(self, x, y):
        self.test_points.append(
            ft.LineChartDataPoint(
                x,
                y,
                selected_below_line=ft.ChartPointLine(
                    width=5, color="green", dash_pattern=[2, 4]
                ),
                selected_point=ft.ChartCirclePoint(
                    stroke_width=10, stroke_color="violet"
                ),
            )
        )
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

        self.temperature = InfoCard(val_suf="°F", var_name="T°")
        self.percentage = InfoCard(val_suf="%", var_name="C%")

        self.t_input = ft.TextField(
            **styles.get("field"), keyboard_type=ft.KeyboardType.NUMBER
        )
        self.p_input = ft.TextField(
            **styles.get("field"), keyboard_type=ft.KeyboardType.NUMBER
        )
        self.act_btn = ft.OutlinedButton(
            text="Calcular",
            icon=ft.icons.CHECK,
            expand=True,
            height=30,
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
                ft.Row(controls=[self.act_btn]),
            ],
        )


class FecGraph(ft.Container):
    def __init__(self, view: View, sidebar: Sidebar):

        self.t_counter = 0
        self.p_counter = 0

        self.view: View = view
        self.sidebar: Sidebar = sidebar

        self.sidebar.act_btn.on_click = lambda e: self.update_values(e)
        super().__init__(
            **styles.get("main"),
            content=ft.Row(controls=[self.view, self.sidebar], expand=True),
        )

    def update_values(self, event):
        
        t_delta: str = self.sidebar.t_input.value
        p_delta: str = self.sidebar.p_input.value
        if  t_delta != "" and t_delta.isdigit() and float(t_delta) <= 1600 and float(t_delta) >= 20:
            self.t_counter = t_delta
            self.sidebar.temperature.updateValue(self.t_counter)
            self.sidebar.t_input.value = ""
            self.sidebar.t_input.update()

        if p_delta != "" and p_delta.isdigit() and float(p_delta) <= 6.67 and float(p_delta) >= 0:
            self.p_counter = p_delta
            self.sidebar.percentage.updateValue(self.p_counter)
            self.sidebar.p_input.value = ""
            self.sidebar.p_input.update()

        if self.t_counter or self.p_counter:
            self.view.lowerpart.chart.create_data_point(
                x = self.p_counter,
                y = self.t_counter
            )

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
