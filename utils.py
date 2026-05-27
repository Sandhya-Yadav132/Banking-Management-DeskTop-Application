from tkinter import *


def add_hover_effect(button):

    def on_enter(e):

        button.config(
            bd=3,
            relief="raised"
        )


    def on_leave(e):

        button.config(
            bd=0,
            relief="solid"
        )


    button.bind("<Enter>", on_enter)

    button.bind("<Leave>", on_leave)