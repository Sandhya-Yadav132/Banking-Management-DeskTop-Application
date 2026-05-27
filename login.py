# from tkinter import *
# from tkinter import messagebox

# from user_dashboard import open_user_dashboard
# from admin_dashboard import open_admin_dashboard
# from utils import add_hover_effect


# def open_login(bank, root):

#     login_window = Toplevel()

#     login_window.title("Login")

#     login_window.geometry("400x300")

#     login_window.configure(bg="#dbeafe")

#     # ==================================================
#     # MAIN FRAME
#     # ==================================================

#     main_frame = Frame(
#         login_window,
#         bg="#dbeafe"
#     )

#     main_frame.pack(expand=True)

#     # ==================================================
#     # TITLE
#     # ==================================================

#     title = Label(
#         main_frame,
#         text="Login Here!",
#         bg="#dbeafe",
#         fg="#1e3a8a",
#         font=("Arial", 22, "bold")
#     )

#     title.pack(pady=20)









#     # ==================================================
#     # USER ID
#     # ==================================================

#     user_label = Label(
#         main_frame,
#         text="User ID",
#         bg="#dbeafe",
#         font=("Arial", 11)
#     )

#     user_label.pack()

#     user_entry = Entry(
#         main_frame,
#         width=30,
#         font=("Arial", 11)
#     )

#     user_entry.pack(pady=5)

#     # ==================================================
#     # PASSWORD
#     # ==================================================

#     password_label = Label(
#         main_frame,
#         text="Password",
#         bg="#dbeafe",
#         font=("Arial", 11)
#     )

#     password_label.pack()

#     password_entry = Entry(
#         main_frame,
#         width=30,
#         show="*",
#         font=("Arial", 11)
#     )

#     password_entry.pack(pady=5)

#     # ==================================================
#     # LOGIN FUNCTION
#     # ==================================================

#     def login():

#         user_id = user_entry.get().strip()

#         password = password_entry.get()

#         # ---------- EMPTY FIELD VALIDATION ----------

#         if user_id == "":

#             messagebox.showerror(
#                 "Error",
#                 "User ID is Required"
#             )

#             user_entry.focus()

#             return

#         if password == "":

#             messagebox.showerror(
#                 "Error",
#                 "Password is Required"
#             )

#             password_entry.focus()

#             return

#         # ---------- USER ID VALIDATION ----------

#         if not user_id.isdigit():

#             messagebox.showerror(
#                 "Error",
#                 "Please enter valid User ID"
#             )

#             user_entry.delete(0, END)

#             user_entry.focus()

#             return

#         user_id = int(user_id)

#         # ---------- ACCOUNT CHECK ----------

#         if user_id not in bank.accounts:

#             messagebox.showerror(
#                 "Error",
#                 "Account Not Found"
#             )

#             user_entry.delete(0, END)

#             user_entry.focus()

#             return

#         acc = bank.accounts[user_id]

#         # ---------- PASSWORD CHECK ----------

#         if acc.check_password(password):

#             messagebox.showinfo(
#                 "Success",
#                 "Login Successful"
#             )

#             # ---------- CLEAR FIELDS ----------

#             user_entry.delete(0, END)

#             password_entry.delete(0, END)

#             login_window.destroy()

#             root.withdraw()

#             # ---------- OPEN DASHBOARD ----------

#             if acc.role == "admin":

#                 open_admin_dashboard(
#                     bank,
#                     acc,
#                     root
#                 )

#             else:

#                 open_user_dashboard(
#                     bank,
#                     acc,
#                     root
#                 )

#         else:

#             messagebox.showerror(
#                 "Error",
#                 "Wrong Password"
#             )

#             password_entry.delete(0, END)

#             password_entry.focus()

#     # ==================================================
#     # EXIT FUNCTION
#     # ==================================================

#     def exit_window():

#         login_window.destroy()

#         root.deiconify()

#     # ==================================================
#     # ENTER KEY NAVIGATION
#     # ==================================================

#     def move_to_password(event):

#         user_id = user_entry.get().strip()

#         # ---------- EMPTY CHECK ----------

#         if user_id == "":

#             messagebox.showerror(
#                 "Error",
#                 "User ID is Required"
#             )

#             user_entry.focus()

