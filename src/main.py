import flet as ft

# styles
styles: dict = {
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
        "max_y": 110,
        "interactive": True,
        "expand": True,
        "border": ft.border.all(1, ft.colors.GREY_400),
        "left_axis": ft.ChartAxis(labels_size=50),
        "bottom_axis": ft.ChartAxis(labels_interval=1, labels_size=40),
        "horizontal_grid_lines": ft.ChartGridLines(
            interval=10,
            color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE),
            width=1,
        ),
    }
}


# app class
class Sidebar(ft.Container):
    def __init__(self):
        super().__init__(**styles.get("sidebar"))

        self.t_counter = 0
        self.p_counter = 0

        self.temperature = InfoCard(val_suf="°F", var_name="T°")
        self.percentage = InfoCard(val_suf="%", var_name="C%")

        self.t_input = ft.TextField(
            **styles.get("field"), keyboard_type=ft.KeyboardType.NUMBER
        )
        self.p_input = ft.TextField(
            **styles.get("field"), keyboard_type=ft.KeyboardType.NUMBER
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
                ft.Row(
                    controls=[
                        ft.OutlinedButton(
                            text="Calcular",
                            icon=ft.icons.CHECK,
                            expand=True,
                            height=30,
                            on_click=lambda e: self.update_values(e),
                        ),
                    ]
                ),
            ],
        )

    def update_values(self, event):
        if self.t_input != "" and self.t_input.value.isdigit():
            self.t_counter = self.t_input.value
            self.temperature.updateValue(self.t_counter)
            self.t_input.value = ""
            self.t_input.update()

        if self.p_input != "" and self.p_input.value.isdigit():
            self.p_counter = self.p_input.value
            self.percentage.updateValue(self.p_counter)
            self.p_input.value = ""
            self.p_input.update()


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
        self.curved = (True,)
        self.stroke_cap_round = (True,)
        self.below_line_bgcolor = color


# chart
class FecChart(ft.LineChart):
    def __init__(self):
        super().__init__(**chart_styles.get("fec"))

        self.test_points: list = []

        self.min_x = (
            int(min(self.points, key=lambda x: x[0][0])) if self.test_points else None
        )
        self.max_x = (
            int(max(self.points, key=lambda x: x[0][0])) if self.test_points else None
        )

        self.test_line: ft.LineChartData = PhaseLine(color=ft.colors.RED)
        self.test_line.data_points = self.test_points

        self.data_series = [self.test_line]

    def create_data_points(self, x, y):
        self.test_points.append(
            ft.LineChartDataPoint(
                x,
                y,
                selected_below_line=ft.ChartPointLine(
                    width=0.5, color="green", dash_pattern=[2, 4]
                ),
                selected_point=ft.ChartCirclePoint(
                    stroke_width=1, stroke_color="violet"
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
        self.chart: ft.LineChart = FecChart()
        self.content = ft.Row(
            controls=[
                ft.Container(
                    expand=True, padding=ft.Padding(10, 10, 10, 10), content= self.chart
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
        view_upperpart: ft.Container = ViewUpperpart()
        view_lowerpart: ft.Container = ViewLowerpart()
        self.content = ft.Column(controls=[view_upperpart, view_lowerpart])

    pass


class FecGraph(ft.Container):
    def __init__(self):
        super().__init__(**styles.get("main"))

        view: ft.Container = View()
        sidebar: ft.Container = Sidebar()
        self.content = ft.Row(controls=[view, sidebar], expand=True)

    pass


# main
def main(page: ft.Page):
    page.title = "FecGraph"
    page.appbar = appbar

    sidebar: ft.Container = Sidebar()
    view: ft.Container = View()
    body = ft.Row(controls=[view, sidebar], expand=True)

    page.add(body)


ft.app(target=main)
