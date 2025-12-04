import flet as ft
import threading
import time
import random
from db import get_connection

def game_page(page, user, category, difficulty, on_game_end):
    page.title = f"Trivia - {category} ({difficulty})"
    page.bgcolor = ft.Colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- Configuración por nivel ---
    config = {
        "Fácil": {"preguntas": 10, "tiempo": 15},
        "Medio": {"preguntas": 15, "tiempo": 10},
        "Difícil": {"preguntas": 20, "tiempo": 7},
    }
    total_questions = config.get(difficulty, {"preguntas": 10, "tiempo": 15})["preguntas"]
    question_time = config.get(difficulty, {"preguntas": 10, "tiempo": 15})["tiempo"]

    # --- Estado del juego ---
    questions_answered = 0
    correct_answers = 0
    wrong_answers = 0
    score = 0
    stop_timer = False

    # --- Elementos visuales ---
    question_text = ft.Text("", size=24, color=ft.Colors.WHITE, weight="bold", text_align=ft.TextAlign.CENTER)
    message = ft.Text("", size=18, color=ft.Colors.AMBER_200, text_align=ft.TextAlign.CENTER)
    timer_label = ft.Text("", size=16, color=ft.Colors.RED_400)
    timer_bar = ft.ProgressBar(width=250, value=1.0, color=ft.Colors.GREEN_400)
    options_container = ft.Column(spacing=12, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # --- Cargar preguntas desde SQLite ---
    preguntas = []
    conn = get_connection()
    conn.row_factory = lambda cursor, row: {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM questions WHERE category=? AND difficulty=?",
        (category, difficulty)
    )
    rows = cursor.fetchall()
    for row in rows:
        opciones = [row["option1"], row["option2"], row["option3"], row["option4"]]
        preguntas.append({
            "q": row["question"],
            "options": opciones,
            "a": opciones[row["correct_option"] - 1]
        })
    cursor.close()
    conn.close()

    if not preguntas:
        message.value = "No hay preguntas disponibles para esta categoría y dificultad."
        page.add(message)
        page.update()
        return

    random.shuffle(preguntas)
    if len(preguntas) < total_questions:
        total_questions = len(preguntas)
    preguntas = preguntas[:total_questions]

    # --- Temporizador ---
    def start_timer():
        nonlocal stop_timer

        def timer_loop():
            nonlocal stop_timer
            remaining = question_time
            while remaining > 0 and not stop_timer:
                timer_label.value = f"Tiempo: {remaining}s"
                timer_bar.value = remaining / question_time
                page.update()
                time.sleep(1)
                remaining -= 1

            if not stop_timer:
                handle_answer(None, None)

        threading.Thread(target=timer_loop, daemon=True).start()

    # --- Manejo de respuesta ---
    def handle_answer(btn, selected_option):
        nonlocal questions_answered, correct_answers, wrong_answers, score, stop_timer

        stop_timer = True
        q = preguntas[questions_answered]
        correct = (selected_option == q["a"])

        # Destacar botón seleccionado
        if btn:
            btn.style = ft.ButtonStyle(
                bgcolor=ft.Colors.AMBER_400 if correct else ft.Colors.RED_400,
                color=ft.Colors.BLACK,
                shape=ft.RoundedRectangleBorder(radius=12),
                elevation=6,
            )

        # Mensaje de resultado
        if correct:
            message.value = "✅ ¡Correcto!"
            message.color = ft.Colors.GREEN_400
            correct_answers += 1
            score += 10
        else:
            if selected_option is None:
                message.value = f"⏰ Tiempo agotado. Respuesta: {q['a']}"
            else:
                message.value = f"❌ Incorrecto. Respuesta: {q['a']}"
            message.color = ft.Colors.RED_400
            wrong_answers += 1

        page.update()
        questions_answered += 1

        # Siguiente pregunta después de 1.5s
        def delayed_next():
            time.sleep(1.5)
            show_question()

        threading.Thread(target=delayed_next, daemon=True).start()

    # --- Mostrar siguiente pregunta ---
    def show_question():
        nonlocal questions_answered, stop_timer

        if questions_answered >= total_questions:
            on_game_end(score, category, difficulty, correct_answers, wrong_answers)
            return

        q = preguntas[questions_answered]
        question_text.value = q["q"]
        message.value = ""
        options_container.controls.clear()

        for opt in q["options"]:
            btn = ft.ElevatedButton(
                opt,
                width=200,
                height=45,
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.BLUE_700,
                    color=ft.Colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=12),
                    elevation=4,
                )
            )
            btn.on_click = lambda e, b=btn, o=opt: handle_answer(b, o)
            options_container.controls.append(btn)

        page.update()
        stop_timer = False
        start_timer()

    # --- Botón de terminar juego ---
    def finish_game_click(e):
        nonlocal stop_timer
        stop_timer = True
        on_game_end(score, category, difficulty, correct_answers, wrong_answers)

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
        on_click=finish_game_click
    )

    # --- Layout principal ---
    card = ft.Container(
        content=ft.Column(
            [
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
            ft.Row([card], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
        ],
        expand=True
    )

    page.controls.clear()
    page.add(layout)
    show_question()
