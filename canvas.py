from tkinter import Tk, Canvas

def create_root():
    root = Tk()

    root.geometry("700x600")
    root.title("CraftyResinCoupleShop")
    root.resizable(False, False)

    return root

def create_frame():
    frame = Canvas(root, width=700, height=600, bg="#f7f1da")
    frame.grid(row=0, column=0)

    return frame

root = create_root()
frame = create_frame()