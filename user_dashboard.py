# from tkinter import *
# from tkinter import messagebox, simpledialog
# from utils import add_hover_effect

# def open_user_dashboard(bank, acc, root):

#     dashboard = Toplevel()

#     dashboard.title("User Dashboard")

#     dashboard.geometry("400x300")
#     dashboard.configure(bg="#dbeafe")


#     main_frame = Frame(dashboard,
#                        bg="#dbeafe")

#     main_frame.pack(expand=True)

#     welcome_label = Label(
#         main_frame,
#         text=f"Welcome {acc.name}",
#         bg="#dbeafe",
#         fg="#1e3a8a",
#         font=("Arial", 22, "bold")
#     )

#     welcome_label.pack(pady=20)


#     def check_balance():

#         messagebox.showinfo(
#             "Balance",
#             f"Current Balance : ₹ {acc.balance}",
#             parent=dashboard
#         )


#     def deposit():

#         amount = simpledialog.askinteger(
#             "Deposit",
#             "Enter Amount",
#             parent=dashboard
#         )

#         if amount is None:

#             return


#         msg = acc.deposit(amount)

#         bank.save_accounts()


#         messagebox.showinfo(
#             "Deposit",
#             msg,
#             parent=dashboard
#         )


#     def withdraw():

#         amount = simpledialog.askinteger(
#             "Withdraw",
#             "Enter Amount",
#             parent=dashboard
#         )

#         if amount is None:

#             return


#         msg = acc.withdraw(amount)

#         bank.save_accounts()


#         messagebox.showinfo(
#             "Withdraw",
#             msg,
#             parent=dashboard
#         )


#     def transfer():

#         receiver_id = simpledialog.askinteger(
#             "Transfer",
#             "Enter Receiver ID",
#             parent=dashboard
#         )

#         if receiver_id is None:

#             return


#         if receiver_id not in bank.accounts:

#             messagebox.showerror(
#                 "Error",
#                 "Account Not Found",
#                 parent=dashboard
#             )

#             return


#         receiver = bank.accounts[receiver_id]


#         confirm = messagebox.askyesno(
#             "Confirm Receiver",
#             f"Transfer To:\n\n"
#             f"Name : {receiver.name}\n"
#             f"ID : {receiver.user_id}",
#             parent=dashboard
#         )

#         if not confirm:

#             return


#         amount = simpledialog.askinteger(
#             "Transfer",
#             "Enter Amount",
#             parent=dashboard
#         )

#         if amount is None:

#             return


#         msg = acc.transaction(
#             bank.accounts,
#             receiver_id,
#             amount
#         )

#         bank.save_accounts()


#         messagebox.showinfo(
#             "Transaction",
#             msg,
#             parent=dashboard
#         )


#     def logout():

#         dashboard.destroy()

#         root.deiconify()


#     balance_btn = Button(
#         main_frame,
#         text="Check Balance",
#         width=20,
#         bg="#2563eb",
#         fg="white",
#         font=("Arial", 11, "bold"),
#         command=check_balance
#     )

#     balance_btn.pack(pady=10)
#     add_hover_effect(balance_btn)


#     deposit_btn = Button(
#         main_frame,
#         text="Deposit",
#         width=20,
#         bg="#2563eb",
#         fg="white",
#         font=("Arial", 11, "bold"),
#         command=deposit
#     )

#     deposit_btn.pack(pady=10)
#     add_hover_effect(deposit_btn)

#     withdraw_btn = Button(
#         main_frame,
#         text="Withdraw",
#         width=20,
#         bg="#2563eb",
#         fg="white",
#         font=("Arial", 11, "bold"),
#         command=withdraw
#     )

#     withdraw_btn.pack(pady=10)
#     add_hover_effect(withdraw_btn)

#     transfer_btn = Button(
#         main_frame,
#         text="Transfer",
#         width=20,
#         bg="#2563eb",
#         fg="white",
#         font=("Arial", 11, "bold"),
#         command=transfer
#     )

#     transfer_btn.pack(pady=10)
#     add_hover_effect(transfer_btn)

