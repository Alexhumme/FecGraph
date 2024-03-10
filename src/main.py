import flet as ft

def main(page: ft.Page):
    page.title = "FecGraph"

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.ABC),
        leading_width=40,
        title=ft.Text("FecGraph"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.PopupMenuButton(
                tooltip = "Opciones",
                items=[
                    ft.PopupMenuItem(icon=ft.icons.DOWNLOAD, text="Descargar Manual")
                ]
            ),
        ],
    )
    body = ft.Row(controls=[ft.Container(), ft.Container()])
    page.add(body)


ft.app(target=main)
