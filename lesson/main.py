import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Hello world")
    history = []
    history_text = ft.Text('История сообщений: ')
    message_text = ft.Text("", color=ft.Colors.RED)

    def on_button_click(_):
        name = name_input.value.strip()
        if name:
            greeting_text.value = f"Hello {name}"
            name_input.value = ""
            timestamp = datetime.now().strftime('%H:%M:%S')
            history.append(f"{name} вошёл в чат в {timestamp}")
            history_text.value = 'История сообщений:\n' + '\n'.join(history)
            message_text.value = ""
        else:
            message_text.value = "Пожалуйста, введите имя!"
        page.update()

    def delete_last(_):
        if history:
            history.pop()  
            history_text.value = 'История сообщений:\n' + '\n'.join(history)
            message_text.value = "Последнее приветствие удалено!"
        else:
            message_text.value = "История пуста!"
        page.update()


    name_input = ft.TextField(label="Ваше имя: ", on_submit=on_button_click)
    send_button = ft.ElevatedButton(text="Отправить", icon=ft.Icons.SEND, on_click=on_button_click)
    delete_button = ft.ElevatedButton(text="Удалить последнее", icon=ft.Icons.DELETE, on_click=delete_last)


    page.add(
        greeting_text,
        name_input,
        ft.Row([send_button, delete_button], spacing=10),
        history_text,
        message_text
    )

ft.app(target=main)