#     logout_btn = Button(
#         main_frame,
#         text="Logout",
#         width=20,
#         bg="#2563eb",
#         fg="white",
#         font=("Arial", 11, "bold"),
#         command=logout
#     )

#     logout_btn.pack(pady=10)
#     add_hover_effect(logout_btn)


from tkinter import *
from tkinter import messagebox, simpledialog
from utils import add_hover_effect


def open_user_dashboard(bank, acc, root):

    # ==================================================
    # WINDOW
    # ==================================================

    dashboard = Toplevel()

    dashboard.title("User Dashboard")

    dashboard.geometry("1280x720")

    dashboard.configure(bg="#f1f5f9")

    dashboard.minsize(1150, 650)


    # ==================================================
    # MAIN FRAME
    # ==================================================

    main_frame = Frame(
        dashboard,
        bg="#f1f5f9"
    )

    main_frame.pack(fill="both", expand=True)


    # ==================================================
    # SIDEBAR
    # ==================================================

    sidebar = Frame(
        main_frame,
        bg="#0f172a"
    )

    sidebar.place(
        relx=0,
        rely=0,
        relwidth=0.22,
        relheight=1
    )


    # ==================================================
    # CONTENT AREA
    # ==================================================

    content = Frame(
        main_frame,
        bg="#f1f5f9"
    )

    content.place(
        relx=0.22,
        rely=0,
        relwidth=0.78,
        relheight=1
    )


    # ==================================================
    # SIDEBAR HEADER
    # ==================================================

    logo = Label(
        sidebar,
        text="🏦",
        bg="#0f172a",
        fg="white",
        font=("Segoe UI", 42)
    )

    logo.pack(anchor="w", padx=35, pady=(35, 10))


    title = Label(
        sidebar,
        text="Banking\nDashboard",
        bg="#0f172a",
        fg="white",
        font=("Segoe UI", 25, "bold"),
        justify="left"
    )

    title.pack(anchor="w", padx=35)


    blue_line = Frame(
        sidebar,
        bg="#3b82f6",
        width=70,
        height=4
    )

    blue_line.pack(anchor="w", padx=35, pady=20)


    user_info = Label(
        sidebar,
        text=f"Welcome,\n{acc.name}",
        bg="#0f172a",
        fg="#cbd5e1",
        font=("Segoe UI", 12),
        justify="left"
    )

    user_info.pack(anchor="w", padx=35)


    # ==================================================
    # FUNCTIONS
    # ==================================================

    def refresh_balance():

        balance_amount.config(
            text=f"₹ {acc.balance}"
        )


    # ---------------- DEPOSIT ----------------

    def deposit():

        amount = simpledialog.askinteger(
            "Deposit",
            "Enter Amount",
            parent=dashboard
        )

        if amount is None:

            return

        msg = acc.deposit(amount)

        bank.save_accounts()

        refresh_balance()

        messagebox.showinfo(
            "Deposit",
            msg,
            parent=dashboard
        )


    # ---------------- WITHDRAW ----------------

    def withdraw():

        amount = simpledialog.askinteger(
            "Withdraw",
            "Enter Amount",
            parent=dashboard
        )

        if amount is None:

            return

        msg = acc.withdraw(amount)

        bank.save_accounts()

        refresh_balance()

        messagebox.showinfo(
            "Withdraw",
            msg,
            parent=dashboard
        )


    # ---------------- TRANSFER ----------------

    def transfer():

        receiver_id = simpledialog.askinteger(
            "Transfer",
            "Enter Receiver ID",
            parent=dashboard
        )

        if receiver_id is None:

            return

        if receiver_id not in bank.accounts:

            messagebox.showerror(
                "Error",
                "Account Not Found",
                parent=dashboard
            )

            return

        receiver = bank.accounts[receiver_id]

        confirm = messagebox.askyesno(
            "Confirm Receiver",
            f"Transfer To:\n\n"
            f"Name : {receiver.name}\n"
            f"ID : {receiver.user_id}",
            parent=dashboard
        )

        if not confirm:

            return

        amount = simpledialog.askinteger(
            "Transfer",
            "Enter Amount",
            parent=dashboard
        )

        if amount is None:

            return

        msg = acc.transaction(
            bank.accounts,
            receiver_id,
            amount
        )

        bank.save_accounts()

        refresh_balance()

        messagebox.showinfo(
            "Transaction",
            msg,
            parent=dashboard
        )


    # ---------------- VIEW ACCOUNT ----------------

    def view_account():

        profile = Toplevel()

        profile.title("My Account")

        profile.geometry("500x450")

        profile.configure(bg="#f1f5f9")

        profile.resizable(False, False)


        # =========================
        # CONTAINER
        # =========================

        container = Frame(
            profile,
            bg="white",
            highlightbackground="#dbeafe",
            highlightthickness=2
        )

        container.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=380,
            height=340
        )


        # =========================
        # ICON
        # =========================

        icon = Label(
            container,
            text="👤",
            bg="white",
            font=("Segoe UI", 40)
        )

        icon.pack(pady=(20, 10))


        # =========================
        # TITLE
        # =========================

        profile_title = Label(
            container,
            text="Account Details",
            bg="white",
            fg="#0f172a",
            font=("Segoe UI", 20, "bold")
        )

        profile_title.pack(pady=(0, 20))


        # =========================
        # DETAILS
        # =========================

        details = [
            ("Account Holder", acc.name),
            ("User ID", acc.user_id),
            ("Mobile Number", acc.mobile_number),
            ("DOB", acc.dob),
            ("Balance", f"₹ {acc.balance}")
        ]


        for label_text, value in details:

            row = Frame(
                container,
                bg="white"
            )

            row.pack(
                fill="x",
                padx=35,
                pady=8
            )

            label = Label(
                row,
                text=label_text,
                bg="white",
                fg="#475569",
                font=("Segoe UI", 11, "bold")
            )

            label.pack(side="left")


            value_label = Label(
                row,
                text=value,
                bg="white",
                fg="#0f172a",
                font=("Segoe UI", 11)
            )

            value_label.pack(side="right")


        # =========================
        # CLOSE BUTTON
        # =========================

        close_btn = Button(
            container,
            text="Close",
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            font=("Segoe UI", 11, "bold"),
            bd=0,
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=8,
            command=profile.destroy
        )

        close_btn.pack(pady=25)

        add_hover_effect(close_btn)


    # ---------------- LOGOUT ----------------

    def logout():

        dashboard.destroy()

        root.deiconify()


    # ==================================================
    # SIDEBAR BUTTONS
    # ==================================================

    button_frame = Frame(
        sidebar,
        bg="#0f172a"
    )

    button_frame.pack(pady=(60, 0))


    def sidebar_button(text, color, command):

        btn = Button(
            button_frame,
            text=text,
            width=22,
            bg=color,
            fg="white",
            activebackground=color,
            activeforeground="white",
            font=("Segoe UI", 11, "bold"),
            bd=0,
            relief="flat",
            cursor="hand2",
            pady=12,
            command=command
        )

        btn.pack(pady=12)

        add_hover_effect(btn)

        return btn


    sidebar_button(
        "👤  View Account",
        "#2563eb",
        view_account
    )

    sidebar_button(
        "🚪  Logout",
        "#ef4444",
        logout
    )


    # ==================================================
    # TOPBAR
    # ==================================================

    topbar = Frame(
        content,
        bg="white",
        height=80
    )

    topbar.pack(fill="x")

    topbar.pack_propagate(False)


    top_title = Label(
        topbar,
        text="User Banking Dashboard",
        bg="white",
        fg="#0f172a",
        font=("Segoe UI", 22, "bold")
    )

    top_title.pack(side="left", padx=35, pady=20)


    profile_icon = Label(
        topbar,
        text="👤",
        bg="white",
        font=("Segoe UI", 20)
    )

    profile_icon.pack(side="right", padx=30)


    # ==================================================
    # DASHBOARD CARDS
    # ==================================================

    cards_frame = Frame(
        content,
        bg="#f1f5f9"
    )

    cards_frame.pack(pady=30)


    def create_card(parent, title, value, color):

        card = Frame(
            parent,
            bg="white",
            width=280,
            height=180,
            highlightbackground="#e2e8f0",
            highlightthickness=1
        )

        card.pack(side="left", padx=18)

        card.pack_propagate(False)


        title_label = Label(
            card,
            text=title,
            bg="white",
            fg="#64748b",
            font=("Segoe UI", 12)
        )

        title_label.pack(pady=(35, 12))


        value_label = Label(
            card,
            text=value,
            bg="white",
            fg=color,
            font=("Segoe UI", 24, "bold")
        )

        value_label.pack()


        return value_label


    # ==================================================
    # CARDS
    # ==================================================

    create_card(
        cards_frame,
        "Account Holder",
        acc.name,
        "#0f172a"
    )

    create_card(
        cards_frame,
        "User ID",
        acc.user_id,
        "#2563eb"
    )

    balance_amount = create_card(
        cards_frame,
        "Total Balance",
        f"₹ {acc.balance}",
        "#16a34a"
    )


    # ==================================================
    # QUICK ACTIONS
    # ==================================================

    quick_frame = Frame(
        content,
        bg="#f1f5f9"
    )

    quick_frame.pack()


    quick_title = Label(
        quick_frame,
        text="Quick Banking Services",
        bg="#f1f5f9",
        fg="#0f172a",
        font=("Segoe UI", 22, "bold")
    )

    quick_title.pack(pady=(5, 25))


    action_frame = Frame(
        quick_frame,
        bg="#f1f5f9"
    )

    action_frame.pack()


    # ==================================================
    # ACTION BUTTON DESIGN
    # ==================================================

    def quick_action(text, bg_color, command):

        btn = Button(
            action_frame,
            text=text,
            width=17,
            height=5,
            bg=bg_color,
            fg="white",
            activebackground=bg_color,
            activeforeground="white",
            font=("Segoe UI", 11, "bold"),
            bd=0,
            relief="flat",
            cursor="hand2",
            justify="center",
            command=command
        )

        btn.pack(
            side="left",
            padx=20
        )

        add_hover_effect(btn)

        return btn


    # ==================================================
    # QUICK ACTION BUTTONS
    # ==================================================

    quick_action(
        "📥\nDeposit Money",
        "#16a34a",
        deposit
    )

    quick_action(
        "📤\nWithdraw Money",
        "#f97316",
        withdraw
    )

    quick_action(
        "🔄\nTransfer Money",
        "#7c3aed",
        transfer
    )


    # ==================================================
    # BOTTOM PANEL
    # ==================================================

    bottom_panel = Frame(
        content,
        bg="white",
        highlightbackground="#e2e8f0",
        highlightthickness=1
    )

    bottom_panel.pack(
        fill="both",
        expand=True,
        padx=35,
        pady=35
    )


    panel_title = Label(
        bottom_panel,
        text="Secure Banking Services",
        bg="white",
        fg="#0f172a",
        font=("Segoe UI", 24, "bold")
    )

    panel_title.pack(pady=(35, 10))


    panel_subtitle = Label(
        bottom_panel,
        text="Fast, Secure and Reliable Banking Experience.",
        bg="white",
        fg="#64748b",
        font=("Segoe UI", 12)
    )

    panel_subtitle.pack()


    line = Frame(
        bottom_panel,
        bg="#2563eb",
        width=90,
        height=4
    )

    line.pack(pady=22)


    features = [
        "✔  Instant Transactions",
        "✔  Secure Account Protection",
        "✔  Real-Time Balance Updates",
        "✔  Trusted Banking System"
    ]


    for item in features:

        feature = Label(
            bottom_panel,
            text=item,
            bg="white",
            fg="#0f172a",
            font=("Segoe UI", 13)
        )

        feature.pack(pady=5)


    footer = Label(
        bottom_panel,
        text="© 2026 Banking Management System",
        bg="white",
        fg="#94a3b8",
        font=("Segoe UI", 10)
    )

    footer.pack(side="bottom", pady=20)