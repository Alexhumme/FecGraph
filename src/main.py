import flet as ft


# interface
def Compoundcard():
    return ft.Container(
        padding=ft.Padding(10, 10, 10, 10),
        margin=ft.Margin(0, 0, 0, 0),
        border_radius=ft.BorderRadius(10, 10, 10, 10),
        bgcolor=ft.colors.SURFACE,
        height=170,
    )


def Infocard(value: str, var=""):
    return ft.Container(
        padding=ft.Padding(10, 10, 10, 10),
        margin=ft.Margin(0, 0, 0, 0),
        border_radius=ft.BorderRadius(10, 10, 10, 10),
        bgcolor=ft.colors.SURFACE,
        content=ft.Column(
            controls=[
                ft.Container(
                    height=20,
                    content=ft.Text(
                        var,
                        color=ft.colors.SURFACE_TINT,
                        weight=ft.FontWeight.W_900,
                    ),
                ),
                ft.Container(
                    bgcolor=ft.colors.SECONDARY_CONTAINER,
                    border_radius=ft.BorderRadius(10, 10, 10, 10),
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        value,
                        color=ft.colors.SURFACE_TINT,
                        weight=ft.FontWeight.W_700,
                        size=50,
                    ),
                ),
            ]
        ),
    )


def Infoinput():
    return ft.Container(
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextField(
                    height=30,
                    width=110,
                    filled=True,
                    border_radius=ft.BorderRadius(10, 10, 10, 10),
                    border_color=ft.colors.TRANSPARENT,
                    bgcolor=ft.colors.SURFACE,
                    text_style=ft.TextStyle(color=ft.colors.SECONDARY, size=12),
                ),
                ft.IconButton(
                    ft.icons.CHECK,
                    style=ft.ButtonStyle(elevation=0.1),
                    bgcolor=ft.colors.SECONDARY_CONTAINER,
                ),
            ],
        ),
    )


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


gridswitch = ft.Switch("Mostrar grilla")

# gui
appbar = ft.AppBar(
    leading=ft.Icon(ft.icons.ABC),
    leading_width=40,
    title=ft.Text("FecGraph"),
    center_title=False,
    bgcolor=ft.colors.SURFACE_VARIANT,
    actions=[
        ft.PopupMenuButton(
            tooltip="Opciones",
            items=[ft.PopupMenuItem(icon=ft.icons.DOWNLOAD, text="Descargar Manual")],
        ),
    ],
    elevation=1,
)
sidebar = ft.Container(
    bgcolor=ft.colors.SURFACE_VARIANT,
    width=220,
    alignment=ft.alignment.center,
    border_radius=ft.BorderRadius(10, 10, 10, 10),
    padding=ft.Padding(left=20, top=30, right=20, bottom=0),
    content=ft.Column(
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.VerticalAlignment.CENTER,
        controls=[
            Compoundcard(),
            Infocard("0°F", var="T°"),
            Infoinput(),
            Infocard("0%", var="C%"),
            Infoinput(),
        ],
    ),
)
# chart
chart = ft.BarChart(
    bar_groups=[
        ft.BarChartGroup(
            x=0,
            bar_rods=[
                ft.BarChartRod(
                    from_y=0,
                    to_y=40,
                    width=40,
                    color=ft.colors.AMBER,
                    tooltip="Apple",
                    border_radius=0,
                ),
            ],
        ),
        ft.BarChartGroup(
            x=1,
            bar_rods=[
                ft.BarChartRod(
                    from_y=0,
                    to_y=100,
                    width=40,
                    color=ft.colors.BLUE,
                    tooltip="Blueberry",
                    border_radius=0,
                ),
            ],
        ),
        ft.BarChartGroup(
            x=2,
            bar_rods=[
                ft.BarChartRod(
                    from_y=0,
                    to_y=30,
                    width=40,
                    color=ft.colors.RED,
                    tooltip="Cherry",
                    border_radius=0,
                ),
            ],
        ),
        ft.BarChartGroup(
            x=3,
            bar_rods=[
                ft.BarChartRod(
                    from_y=0,
                    to_y=60,
                    width=40,
                    color=ft.colors.ORANGE,
                    tooltip="Orange",
                    border_radius=0,
                ),
            ],
        ),
    ],
    border=ft.border.all(1, ft.colors.GREY_400),
    left_axis=ft.ChartAxis(
        labels_size=40, title=ft.Text("Temperatura (grados Farenheig)"), title_size=40
    ),
    bottom_axis=ft.ChartAxis(
        labels_size=40, title=ft.Text("Porcentaje de carbono"), title_size=40
    ),
    horizontal_grid_lines=ft.ChartGridLines(
        color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
    ),
    tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
    max_y=110,
    interactive=True,
    expand=True,
)
# view
view_upperpart = ft.Container(
    padding=ft.Padding(20, 20, 20, 20),
    height=150,
    bgcolor=ft.colors.SECONDARY,
    border_radius=ft.BorderRadius(10, 10, 10, 10),
    content=ft.Row(
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
    ),
)
view_lowerpart = ft.Container(
    expand=True,
    content=ft.Row(
        controls=[
            ft.Container(
                expand=True, padding=ft.Padding(10, 10, 10, 10), content=chart
            ),
            ft.Container(
                width=200,
                bgcolor=ft.colors.SURFACE,
                border_radius=ft.BorderRadius(10, 10, 10, 10),
                padding=ft.Padding(10, 10, 10, 10),
                content=ft.Column(
                    controls=[
                        Infobar(),
                        Infobar(),
                        Infobar(),
                        Infobar(),
                    ],
                    # alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
        ]
    ),
)

view = ft.Container(
    expand=True,
    padding=ft.Padding(20, 20, 20, 20),
    border_radius=ft.BorderRadius(10, 10, 10, 10),
    bgcolor=ft.colors.SURFACE_VARIANT,
    content=ft.Column(controls=[view_upperpart, view_lowerpart]),
)

body = ft.Row(controls=[view, sidebar], expand=True)


# main
def main(page: ft.Page):
    page.title = "FecGraph"
    page.appbar = appbar

    page.add(body)


ft.app(target=main)
