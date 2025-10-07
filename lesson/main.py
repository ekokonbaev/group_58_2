import flet as ft 


def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text("Hello world")
    name_input = ft.TextField(label="Ваше имя: ")
    name_button = ft.ElevatedButton(text="SEND" , icon=ft.Icons.SEND)
    #name_text_button = ft.TextButton(text="Text Button")
    #name_icon_buttin = ft.IconButton(icon=ft.Icons.Send)
    page.add(greeting_text , name_input, name_button)


ft.app(target=main)