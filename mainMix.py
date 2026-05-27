from tkinter import *
from tkinter import messagebox

from backend import Main
from backend import Bank

bank = Main()

root = Tk()

root.title("Banking System")
root.geometry("400x300")


# ---------------- USER DASHBOARD ----------------

def open_user_dashboard(acc):

    dashboard = Toplevel()

    dashboard.title("User Dashboard")

    dashboard.geometry("400x350")

    welcome_label = Label(
        dashboard,
        text=f"Welcome {acc.name}",
        font=("Arial", 18)
    )

    welcome_label.pack(pady=20)

    amount_entry = Entry(
        dashboard,
        width=30
    )

    amount_entry.pack(pady=10)

    receiver_entry = Entry(
        dashboard,
        width=30
    )

    receiver_entry.pack(pady=10)


    def check_balance():

        messagebox.showinfo(
            "Balance",
            f"Current Balance : ₹ {acc.balance}"
        )


    def deposit():

        amount = amount_entry.get()

        if not amount.isdigit():

            messagebox.showerror(
                "Error",
                "Please enter valid amount"
            )

            return

        amount = int(amount)

        msg = acc.deposit(amount)

        bank.save_accounts()

        messagebox.showinfo(
            "Deposit",
            msg
        )

    def transfer():

        receiver_id = receiver_entry.get()

        amount = amount_entry.get()

        if not receiver_id.isdigit() or not amount.isdigit():

            messagebox.showerror(
                "Error",
                "Please enter valid details"
            )

            return

        receiver_id = int(receiver_id)

        amount = int(amount)

        msg = acc.transaction(
            bank.accounts,
            receiver_id,
            amount
        )

        bank.save_accounts()

        messagebox.showinfo(
            "Transaction",
            msg
        )

    balance_btn = Button(
        dashboard,
        text="Check Balance",
        width=20,
        command=check_balance
    )

    balance_btn.pack(pady=10)


    deposit_btn = Button(
        dashboard,
        text="Deposit",
        width=20,
        command=deposit
    )

    deposit_btn.pack(pady=10)

    transfer_btn = Button(
        dashboard,
        text="Transfer",
        width=20,
        command=transfer
    )

    transfer_btn.pack(pady=10)


    logout_btn = Button(
        dashboard,
        text="Logout",
        width=20,
        command=dashboard.destroy
    )

    logout_btn.pack(pady=10)


# ---------------- ADMIN DASHBOARD ----------------

def open_admin_dashboard(acc):

    dashboard = Toplevel()

    dashboard.title("Admin Dashboard")

    dashboard.geometry("500x400")

    welcome_label = Label(
        dashboard,
        text=f"Welcome Admin {acc.name}",
        font=("Arial", 18)
    )

    welcome_label.pack(pady=20)


    def view_users():

        output.delete("1.0", END)

        for acc in bank.accounts.values():

            if acc.role == "user":

                output.insert(
                    END,
                    f"ID : {acc.user_id} | Name : {acc.name}\n"
                )


    view_btn = Button(
        dashboard,
        text="View All Users",
        width=20,
        command=view_users
    )

    view_btn.pack(pady=10)


    search_btn = Button(
        dashboard,
        text="Search User",
        width=20
    )

    search_btn.pack(pady=10)


    output = Text(
        dashboard,
        width=45,
        height=10
    )

    output.pack(pady=10)


    logout_btn = Button(
        dashboard,
        text="Logout",
        width=20,
        command=dashboard.destroy
    )

    logout_btn.pack(pady=10)

def open_create_account():

    create_window = Toplevel()

    create_window.title("Create Account")

    create_window.geometry("400x400")
    title = Label(
        create_window,
        text="Create Account",
        font=("Arial", 18)
    )

    title.pack(pady=20)


    name_label = Label(
        create_window,
        text="Full Name"
    )

    name_label.pack()

    name_entry = Entry(
        create_window,
        width=30
    )

    name_entry.pack(pady=10)


    password_label = Label(
        create_window,
        text="Password"
    )

    password_label.pack()

    password_entry = Entry(
        create_window,
        width=30,
        show="*"
    )

    password_entry.pack(pady=10)


    mobile_label = Label(
        create_window,
        text="Mobile Number"
    )

    mobile_label.pack()

    mobile_entry = Entry(
        create_window,
        width=30
    )

    mobile_entry.pack(pady=10)

    dob_label = Label(
        create_window,
        text="DOB (DD-MM-YYYY)"
    )

    dob_label.pack()

    dob_entry = Entry(
        create_window,
        width=30
    )

    dob_entry.pack(pady=10)

    def create_account():

        name = name_entry.get()

        password = password_entry.get()

        mobile = mobile_entry.get()

        dob = dob_entry.get()

        if name == "" or password == "" or mobile == "" or dob == "":

            messagebox.showerror(
                "Error",
                "All Fields Are Required"
            )

            return
        if not mobile.isdigit() or len(mobile) != 10:

            messagebox.showerror(
                "Error",
                "Please Enter Valid Mobile Number"
            )

            return
        if len(password) < 8:

            messagebox.showerror(
                "Error",
                "Password Must Be At Least 8 Characters"
            )

            return


        user_ids = []

        for acc in bank.accounts.values():

            if acc.role == "user":

                user_ids.append(acc.user_id)


        if user_ids:

            new_id = max(user_ids) + 1

        else:

            new_id = 2001


        from backend import Bank

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
    create_btn = Button(
        create_window,
        text="Create Account",
        command=create_account
    )
    create_btn.pack(pady=20)


# ---------------- LOGIN FUNCTION ----------------

def login():

    user_id = user_entry.get()

    password = password_entry.get()

    if not user_id.isdigit():

        messagebox.showerror(
            "Error",
            "Please enter valid User ID"
        )

        return

    user_id = int(user_id)

    if user_id in bank.accounts:

        acc = bank.accounts[user_id]

        if acc.check_password(password):

            messagebox.showinfo(
                "Success",
                "Login Successful"
            )

            if acc.role == "admin":

                open_admin_dashboard(acc)

            else:

                open_user_dashboard(acc)

        else:

            messagebox.showerror(
                "Error",
                "Wrong Password"
            )

    else:

        messagebox.showerror(
            "Error",
            "Account Not Found"
        )


# ---------------- MAIN WINDOW ----------------

title = Label(
    root,
    text="Banking Login",
    font=("Arial", 20)
)

title.pack(pady=20)


user_label = Label(
    root,
    text="User ID"
)

user_label.pack()

user_entry = Entry(
    root,
    width=30
)

user_entry.pack(pady=5)


password_label = Label(
    root,
    text="Password"
)

password_label.pack()

password_entry = Entry(
    root,
    width=30,
    show="*"
)

password_entry.pack(pady=5)


login_btn = Button(
    root,
    text="Login",
    width=20,
    command=login
)

login_btn.pack(pady=20)

create_btn = Button(
    root,
    text="Create Account",
    width=20,
    command=open_create_account
)

create_btn.pack()


root.mainloop()