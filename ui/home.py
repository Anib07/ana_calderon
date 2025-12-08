import flet as ft
from ui.login import login_page

def home_page(page, user, on_play, on_ranking, on_manual):
    page.bgcolor = ft.Colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # --- CABECERA ---
    header = ft.Column(
        [
            ft.Icon(ft.Icons.SPORTS_ESPORTS, size=70 if page.width < 500 else 90, color=ft.Colors.PURPLE_400),
            ft.Text("ANI_TRIVIA", size=32 if page.width < 500 else 44, weight="bold", color=ft.Colors.PURPLE_200),
            ft.Text(f"👋 Bienvenido, {user['username']}!",
                    size=18 if page.width < 500 else 22,
                    color=ft.Colors.PINK_200,
                    italic=True,
                    text_align=ft.TextAlign.CENTER),
            ft.Text("¡Prepárate para poner a prueba tus conocimientos!",
                    size=11 if page.width < 500 else 13,
                    color=ft.Colors.PURPLE_100,
                    italic=True,
                    text_align=ft.TextAlign.CENTER),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=6,
    )

    # --- FUNCIONES DE DIÁLOGO ---
    def dismiss_dialog(d):
        d.open = False
        page.update()

    def go_to_login(dialog):
        dialog.open = False
        page.controls.clear()
        page.add(login_page(page, on_login=lambda user: home_page(page, user, on_play, on_ranking, on_manual)))
        page.update()

    def show_logout_dialog(e):
        dialog = ft.AlertDialog(
            title=ft.Text("Confirmación"),
            content=ft.Text("¿Estás seguro que deseas cerrar sesión?"),
            actions=[
                ft.TextButton("No", on_click=lambda e: dismiss_dialog(dialog)),
                ft.ElevatedButton("Sí", on_click=lambda e: go_to_login(dialog)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            modal=True,
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    # --- BOTÓN GLOW ---
    def make_glow_button(text, icon, gradient_colors, on_click):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(icon, color=ft.Colors.WHITE, size=22),
                    ft.Text(
                        text,
                        size=15 if page.width < 500 else 17,
                        color=ft.Colors.WHITE,
                        weight="bold",
                        text_align=ft.TextAlign.CENTER,
                        expand=True,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=8,
            ),
            width=page.width * 0.85 if page.width < 500 else 320,
            padding=12,
            border_radius=14,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=gradient_colors,
            ),
            on_click=on_click,
        )

    # --- BOTONES PRINCIPALES ---
    buttons = ft.Column(
        [
            make_glow_button("🎮 JUGAR", ft.Icons.PLAY_ARROW,
                             [ft.Colors.PURPLE_500, ft.Colors.BLUE_400], lambda e: on_play()),
            make_glow_button("🏆 RANKING", ft.Icons.LEADERBOARD,
                             [ft.Colors.PINK_500, ft.Colors.ORANGE_400], lambda e: on_ranking()),
            make_glow_button("📘 MANUAL DE USUARIO", ft.Icons.MENU_BOOK,
                             [ft.Colors.TEAL_500, ft.Colors.CYAN_400], lambda e: on_manual()),
            make_glow_button("🚪 CERRAR SESIÓN", ft.Icons.EXIT_TO_APP,
                             [ft.Colors.RED_600, ft.Colors.PINK_400], show_logout_dialog),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=22,
    )

    # --- CONTENEDOR CENTRAL ---
    content = ft.Container(
        content=ft.Column(
            [
                header,
                ft.Divider(height=22, thickness=2, color=ft.Colors.PURPLE_400),
                buttons,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=26,
        ),
        padding=25,
        border_radius=25,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.Colors.with_opacity(0.35, ft.Colors.PURPLE_700),
                    ft.Colors.with_opacity(0.9, ft.Colors.BLACK)],
        ),
        border=ft.border.all(1, ft.Colors.PURPLE_600),
        alignment=ft.alignment.center,
        width=page.width * 0.9 if page.width < 500 else 360,
    )

    # --- FONDO RESPONSIVE ---
    background = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Stack(
            controls=[
                # Fondo degradado
                ft.Container(
                    expand=True,
                    gradient=ft.RadialGradient(
                        center=ft.alignment.center,
                        radius=1.3,
                        colors=[ft.Colors.with_opacity(0.3, ft.Colors.PINK_600), ft.Colors.BLACK],
                    ),
                ),
                # Imagen flotante 1
                ft.Container(
                    content=ft.Image(
                        src="https://cdn-icons-png.flaticon.com/512/2821/2821873.png",
                        width=150, height=150, opacity=0.07
                    ),
                    right=40,
                    top=40,
                ),
                # Imagen flotante 2
                ft.Container(
                    content=ft.Image(
                        src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
                        width=200, height=200, opacity=0.07
                    ),
                    left=60,
                    bottom=60,
                ),
                # Contenido centrado con scroll
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        [content],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        scroll=ft.ScrollMode.AUTO,
                    ),
                ),
            ],
            expand=True,
        ),
    )

    return background
