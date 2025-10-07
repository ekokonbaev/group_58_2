import flet as ft 


def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.SYSTEM
    greeting_text = ft.Text("Hello world")
    name_input = ft.TextField(label="Ваше имя: ")

    page.add(greeting_text)


ft.app(target=main)