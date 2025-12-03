import flet as ft

def manual_page(page, on_back_home):
    page.bgcolor = ft.Colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Cabecera
    header = ft.Column(
        [
            ft.Icon(ft.Icons.MENU_BOOK, size=80, color=ft.Colors.TEAL_400),
            ft.Text("MANUAL DE USUARIO", size=44, weight="bold", color=ft.Colors.CYAN_200),
            ft.Text(
                "Aprende a usar la aplicación y cómo jugar tus partidas.",
                size=18,
                color=ft.Colors.CYAN_100,
                italic=True
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )

    # Contenido
    content_text = ft.Column(
        [
            ft.Text("1️⃣ Presiona '🎮 JUGAR' para iniciar una partida.", size=16, color=ft.Colors.WHITE),
            ft.Text("2️⃣ Elige la categoría y la dificultad.", size=16, color=ft.Colors.WHITE),
            ft.Text("3️⃣ Responde las preguntas. Cada acierto suma puntos. ", size=16, color=ft.Colors.WHITE),
            ft.Text("Y cada Dificultad tiene una serie de tiempo y cantidad de pregutas diferentes", size=16, color=ft.Colors.WHITE),
            ft.Text("4️⃣ Al finalizar verás tu puntaje.", size=16, color=ft.Colors.WHITE),
            ft.Text("5️⃣ Consulta '🏆 RANKING' para ver tu posición.", size=16, color=ft.Colors.WHITE),
            ft.Text("6️⃣ Para salir presiona '🚪 CERRAR SESIÓN'.", size=16, color=ft.Colors.WHITE),
        ],
        spacing=12,
    )

    # Botón estilo gamer
    def make_glow_button(text, icon, gradient_colors, on_click):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(icon, color=ft.Colors.WHITE, size=28),
                    ft.Text(text, size=20, color=ft.Colors.WHITE, weight="bold"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            width=260,
            height=60,
            border_radius=12,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=gradient_colors,
            ),
            on_click=on_click,
        )

    # Botones
    back_button = make_glow_button(
        "⬅️ Volver",
        ft.Icons.ARROW_BACK,
        [ft.Colors.TEAL_500, ft.Colors.CYAN_400],
        lambda e: on_back_home()
    )

    # Botón para abrir video en el navegador
    video_button = make_glow_button(
        "▶️ Ver video explicativo",
        ft.Icons.PLAY_CIRCLE_FILL,
        [ft.Colors.PURPLE_500, ft.Colors.BLUE_400],
        lambda e: page.launch_url("/videoexplicativo.mp4")  # abre el video en nueva pestaña
    )

    # Contenedor central
    content = ft.Column(
        [
            header,
            ft.Divider(height=25, thickness=2, color=ft.Colors.CYAN_400),
            content_text,
            ft.Divider(height=25, thickness=2, color=ft.Colors.CYAN_400),
            back_button,
            ft.Container(height=10),
            video_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )

    # Fondo decorativo
    background = ft.Column(
        [
            ft.Stack(
                [
                    ft.Container(
                        gradient=ft.RadialGradient(
                            center=ft.alignment.center,
                            radius=1.3,
                            colors=[ft.Colors.with_opacity(0.25, ft.Colors.CYAN_600), ft.Colors.BLACK]
                        ),
                        expand=True,
                    ),
                    ft.Image(
                        src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
                        width=200,
                        height=200,
                        opacity=0.08,
                        left=60,
                        bottom=60,
                    ),
                    ft.Column(
                        [content],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        expand=True,
                    ),
                ],
                expand=True,
            )
        ],
        scroll="always",
        expand=True
    )

    return background
