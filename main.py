import flet as ft
from ui.login import login_page
from ui.home import home_page
from ui.category import category_page
from ui.game import game_page
from ui.result import result_page
from ui.ranking import ranking_page
from db import save_score

def main(page: ft.Page):
    page.title = "ANI_TRIVIA"
    page.bgcolor = ft.Colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- Pantalla de inicio / Home ---
    def show_home(user):
        page.controls.clear()

        # --- Función que se llama al terminar un juego ---
        def on_game_end(score, category, difficulty, correct, wrong):
            # Guardar puntuación en la base de datos
            save_score(user['id'], score, category, difficulty)

            # Mostrar resultados
            page.controls.clear()
            result_page(
                page,
                user=user['username'],
                score=score,
                category=category,
                difficulty=difficulty,
                correct=correct,
                wrong=wrong,
                on_play_again=lambda: start_game(category, difficulty),
                on_back_home=lambda: show_home(user)
            )
            page.update()

        # --- Función para iniciar un juego ---
        def start_game(category, difficulty):
            page.controls.clear()
            # ⚡ Pasamos go_category como on_back_home para volver a category_page
            game_page(
                page,
                user,
                category,
                difficulty,
                on_game_end,
                on_back_home=lambda: go_category()  
            )

        # --- Ir a seleccionar categoría/dificultad ---
        def go_category(e=None):
            page.controls.clear()

            # Función para volver a home
            def back_to_home():
                page.controls.clear()
                show_home(user)

            # Llamada correcta a category_page con on_back_home
            page.add(category_page(page, on_start_game=start_game, on_back_home=back_to_home))
            page.update()

        # --- Ir al ranking ---
        def go_ranking(e=None):
            page.controls.clear()
            ranking_page(page, user=user, on_back_home=lambda: show_home(user))
            page.update()

        # --- Mostrar home ---
        page.add(home_page(page, user, on_play=go_category, on_ranking=go_ranking))
        page.update()

    # --- Login ---
    def on_login_success(user):
        show_home(user)

    page.add(login_page(page, on_login=on_login_success))
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)
