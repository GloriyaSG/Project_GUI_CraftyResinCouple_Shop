from tkinter import Button, Entry
from canvas import root, frame
from helpers import screen_cleaner
from json import loads


def entry_render():
    register_button = Button(
        root,
        text="Register",
        bg="#635014",
        fg="black",
        width="20",
        height="3",
        borderwidth=0,
        command=register,

    )

    login_button = Button(
        root,
        text="Login",
        bg="#7a6a3a",
        fg="black",
        width="20",
        height="3",
        borderwidth=0
    )

    frame.create_window(350, 320, window=register_button)
    frame.create_window(350,260, window=login_button)

def client_login():

    info_data = []

    with open("data_base/users_info.txt","r") as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data

def register():
    screen_cleaner()

    frame.create_text(100,50, text="First Name:")
    frame.create_text(100,100, text="Last Name:")
    frame.create_text(100,150, text="Username:")
    frame.create_text(100,200, text="Password:")
    frame.create_text(100,250, text="Confirm Password:")

    frame.create_window(220,50, window=first_name_box)
    frame.create_window(220,100, window=last_name_box)
    frame.create_window(220,150, window=username_box)
    frame.create_window(220,200, window=password_box)
    frame.create_window(220,250, window=confirm_password_box)

    register_button = Button(
        root,
        text="Register",
        bg="#635014",
        fg="black",
        width="15",
        height="3",
        borderwidth=0,
        command=registration,

    )

    frame.create_window(220,300, window=register_button)



first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show="*")
confirm_password_box = Entry(root, bd=0, show="*")


def registration():

    users_dict = {
        "First Name": first_name_box.get(),
        "Last Name": last_name_box.get(),
        "Username": username_box.get(),
        "Password": password_box.get(),
        "Confirm Password": confirm_password_box.get()

    }

    if check_registration(users_dict):
        pass


def check_registration(info):
    frame.delete("error")
    for key, value in info.items():
        if not value.strip():
            frame.create_text(
                220,
                350,
                text=f"{key} cannot be empty!",
                fill="red",
                tags="error",

            )
            return False

    info_data = client_login()

    print(info_data)