#             return

#         # ---------- DIGIT CHECK ----------

#         if not user_id.isdigit():

#             messagebox.showerror(
#                 "Error",
#                 "Please enter valid User ID"
#             )

#             user_entry.delete(0, END)

#             user_entry.focus()

#             return

#         user_id = int(user_id)

#         # ---------- ACCOUNT CHECK ----------

#         if user_id not in bank.accounts:

#             messagebox.showerror(
#                 "Error",
#                 "Account Not Found"
#             )

#             user_entry.delete(0, END)

#             user_entry.focus()

#             return

#         # ---------- MOVE TO PASSWORD ----------

#         password_entry.focus()

#     # ---------- ENTER KEY BINDS ----------

#     user_entry.bind(
#         "<Return>",
#         move_to_password
#     )

#     password_entry.bind(
#         "<Return>",
#         lambda event: login()
#     )

#     # ==================================================
#     # LOGIN BUTTON
#     # ==================================================

#     login_btn = Button(
#         main_frame,
#         text="Login",
#         width=20,
#         bg="#2563eb",
#         fg="white",
#         font=("Arial", 11, "bold"),
#         bd=2,
#         relief="solid",
#         cursor="hand2",
#         command=login
#     )

#     login_btn.pack(pady=20)

#     add_hover_effect(login_btn)

#     # ==================================================
#     # EXIT BUTTON
#     # ==================================================

#     exit_btn = Button(
#         main_frame,
#         text="Exit",
#         width=20,
#         bg="#dc2626",
#         fg="white",
#         font=("Arial", 11, "bold"),
#         bd=2,
#         relief="solid",
#         cursor="hand2",
#         command=exit_window
#     )

#     exit_btn.pack(pady=5)

#     add_hover_effect(exit_btn)




from tkinter import *
from tkinter import messagebox

from user_dashboard import open_user_dashboard
from admin_dashboard import open_admin_dashboard
from utils import add_hover_effect


