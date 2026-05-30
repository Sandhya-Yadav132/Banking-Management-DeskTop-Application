from tkinter import *
from tkinter import messagebox

from backend import Bank
from utils import add_hover_effect


def open_create_account(bank, root):

    create_window = Toplevel()

    create_window.title("Create Account")

    create_window.geometry("550x650")

    create_window.configure(bg="#f1f5f9")

    # create_window.resizable(False, False)

    # ==================================================
    # MAIN FRAME
    # ==================================================

    main_frame = Frame(
        create_window,
        bg="#f1f5f9"
    )

    main_frame.pack(fill="both", expand=True)


    # ==================================================
    # CONTAINER
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
        width=420,
        height=580
    )


    # ==================================================
    # TITLE
    # ==================================================

    title = Label(
        container,
        text="Create Account",
        bg="white",
        fg="#0f172a",
        font=("Segoe UI", 26, "bold")
    )

    title.pack(pady=(25, 5))


    # ==================================================
    # SUBTITLE
    # ==================================================

    subtitle = Label(
        container,
        text="Fill in your details to continue",
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

    blue_line.pack(pady=18)


    # ==================================================
    # FULL NAME
    # ==================================================

    name_label = Label(
        container,
        text="Full Name",
        bg="white",
        fg="#0f172a",
        font=("Segoe UI", 11, "bold")
    )

    name_label.pack(anchor="w", padx=60)

    name_entry = Entry(
        container,
        width=32,
        font=("Segoe UI", 12),
        relief="solid",
        bd=1
    )

    name_entry.pack(pady=(5, 15), ipady=7)


    # ==================================================
    # PASSWORD
    # ==================================================

    password_label = Label(
        container,
        text="Password",
        bg="white",
        fg="#0f172a",
        font=("Segoe UI", 11, "bold")
    )

    password_label.pack(anchor="w", padx=60)

    password_entry = Entry(
        container,
        width=32,
        show="*",
        font=("Segoe UI", 12),
        relief="solid",
        bd=1
    )

    password_entry.pack(pady=(5, 15), ipady=7)


    # ==================================================
    # MOBILE NUMBER
    # ==================================================

    mobile_label = Label(
        container,
        text="Mobile Number",
        bg="white",
        fg="#0f172a",
        font=("Segoe UI", 11, "bold")
    )

    mobile_label.pack(anchor="w", padx=60)

    mobile_entry = Entry(
        container,
        width=32,
        font=("Segoe UI", 12),
        relief="solid",
        bd=1
    )

    mobile_entry.pack(pady=(5, 15), ipady=7)


    # ==================================================
    # DOB
    # ==================================================

    dob_label = Label(
        container,
        text="DOB (DD-MM-YYYY)",
        bg="white",
        fg="#0f172a",
        font=("Segoe UI", 11, "bold")
    )

    dob_label.pack(anchor="w", padx=60)

    dob_entry = Entry(
        container,
        width=32,
        font=("Segoe UI", 12),
        relief="solid",
        bd=1
    )

    dob_entry.pack(pady=(5, 20), ipady=7)


    # ==================================================
    # REAL TIME VALIDATIONS
    # ==================================================

    def check_name(event):

        name = name_entry.get().strip()

        if name == "":
            return

        result = bank.validate_name(name)

        if result != True:

            messagebox.showerror(
                "Error",
                result
            )

            name_entry.focus()


    def check_password(event):

        password = password_entry.get()

        if password == "":
            return

        result = bank.validate_password(password)

        if result != True:

            messagebox.showerror(
                "Error",
                result
            )

            password_entry.focus()


    def check_mobile(event):

        mobile = mobile_entry.get()

        if mobile == "":
            return

        result = bank.validate_mobile(mobile)

        if result != True:

            messagebox.showerror(
                "Error",
                result
            )

            mobile_entry.focus()


    def check_dob(event):

        dob = dob_entry.get()

        if dob == "":
            return

        result = bank.validate_dob(dob)

        if result != True:

            messagebox.showerror(
                "Error",
                result
            )

            dob_entry.focus()


    # ==================================================
    # BIND EVENTS
    # ==================================================

    name_entry.bind(
        "<FocusOut>",
        check_name
    )

    password_entry.bind(
        "<FocusOut>",
        check_password
    )

    mobile_entry.bind(
        "<FocusOut>",
        check_mobile
    )

    dob_entry.bind(
        "<FocusOut>",
        check_dob
    )


    # ==================================================
    # CREATE ACCOUNT FUNCTION
    # ==================================================

    def create_account():

        name = name_entry.get().title().strip()

        password = password_entry.get()

        mobile = mobile_entry.get()

        dob = dob_entry.get()

        # ---------- EMPTY FIELD VALIDATION ----------

        if name == "":

            messagebox.showerror(
                "Error",
                "Full Name is Required"
            )

            name_entry.focus()

            return

        if password == "":

            messagebox.showerror(
                "Error",
                "Password is Required"
            )

            password_entry.focus()

            return

        if mobile == "":

            messagebox.showerror(
                "Error",
                "Mobile Number is Required"
            )

            mobile_entry.focus()

            return

        if dob == "":

            messagebox.showerror(
                "Error",
                "DOB is Required"
            )

            dob_entry.focus()

            return

        # ---------- VALIDATIONS ----------

        name_validation = bank.validate_name(name)

        if name_validation != True:

            messagebox.showerror(
                "Error",
                name_validation
            )

            name_entry.focus()

            return

        password_validation = bank.validate_password(password)

        if password_validation != True:

            messagebox.showerror(
                "Error",
                password_validation
            )

            password_entry.focus()

            return

        mobile_validation = bank.validate_mobile(mobile)

        if mobile_validation != True:

            messagebox.showerror(
                "Error",
                mobile_validation
            )

            mobile_entry.focus()

            return

        dob_validation = bank.validate_dob(dob)

        if dob_validation != True:

            messagebox.showerror(
                "Error",
                dob_validation
            )

            dob_entry.focus()

            return

        # ---------- USER ID ----------

        user_ids = []

        for acc in bank.accounts.values():

            if acc.role == "user":

                user_ids.append(acc.user_id)

        if user_ids:

            new_id = max(user_ids) + 1

        else:

            new_id = 2001

        # ---------- CREATE ACCOUNT ----------

        acc = Bank(
            new_id,
            name,
            password,
            mobile,
            dob
        )

        bank.accounts[new_id] = acc

        bank.save_accounts()

        messagebox.showinfo(
            "Success",
            f"Account Created\nYour ID : {new_id}"
        )

        create_window.destroy()


    # ==================================================
    # EXIT FUNCTION
    # ==================================================

    def exit_window():

        create_window.destroy()

        root.deiconify()


    # ==================================================
    # ENTER KEY NAVIGATION
    # ==================================================

    name_entry.bind(
        "<Return>",
        lambda event: password_entry.focus()
    )

    password_entry.bind(
        "<Return>",
        lambda event: mobile_entry.focus()
    )

    mobile_entry.bind(
        "<Return>",
        lambda event: dob_entry.focus()
    )

    dob_entry.bind(
        "<Return>",
        lambda event: create_account()
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
    # CREATE BUTTON
    # ==================================================

    create_btn = Button(
        button_frame,
        text="Create Account",
        width=15,
        bg="#2563eb",
        fg="white",
        activebackground="#1d4ed8",
        activeforeground="white",
        font=("Segoe UI", 11, "bold"),
        bd=0,
        relief="flat",
        cursor="hand2",
        pady=8,
        command=create_account
    )

    create_btn.grid(row=0, column=0, padx=10)

    add_hover_effect(create_btn)


    # ==================================================
    # EXIT BUTTON
    # ==================================================

    exit_btn = Button(
        button_frame,
        text="Exit",
        width=15,
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
