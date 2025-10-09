import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Приветствие по времени"
    page.theme_mode = ft.ThemeMode.LIGHT 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    name_field = ft.TextField(label="Введите имя", width=250)
    age_field = ft.TextField(label="Введите возраст", width=250)
    result_text = ft.Text(value="", size=18, weight=ft.FontWeight.BOLD)

    def get_greeting(name):
        hour = datetime.now().hour
        if 6 <= hour < 12:
            return f"Доброе утро, {name}!"
        elif 12 <= hour < 18:
            return f"Добрый день, {name}!"
        elif 18 <= hour < 24:
            return f"Добрый вечер, {name}!"
        else:
            return f"Доброй ночи, {name}!"

    def on_submit(e):
        name = name_field.value.strip()
        age = age_field.value.strip()

        if not name:
            result_text.value = "Введите имя!"
        elif not age:
            result_text.value = "Введите возраст!"
        else:
            try:
                age_int = int(age)
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                greeting = get_greeting(name)
                result_text.value = f"{now} - {greeting} Тебе {age_int} лет."
            except ValueError:
                result_text.value = "Возраст должен быть числом!"

        page.update()

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    submit_btn = ft.ElevatedButton(text="Показать приветствие", on_click=on_submit)
    theme_btn = ft.IconButton(
        icon=ft.icons.BRIGHTNESS_7,
        tooltip="Сменить тему",
        on_click=toggle_theme
    )

    page.add(
        ft.Column(
            [
                ft.Row([theme_btn], alignment=ft.MainAxisAlignment.END),
                name_field,
                age_field,
                submit_btn,
                result_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
