from tkinter import Button

from canvas import root, frame


def entry_render():
    register_button = Button(
        root,
        text="Register",
        bg="#7a6a3a",
        fg="black",
        width="20",
        height="3",
        borderwidth=0

    )

    login_button = Button(
        root,
        text="Login",
        bg="#635014",
        fg="black",
        width="20",
        height="3",
        borderwidth=0
    )

    frame.create_window(350, 320, window=register_button)
    frame.create_window(350,260, window=login_button)

