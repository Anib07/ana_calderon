import flet as ft
from ui.login import login_page  

def home_page(page, user, on_play, on_ranking):
    page.bgcolor = ft.Colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # --- Cabecera ---
    header = ft.Column(
        [
            ft.Icon(ft.Icons.SPORTS_ESPORTS, size=90, color=ft.Colors.PURPLE_400),
            ft.Text("ANI_TRIVIA", size=44, weight="bold", color=ft.Colors.PURPLE_200),
           ft.Text(f"👋 Bienvenido, {user['username']}!", size=22, color=ft.Colors.PINK_200, italic=True),
           ft.Text("¡Prepárate para poner a prueba tus conocimientos!", size=10, color=ft.Colors.PURPLE_100, italic=True),

        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=8,
    )

    # --- Botón estilo gamer ---
    def make_glow_button(text, icon, gradient_colors, on_click):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(icon, color=ft.Colors.WHITE, size=28),
                    ft.Text(text, size=20, color=ft.Colors.WHITE, weight="bold")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            ),
            width=260,
            height=60,
            border_radius=12,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=gradient_colors
            ),
            on_click=on_click,
        )

    # --- Confirmación de salida ---
    def confirm_exit(e):
        dialog = ft.AlertDialog(
            title=ft.Text("Confirmación"),
            content=ft.Text("¿Estás seguro que deseas cerrar sesión?"),
            actions=[
                ft.TextButton("No", on_click=lambda e: dialog.dismiss()),
                ft.ElevatedButton("Sí", on_click=lambda e: go_to_login())
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            modal=True
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    def go_to_login():
        page.dialog.open = False
        page.update()
        page.controls.clear()
        page.add(login_page(page, on_login=lambda user: print("Volvió al login"))) 
        page.update()

    # --- Botones principales ---
    buttons = ft.Column(
        [
            make_glow_button("🎮 JUGAR", ft.Icons.PLAY_ARROW, [ft.Colors.PURPLE_500, ft.Colors.BLUE_400], lambda e: on_play()),
            make_glow_button("🏆 RANKING", ft.Icons.LEADERBOARD, [ft.Colors.PINK_500, ft.Colors.ORANGE_400], lambda e: on_ranking()),
            make_glow_button("🚪 SALIR", ft.Icons.EXIT_TO_APP, [ft.Colors.RED_600, ft.Colors.PINK_400], confirm_exit),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=25,
    )

    # --- Contenedor central ---
    content = ft.Container(
        content=ft.Column([header, ft.Divider(height=30, thickness=2, color=ft.Colors.PURPLE_400), buttons],
                          alignment=ft.MainAxisAlignment.CENTER,
                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                          spacing=35),
        width=450,
        padding=40,
        border_radius=25,
        gradient=ft.LinearGradient(begin=ft.alignment.top_left, end=ft.alignment.bottom_right,
                                   colors=[ft.Colors.with_opacity(0.3, ft.Colors.PURPLE_700), ft.Colors.BLACK]),
        border=ft.border.all(1, ft.Colors.PURPLE_600),
        alignment=ft.alignment.center,
    )

    # --- Fondo decorativo ---
    background = ft.Stack(
        [
            ft.Container(gradient=ft.RadialGradient(center=ft.alignment.center, radius=1.3,
                                                   colors=[ft.Colors.with_opacity(0.25, ft.Colors.PINK_600), ft.Colors.BLACK]),
                         expand=True),
            ft.Image(src="https://cdn-icons-png.flaticon.com/512/2821/2821873.png", width=160, height=160, opacity=0.08, right=40, top=40),
            ft.Image(src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=200, height=200, opacity=0.08, left=60, bottom=60),
            ft.Row([content], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER, expand=True),
        ],
        expand=True,
    )

    return background
