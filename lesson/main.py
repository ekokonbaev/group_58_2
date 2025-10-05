import flet as ft 


def main(page: ft.Page):
    page.title = 'Моё первое приложение'

    greeting_text = ft.Text("Hello world")

    page.add(greeting_text)


ft.app(target=main)