from tkinter import *

root = Tk()

root.title("Banking Management System Desktop Application")
root.geometry("500x300")

label = Label(root, text="Hello!,Welcome in my App")
label.pack()

def hello():
    print("Button Clicked")


button = Button(root, text="Click Me", command=hello)
button.pack()

root.mainloop()