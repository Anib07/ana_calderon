import flet as ft
from functools import partial

def category_page(page, on_start_game, on_back_home):
    categories = ["Historia", "Ciencia", "Informática", "Deportes"]
    difficulties = ["Fácil", "Medio", "Difícil"]

    selected_category = ft.Ref[str]()
    selected_difficulty = ft.Ref[str]()

    message = ft.Text("", color=ft.Colors.RED_400, size=16, weight="bold", text_align=ft.TextAlign.CENTER)
    small_screen = page.width < 500

    category_btn_refs = []
    difficulty_btn_refs = []

    def update_message():
        if selected_category.current and selected_difficulty.current:
            message.value = f"✅ {selected_category.current} - {selected_difficulty.current}"
            message.color = ft.Colors.LIME_300
        else:
            message.value = ""
        page.update()

    def select_category(cat, e=None):
        selected_category.current = cat
        for btn, c in zip(category_btn_refs, categories):
            btn.style.bgcolor = ft.Colors.LIME_500 if c == cat else ft.Colors.PURPLE_900
        update_message()
        page.update()

    def select_difficulty(diff, e=None):
        selected_difficulty.current = diff
        for btn, d in zip(difficulty_btn_refs, difficulties):
            btn.style.bgcolor = ft.Colors.ORANGE_400 if d == diff else ft.Colors.PINK_900
        update_message()
        page.update()

    def start_game_click(e):
        if selected_category.current and selected_difficulty.current:
            on_start_game(selected_category.current, selected_difficulty.current)
        else:
            message.value = "⚠️ Selecciona categoría y dificultad"
            message.color = ft.Colors.RED_400
            page.update()

    # --- Botones con estilo gamer ---
    category_buttons = ft.Row(
        [ft.ElevatedButton(
            c,
            on_click=partial(select_category, c),
            width=140 if small_screen else 160,
            height=50 if small_screen else 60,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.PURPLE_900,
                color=ft.Colors.WHITE,
                overlay_color=ft.Colors.LIME_400,
                shape=ft.RoundedRectangleBorder(radius=25),
                elevation=8
            )
        ) for c in categories],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15,
        wrap=True
    )
    category_btn_refs.extend(category_buttons.controls)

    difficulty_buttons = ft.Row(
        [ft.ElevatedButton(
            d,
            on_click=partial(select_difficulty, d),
            width=120 if small_screen else 140,
            height=45 if small_screen else 50,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.PINK_900,
                color=ft.Colors.WHITE,
                overlay_color=ft.Colors.ORANGE_400,
                shape=ft.RoundedRectangleBorder(radius=20),
                elevation=7
            )
        ) for d in difficulties],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15
    )
    difficulty_btn_refs.extend(difficulty_buttons.controls)

    start_button = ft.ElevatedButton(
        "🎮 COMENZAR",
        on_click=start_game_click,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.AMBER_800,
            color=ft.Colors.BLACK,
            overlay_color=ft.Colors.AMBER_500,
            shape=ft.RoundedRectangleBorder(radius=25),
            elevation=10
        )
    )

    back_button = ft.ElevatedButton(
        "⬅️ Volver",
        on_click=lambda e: on_back_home(),
        width=160,
        height=50,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREY_800,
            color=ft.Colors.WHITE,
            overlay_color=ft.Colors.GREY_500,
            shape=ft.RoundedRectangleBorder(radius=25),
            elevation=7
        )
    )

    # --- Tarjeta central estilo gamer ---
    card = ft.Container(
        content=ft.Column(
            [
                ft.Icon(ft.Icons.GAMES, size=90, color=ft.Colors.PURPLE_400),
                ft.Text("Selecciona categoría y dificultad",
                        size=28,
                        weight="bold",
                        color=ft.Colors.PURPLE_200,
                        text_align=ft.TextAlign.CENTER),
                ft.Divider(height=10, thickness=2, color=ft.Colors.PURPLE_500),
                ft.Container(category_buttons, padding=ft.padding.all(10), border_radius=20,
                             bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.PURPLE_900)),
                ft.Container(difficulty_buttons, padding=ft.padding.all(10), border_radius=20,
                             bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.PINK_900)),
                ft.Row([start_button, back_button], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                message
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        width=small_screen and page.width - 40 or 650,
        padding=ft.padding.all(40),
        border_radius=30,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.Colors.with_opacity(0.3, ft.Colors.PURPLE_900), ft.Colors.BLACK]
        ),
        border=ft.border.all(2, ft.Colors.PURPLE_500),
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=25, color=ft.Colors.PURPLE_800, offset=ft.Offset(0, 0))
    )

    # --- Fondo gamer ---
    layout = ft.Stack(
        [
            ft.Container(
                expand=True,
                gradient=ft.RadialGradient(
                    center=ft.alignment.center,
                    radius=1.2,
                    colors=[ft.Colors.with_opacity(0.15, ft.Colors.PINK_600), ft.Colors.BLACK]
                ),
            ),
            ft.Image(src="https://cdn-icons-png.flaticon.com/512/2821/2821873.png",
                     width=160, height=160, opacity=0.07, right=40, top=40),
            ft.Image(src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
                     width=200, height=200, opacity=0.07, left=60, bottom=60),
            ft.Row([card], alignment=ft.MainAxisAlignment.CENTER,
                   vertical_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
        ],
        expand=True
    )

    return layout
