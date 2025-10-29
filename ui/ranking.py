import flet as ft

def ranking_page(page, user=None, on_back_home=None):
    page.controls.clear()
    page.bgcolor = ft.Colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # --- Texto principal ---
    message = ft.Text(
        "🛠️ En desarrollo...",
        size=30,
        weight="bold",
        color=ft.Colors.AMBER_300,
        text_align=ft.TextAlign.CENTER,
    )

    # --- Botón volver ---
    back_button = ft.ElevatedButton(
        "Volver al menú",
        width=200,
        height=50,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.PURPLE_700,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=12),
            overlay_color=ft.Colors.with_opacity(0.2, ft.Colors.WHITE),
            elevation=6,
        ),
        on_click=lambda e: on_back_home() if on_back_home else None
    )

    # --- Contenedor principal ---
    container = ft.Column(
        [message, back_button],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=30,
    )

    page.add(container)
    page.update()
