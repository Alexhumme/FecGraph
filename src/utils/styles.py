import flet as ft

# Dicionario de estilos de los componentes
interface: dict = {
    "main": {"expand": True},
    "appbar": {
        "leading": ft.Icon(ft.icons.ABC),
        "leading_width": 40,
        "center_title": False,
        "bgcolor": ft.colors.SURFACE_VARIANT,
    },
    "infosnack":{
        "bgcolor":ft.colors.SURFACE_VARIANT,
        "border_radius":ft.BorderRadius(10, 10, 10, 10),
    },
    "card_main": {
        "padding": ft.Padding(10, 10, 10, 10),
        "margin": ft.Margin(0, 0, 0, 0),
        "border_radius": ft.BorderRadius(10, 10, 10, 10),
        "bgcolor": ft.colors.SURFACE,
    },
    "card_tight": {
        "margin": ft.Margin(0, 0, 0, 0),
        "border_radius": ft.BorderRadius(10, 10, 10, 10),
        "bgcolor": ft.colors.SURFACE,
    },
    "panel": {
        "padding": ft.Padding(20, 20, 20, 20),
        "margin": ft.Margin(5, 5, 5, 5),
        "border_radius": ft.BorderRadius(10, 10, 10, 10),
        "bgcolor": ft.colors.SECONDARY,
        "expand":True,
    },
    "sidebar": {
        "bgcolor": ft.colors.SURFACE_VARIANT,
        "width": 220,
        "alignment": ft.alignment.center,
        "border_radius": ft.BorderRadius(10, 10, 10, 10),
        "padding": ft.Padding(left=20, top=30, right=20, bottom=0),
    },
    "field_t": {
        "height": 30,
        "min":20,
        "max":1600,
        "divisions":32,
        "value":20,
        "round":0
    },
    "field_p": {
        "height": 30,
        "min":0,
        "max":7,
        "divisions":14,
        "value":0,
        "round":1
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
        "max_x": 7,
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
    },
    "fectly": {
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
    },
}