def open_login(bank, root):

    login_window = Toplevel()

    login_window.title("Login")

    login_window.geometry("500x450")

    login_window.configure(bg="#f1f5f9")

    # login_window.resizable(False, False)

    # ==================================================
    # MAIN FRAME
    # ==================================================

    main_frame = Frame(
        login_window,
        bg="#f1f5f9"
    )

    main_frame.pack(fill="both", expand=True)


    # ==================================================
    # LOGIN CONTAINER
    # ==================================================

    container = Frame(
        main_frame,
        bg="white",
        highlightbackground="#dbeafe",
        highlightthickness=1
    )

    container.place(
        relx=0.5,
        rely=0.5,
        anchor="center",
        width=380,
        height=410
    )


    # ==================================================
    # TITLE
    # ==================================================

    title = Label(
        container,
        text="Welcome",
        bg="white",
        fg="#0f172a",
        font=("Segoe UI", 24, "bold")
    )

    title.pack(pady=(20, 5))


    # ==================================================
    # SUBTITLE
    # ==================================================

    subtitle = Label(
        container,
        text="Login to continue",
        bg="white",
        fg="#64748b",
        font=("Segoe UI", 11)
    )

    subtitle.pack()


    # ==================================================
    # BLUE LINE
    # ==================================================

    blue_line = Frame(
        container,
        bg="#2563eb",
        width=70,
        height=3
    )

    blue_line.pack(pady=15)


    # ==================================================
    # USER ID LABEL
    # ==================================================

    user_label = Label(
        container,
        text="User ID",
        bg="white",
        fg="#0f172a",
        font=("Segoe UI", 11, "bold")
    )

    user_label.pack(anchor="w", padx=60)


    # ==================================================
    # USER ID ENTRY
    # ==================================================

    user_entry = Entry(
        container,
        width=28,
        font=("Segoe UI", 12),
        relief="solid",
        bd=1
    )

    user_entry.pack(pady=(5, 15), ipady=7)


    # ==================================================
    # PASSWORD LABEL
    # ==================================================

    password_label = Label(
        container,
        text="Password",
        bg="white",
        fg="#0f172a",
        font=("Segoe UI", 11, "bold")
    )

    password_label.pack(anchor="w", padx=60)


    # ==================================================
    # PASSWORD ENTRY
    # ==================================================

    password_entry = Entry(
        container,
        width=28,
        show="*",
        font=("Segoe UI", 12),
        relief="solid",
        bd=1
    )

    password_entry.pack(pady=(5, 20), ipady=7)


    # ==================================================
    # LOGIN FUNCTION
    # ==================================================

    def login():

        user_id = user_entry.get().strip()

        password = password_entry.get()

        # ---------- EMPTY FIELD VALIDATION ----------

        if user_id == "":

            messagebox.showerror(
                "Error",
                "User ID is Required"
            )

            user_entry.focus()

            return

        if password == "":

            messagebox.showerror(
                "Error",
                "Password is Required"
            )

            password_entry.focus()

            return

        # ---------- USER ID VALIDATION ----------

        if not user_id.isdigit():

            messagebox.showerror(
                "Error",
                "Please enter valid User ID"
            )

            user_entry.delete(0, END)

            user_entry.focus()

            return

        user_id = int(user_id)

        # ---------- ACCOUNT CHECK ----------

        if user_id not in bank.accounts:

            messagebox.showerror(
                "Error",
                "Account Not Found"
            )

            user_entry.delete(0, END)

            user_entry.focus()

            return

        acc = bank.accounts[user_id]

        # ---------- PASSWORD CHECK ----------

        if acc.check_password(password):

            messagebox.showinfo(
                "Success",
                "Login Successful"
            )

            # ---------- CLEAR FIELDS ----------

            user_entry.delete(0, END)

            password_entry.delete(0, END)

            login_window.destroy()

            root.withdraw()

            # ---------- OPEN DASHBOARD ----------

            if acc.role == "admin":

                open_admin_dashboard(
                    bank,
                    acc,
                    root
                )

            else:

                open_user_dashboard(
                    bank,
                    acc,
                    root
                )

        else:

            messagebox.showerror(
                "Error",
                "Wrong Password"
            )

            password_entry.delete(0, END)

            password_entry.focus()


    # ==================================================
    # EXIT FUNCTION
    # ==================================================

    def exit_window():

        login_window.destroy()

        root.deiconify()


    # ==================================================
    # ENTER KEY NAVIGATION
    # ==================================================

    def move_to_password(event):

        user_id = user_entry.get().strip()

        if user_id == "":

            messagebox.showerror(
                "Error",
                "User ID is Required"
            )

            user_entry.focus()

            return

        if not user_id.isdigit():

            messagebox.showerror(
                "Error",
                "Please enter valid User ID"
            )

            user_entry.delete(0, END)

            user_entry.focus()

            return

        user_id = int(user_id)

        if user_id not in bank.accounts:

            messagebox.showerror(
                "Error",
                "Account Not Found"
            )

            user_entry.delete(0, END)

            user_entry.focus()

            return

        password_entry.focus()


    # ==================================================
    # ENTER KEY BINDS
    # ==================================================

    user_entry.bind(
        "<Return>",
        move_to_password
    )

    password_entry.bind(
        "<Return>",
        lambda event: login()
    )


    # ==================================================
    # BUTTON FRAME
    # ==================================================

    button_frame = Frame(
        container,
        bg="white"
    )

    button_frame.pack(pady=(10, 20))


    # ==================================================
    # LOGIN BUTTON
    # ==================================================

    login_btn = Button(
        button_frame,
        text="Login",
        width=12,
        bg="#2563eb",
        fg="white",
        activebackground="#1d4ed8",
        activeforeground="white",
        font=("Segoe UI", 11, "bold"),
        bd=0,
        relief="flat",
        cursor="hand2",
        pady=8,
        command=login
    )

    login_btn.grid(row=0, column=0, padx=10)

    add_hover_effect(login_btn)


    # ==================================================
    # EXIT BUTTON
    # ==================================================

    exit_btn = Button(
        button_frame,
        text="Exit",
        width=12,
        bg="#ef4444",
        fg="white",
        activebackground="#dc2626",
        activeforeground="white",
        font=("Segoe UI", 11, "bold"),
        bd=0,
        relief="flat",
        cursor="hand2",
        pady=8,
        command=exit_window
    )

    exit_btn.grid(row=0, column=1, padx=10)

    add_hover_effect(exit_btn)