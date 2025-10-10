import flet as ft 


def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text("Hello world")

    greeting_text = []
    history_text = ft.Text('История сообщений: ')

    def on_button_click(_):
        name = name_input.value.strip()
        print(name)
        page.update()

        if name:
            greeting_text.value = f"Hello"
        else:
            print("Please enter your name")
        page.update()

    
    name_input = ft.TextField(label="Ваше имя: " , on_submit=on_button_click)

    name_button = ft.ElevatedButton(text="SEND" , icon=ft.Icons.SEND, on_click=on_button_click)
    #name_text_button = ft.TextButton(text="Text Button")
    #name_icon_buttin = ft.IconButton(icon=ft.Icons.Send)
    page.add(greeting_text , name_input, name_button, history_text)


ft.app(target=main)