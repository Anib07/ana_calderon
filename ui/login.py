import flet as ft
from db import check_user, register_user

def login_page(page, on_login):
    # --- Configuración general ---
    page.bgcolor = ft.Colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # --- Campos de entrada ---
    username = ft.TextField(
        label="👾 Usuario",
        prefix_icon=ft.Icons.PERSON,
        autofocus=True,
        width=320,
        border_radius=10,
        bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.PURPLE_200),
        color=ft.Colors.WHITE,
        border_color=ft.Colors.PURPLE_400,
        label_style=ft.TextStyle(color=ft.Colors.PURPLE_100),
    )

    password = ft.TextField(
        label="🔐 Contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=320,
        border_radius=10,
        bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.PURPLE_200),
        color=ft.Colors.WHITE,
        border_color=ft.Colors.PURPLE_400,
        label_style=ft.TextStyle(color=ft.Colors.PURPLE_100),
    )

    message = ft.Text("", size=16, weight="bold", color=ft.Colors.WHITE)

    # --- Funciones ---
    def login_click(e):
        user_val = username.value.strip()
        pass_val = password.value.strip()

        # Validaciones
        if not user_val or not pass_val:
            message.value = "⚠️ Todos los campos son obligatorios"
            message.color = ft.Colors.ORANGE_400
            page.update()
            return
        if len(user_val) < 3:
            message.value = "⚠️ El usuario debe tener al menos 3 caracteres"
            message.color = ft.Colors.ORANGE_400
            page.update()
            return
        if len(pass_val) < 6:
            message.value = "⚠️ La contraseña debe tener al menos 6 caracteres"
            message.color = ft.Colors.ORANGE_400
            page.update()
            return

        # Verificación en la base de datos
        user = check_user(user_val, pass_val)
        if user:
            on_login(user)
        else:
            message.value = "❌ Usuario o contraseña incorrectos"
            message.color = ft.Colors.RED_400
            page.update()

    def register_click(e):
        user_val = username.value.strip()
        pass_val = password.value.strip()

        # Validaciones
        if not user_val or not pass_val:
            message.value = "⚠️ Todos los campos son obligatorios"
            message.color = ft.Colors.ORANGE_400
            page.update()
            return
        if len(user_val) < 3:
            message.value = "⚠️ El usuario debe tener al menos 3 caracteres"
            message.color = ft.Colors.ORANGE_400
            page.update()
            return
        if len(pass_val) < 6:
            message.value = "⚠️ La contraseña debe tener al menos 6 caracteres"
            message.color = ft.Colors.ORANGE_400
            page.update()
            return

        # Registro en la base de datos
        if register_user(user_val, pass_val):
            message.value = "✅ Usuario registrado con éxito"
            message.color = ft.Colors.GREEN_400
        else:
            message.value = "⚠️ El usuario ya existe"
            message.color = ft.Colors.RED_400
        page.update()

    # --- Elementos visuales ---
    logo = ft.Icon(name=ft.Icons.SPORTS_ESPORTS, size=90, color=ft.Colors.PURPLE_400)
    title = ft.Text("ANI_TRIVIA", size=40, weight="bold", color=ft.Colors.PURPLE_300)
    subtitle = ft.Text("⚡️ Desafía tu mente ⚡️", size=18, italic=True, color=ft.Colors.PINK_200)

    login_btn = ft.ElevatedButton(
        "INICIAR SESIÓN",
        icon=ft.Icons.PLAY_ARROW,
        on_click=login_click,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.PURPLE_600,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
        width=150,
        height=50,
    )

    register_btn = ft.ElevatedButton(
        "REGISTRAR",
        icon=ft.Icons.APP_REGISTRATION,
        on_click=register_click,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.PINK_500,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
        width=150,
        height=50,
    )

    # --- Tarjeta central ---
    login_card = ft.Container(
        content=ft.Column(
            [
                logo,
                title,
                subtitle,
                ft.Divider(height=15, thickness=2, color=ft.Colors.PURPLE_400),
                username,
                password,
                ft.Row([login_btn, register_btn], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                message,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
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

    # --- Fondo con decoración ---
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
                [login_card],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),
        ],
        expand=True,
    )

    return background
