import flet as ft

def result_page(page, user, score, category, difficulty, correct, wrong, on_play_again, on_back_home):
    page.controls.clear()
    page.bgcolor = ft.Colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # --- Icono y título ---
    trophy_icon = ft.Icon(
        ft.Icons.STAR,  # Ícono compatible
        size=90,
        color=ft.Colors.YELLOW_400
    )

    title = ft.Text(
        "🏆RESULTADOS🏆",
        size=36,
        weight="bold",
        color=ft.Colors.YELLOW_300
    )

    subtitle = ft.Text(
        f"Usuario: {user}",
        size=20,
        color=ft.Colors.WHITE
    )

    details = ft.Text(
        f"Categoría: {category} - Nivel: {difficulty}\nCorrectas: {correct} | Incorrectas: {wrong} | Puntuación: {score}",
        size=20,
        color=ft.Colors.GREEN_400,
        text_align=ft.TextAlign.CENTER
    )

    # --- Botones ---
    play_again_btn = ft.ElevatedButton(
        "Jugar otra vez",
        width=150,
        height=50,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.PURPLE_600,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=12)
        ),
        on_click=lambda e: on_play_again()
    )

    back_home_btn = ft.ElevatedButton(
        "Volver al inicio",
        width=150,
        height=50,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.PINK_500,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=12)
        ),
        on_click=lambda e: on_back_home()
    )

    buttons_row = ft.Row(
        [play_again_btn, back_home_btn],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # --- Tarjeta central ---
    result_card = ft.Container(
        content=ft.Column(
            [
                trophy_icon,
                title,
                subtitle,
                details,
                buttons_row
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        width=420,
        padding=40,
        border_radius=25,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.Colors.with_opacity(0.3, ft.Colors.PURPLE_700), ft.Colors.BLACK],
        ),
        border=ft.border.all(1, ft.Colors.PURPLE_600),
        alignment=ft.alignment.center,
    )

    # --- Fondo decorativo ---
    background = ft.Stack(
        [
            ft.Container(
                gradient=ft.RadialGradient(
                    center=ft.alignment.center,
                    radius=1.2,
                    colors=[ft.Colors.with_opacity(0.25, ft.Colors.PINK_600), ft.Colors.BLACK],
                ),
                expand=True,
            ),
            # Iconos decorativos
            ft.Image(
                src="https://cdn-icons-png.flaticon.com/512/2821/2821873.png",
                width=140,
                height=140,
                opacity=0.08,
                right=40,
                top=40,
            ),
            ft.Image(
                src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
                width=180,
                height=180,
                opacity=0.08,
                left=60,
                bottom=60,
            ),
            ft.Row(
                [result_card],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            )
        ],
        expand=True
    )

    page.add(background)
