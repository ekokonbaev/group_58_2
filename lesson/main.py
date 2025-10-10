import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text("Hello world")

    history = []
    history_text = ft.Text('История сообщений: ')

    def on_button_click(_):
        name = name_input.value.strip()
        print(name)

        if name:
            greeting_text.value = f"Hello {name}"
            name_input.value = ""
            history.append(f"{name} вошёл в чат в {datetime.now().strftime('%H:%M:%S')}")
            timestamp = datetime.now().strftime('%H:%M:%S')
            history_text.value = 'История сообщений:     ' + '\n'.join(history)
        else:
            print("Please enter your name")
        page.update()

    name_input = ft.TextField(label="Ваше имя: ", on_submit=on_button_click)
    name_button = ft.ElevatedButton(text="SEND", icon=ft.Icons.SEND, on_click=on_button_click)

    page.add(greeting_text, name_input, name_button, history_text)


ft.app(target=main)
