from tkinter import Tk

def create_root():
    root = Tk()

    root.geometry("700x600")
    root.title("CraftyResinCoupleShop")
    root.resizable(False, False)

    return root

root = create_root()