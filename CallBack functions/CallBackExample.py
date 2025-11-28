def on_button_click(callback)->None:
    print("Button clicked")
    callback()

def show_msg()->None:
    print(f"Hello, yuvha")

on_button_click(show_msg)