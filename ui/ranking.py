import flet as ft
from db import get_connection

def ranking_page(page, user=None, on_back_home=None):

    # --- Obtener ranking ---
    conn = get_connection()
    ranking = []
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT u.username, s.score, s.category, s.difficulty
            FROM scores s
            JOIN users u ON s.user_id = u.id
            ORDER BY s.score DESC
            LIMIT 10
        """)
        ranking = cursor.fetchall()
        cursor.close()
        conn.close()

    if not ranking:
        return ft.Text("No hay resultados aún.", size=20, color=ft.Colors.AMBER_200)

    # --- Función para medalla ---
    def get_medal(index):
        if index == 0:
            return "🥇"
        elif index == 1:
            return "🥈"
        elif index == 2:
            return "🥉"
        return f"{index+1}°"

    # --- Crear filas ---
    rows = []
    for i, r in enumerate(ranking):
        medal = get_medal(i)
        color = (
            ft.Colors.YELLOW_300 if i == 0 else
            ft.Colors.GREY_300 if i == 1 else
            ft.Colors.AMBER_300 if i == 2 else
            ft.Colors.WHITE
        )
        rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(medal, size=20, weight="bold", color=color)),
                    ft.DataCell(ft.Text(r['username'], color=color)),
                    ft.DataCell(ft.Text(str(r['score']), color=color)),
                    ft.DataCell(ft.Text(r['category'], color=color)),
                    ft.DataCell(ft.Text(r['difficulty'], color=color)),
                ]
            )
        )

    # --- Tabla de ranking ---
    ranking_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("#", color=ft.Colors.PURPLE_300, weight="bold")),
            ft.DataColumn(ft.Text("Usuario", color=ft.Colors.PURPLE_300, weight="bold")),
            ft.DataColumn(ft.Text("Puntos", color=ft.Colors.PURPLE_300, weight="bold")),
            ft.DataColumn(ft.Text("Cat.", color=ft.Colors.PURPLE_300, weight="bold")),
            ft.DataColumn(ft.Text("Dif.", color=ft.Colors.PURPLE_300, weight="bold")),
        ],
        rows=rows,
        heading_row_color=ft.Colors.with_opacity(0.3, ft.Colors.PURPLE_900),
        data_row_color={"hovered": ft.Colors.with_opacity(0.1, ft.Colors.PURPLE_700)},
        column_spacing=15,
        border_radius=10,
    )

    # --- Card central ---
    card_width = min(650, page.width * 0.9)
    ranking_card = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "🏆 TOP 10 MEJORES JUGADORES 🏆",
                    size=26,
                    weight="bold",
                    color=ft.Colors.YELLOW_300,
                    text_align=ft.TextAlign.CENTER,
                ),
                ranking_table,
                ft.ElevatedButton(
                    "Volver",
                    on_click=lambda e: on_back_home() if on_back_home else None,
                    width=160,
                    height=45,
                )
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=30,
        width=card_width,
        border_radius=25,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.Colors.with_opacity(0.3, ft.Colors.PURPLE_900), ft.Colors.BLACK]
        ),
        border=ft.border.all(2, ft.Colors.PURPLE_600),
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=25, color=ft.Colors.PURPLE_800, offset=ft.Offset(0, 0))
    )

    # --- Fondo y layout responsive ---
    layout = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Stack(
            [
                # Fondo degradado
                ft.Container(
                    expand=True,
                    gradient=ft.RadialGradient(
                        center=ft.alignment.center,
                        radius=1.2,
                        colors=[ft.Colors.with_opacity(0.15, ft.Colors.PINK_600), ft.Colors.BLACK]
                    )
                ),
                # Card centrado con scroll
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        [ranking_card],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        scroll=ft.ScrollMode.AUTO
                    )
                )
            ],
            expand=True
        )
    )

    return layout
