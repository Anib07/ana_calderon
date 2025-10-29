import flet as ft
import random

def game_page(page, user, category, difficulty, on_game_end, on_back_home=None):
    page.title = f"Trivia - {category} ({difficulty})"
    page.bgcolor = ft.Colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- Configuración (solo visual) ---
    config = {
        "Fácil": {"preguntas": 10, "tiempo": 15},
        "Medio": {"preguntas": 15, "tiempo": 10},
        "Difícil": {"preguntas": 20, "tiempo": 7},
    }
    total_questions = config.get(difficulty, {"preguntas": 10})["preguntas"]

    # --- Elementos visuales ---
    question_text = ft.Text(
        "¿Qué lenguaje se usa para crear páginas web?", 
        size=24, color=ft.Colors.WHITE, weight="bold", 
        text_align=ft.TextAlign.CENTER
    )
    message = ft.Text(
        "Selecciona la opción correcta...", 
        size=18, color=ft.Colors.AMBER_200, 
        text_align=ft.TextAlign.CENTER
    )
    timer_label = ft.Text("Tiempo: 15s", size=16, color=ft.Colors.RED_400)
    timer_bar = ft.ProgressBar(width=250, value=1.0, color=ft.Colors.GREEN_400)

    # --- Opciones falsas (solo para mostrar) ---
    opciones_demo = ["Python", "HTML", "C++", "Java"]
    options_container = ft.Column(
        spacing=12, horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    for opt in opciones_demo:
        btn = ft.ElevatedButton(
            opt,
            width=200,
            height=45,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.BLUE_700,
                color=ft.Colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=12),
                elevation=4,
            ),
            on_click=None  # 🔒 desactivado
        )
        options_container.controls.append(btn)

    # --- Botón de terminar (solo visual) ---
    finish_button = ft.ElevatedButton(
        "🏁 Terminar juego",
        width=150,
        height=40,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.RED_600,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=12),
            elevation=4,
        ),
        on_click=None  # 🔒 desactivado
    )

    # --- Botón volver al menú ---
    back_button = ft.ElevatedButton(
        "Volver al menú",
        width=180,
        height=45,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.PURPLE_700,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=12),
            overlay_color=ft.Colors.with_opacity(0.2, ft.Colors.WHITE),
            elevation=6,
        ),
        on_click=lambda e: on_back_home() if on_back_home else None
    )

    # --- Layout principal ---
    card = ft.Container(
        content=ft.Column(
            [
                back_button,
                finish_button,
                ft.Text(f"{category} - Nivel {difficulty}", size=20, color=ft.Colors.PURPLE_300),
                question_text,
                timer_label,
                timer_bar,
                options_container,
                message,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        padding=25,
        width=min(400, page.width-20),
        border_radius=25,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.Colors.with_opacity(0.3, ft.Colors.PURPLE_900), ft.Colors.BLACK],
        ),
        border=ft.border.all(2, ft.Colors.PURPLE_500),
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=20, color=ft.Colors.PURPLE_800, offset=ft.Offset(0, 0))
    )

    layout = ft.Stack(
        [
            ft.Container(
                expand=True,
                gradient=ft.RadialGradient(
                    center=ft.alignment.center,
                    radius=1.5,
                    colors=[ft.Colors.with_opacity(0.2, ft.Colors.PINK_600), ft.Colors.BLACK],
                ),
            ),
            ft.Row([card], alignment=ft.MainAxisAlignment.CENTER, 
                   vertical_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
        ],
        expand=True
    )

    page.controls.clear()
    page.add(layout)
