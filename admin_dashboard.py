from tkinter import *
from tkinter import messagebox, simpledialog
from utils import add_hover_effect


def open_admin_dashboard(bank, acc, root):

    # ==================================================
    # WINDOW
    # ==================================================

    dashboard = Toplevel()

    dashboard.title("Admin Dashboard")

    dashboard.geometry("1350x720")

    dashboard.configure(bg="#f1f5f9")

    dashboard.minsize(1200, 650)


    # ==================================================
    # MAIN FRAME
    # ==================================================

    main_frame = Frame(
        dashboard,
        bg="#f1f5f9"
    )

    main_frame.pack(fill="both", expand=True)


    # ==================================================
    # LEFT PANEL
    # ==================================================

    left_panel = Frame(
        main_frame,
        bg="white",
        width=340
    )

    left_panel.pack(
        side="left",
        fill="y"
    )

    left_panel.pack_propagate(False)


    # ==================================================
    # RIGHT PANEL
    # ==================================================

    right_panel = Frame(
        main_frame,
        bg="#f8fafc"
    )

    right_panel.pack(
        side="right",
        fill="both",
        expand=True
    )


    # ==================================================
    # LEFT HEADER
    # ==================================================

    logo = Label(
        left_panel,
        text="🛡️",
        bg="white",
        fg="#2563eb",
        font=("Segoe UI", 45)
    )

    logo.pack(pady=(35, 10))


    title = Label(
        left_panel,
        text="Admin Control Panel",
        bg="white",
        fg="#0f172a",
        font=("Segoe UI", 24, "bold")
    )

    title.pack()


    subtitle = Label(
        left_panel,
        text="Manage users and monitor\nbanking activities easily.",
        bg="white",
        fg="#64748b",
        font=("Segoe UI", 11),
        justify="center"
    )

    subtitle.pack(pady=12)


    line = Frame(
        left_panel,
        bg="#2563eb",
        width=90,
        height=4
    )

    line.pack(pady=10)


    # ==================================================
    # BUTTON FRAME
    # ==================================================

    button_frame = Frame(
        left_panel,
        bg="white"
    )

    button_frame.pack(pady=40)


    # ==================================================
    # FUNCTIONS
    # ==================================================

    # ---------------- VIEW PROFILE ----------------

    def view_profile():

        profile_window = Toplevel()

        profile_window.title("Admin Profile")

        profile_window.geometry("500x500")

        profile_window.configure(bg="#f8fafc")
        profile_window.resizable(False,False)

        container = Frame(
            profile_window,
            bg="white",
            highlightbackground="#dbeafe",
            highlightthickness=2
        )

        container.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=400,
            height=400
        )


        icon = Label(
            container,
            text="👨‍💼",
            bg="white",
            fg="#2563eb",
            font=("Segoe UI", 45)
        )

        icon.pack(pady=(25, 10))


        heading = Label(
            container,
            text="Administrator Profile",
            bg="white",
            fg="#0f172a",
            font=("Segoe UI", 20, "bold")
        )

        heading.pack(pady=(0, 20))


        details = [

            ("Admin Name", acc.name),

            ("Admin ID", acc.user_id),

            ("Mobile Number", getattr(acc, "mobile_number", "N/A")),

            ("DOB", getattr(acc, "dob", "N/A")),

            ("Role", acc.role.title())
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
                font=("Segoe UI", 10, "bold")
            )

            label.pack(side="left")


            value_label = Label(
                row,
                text=value,
                bg="white",
                fg="#0f172a",
                font=("Segoe UI", 10)
            )

            value_label.pack(side="right")


    # ---------------- VIEW USERS ----------------

    def view_users():

        users_window = Toplevel()

        users_window.title("All Users")

        users_window.geometry("750x500")

        users_window.configure(bg="#f8fafc")

        users_window.resizable(False, False)



        heading = Label(
            users_window,
            text="Registered Users",
            bg="#f8fafc",
            fg="#0f172a",
            font=("Segoe UI", 22, "bold")
        )

        heading.pack(pady=20)


        output_frame = Frame(
            users_window,
            bg="white",
            highlightbackground="#cbd5e1",
            highlightthickness=1
        )

        output_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 25)
        )


        scrollbar = Scrollbar(output_frame)

        scrollbar.pack(side="right", fill="y")


        output = Text(
            output_frame,
            bg="white",
            fg="#0f172a",
            font=("Consolas", 11),
            bd=0,
            yscrollcommand=scrollbar.set,
            padx=20,
            pady=20
        )

        output.pack(fill="both", expand=True)

        scrollbar.config(command=output.yview)


        found = False

        for user in bank.accounts.values():

            if user.role == "user":

                found = True

                output.insert(
                    END,

                    f"{'='*55}\n"
                    f"USER ID       : {user.user_id}\n"
                    f"NAME          : {user.name}\n"
                    f"BALANCE       : ₹ {user.balance}\n"
                    f"MOBILE NUMBER : {user.mobile_number}\n"
                    f"DOB           : {user.dob}\n"
                    f"ROLE          : {user.role}\n"
                    f"{'='*55}\n\n"
                )

        if not found:

            output.insert(
                END,
                "No Users Found"
            )


    # ---------------- SEARCH USER ----------------

    def search_user():

        user_id = simpledialog.askinteger(
            "Search User",
            "Enter User ID",
            parent=dashboard
        )

        if user_id is None:

            return


        if user_id not in bank.accounts:

            messagebox.showerror(
                "Error",
                "User Not Found",
                parent=dashboard
            )

            return


        user = bank.accounts[user_id]


        if user.role == "admin":

            messagebox.showerror(
                "Error",
                "Admin Account Cannot Be Searched",
                parent=dashboard
            )

            return


        search_window = Toplevel()

        search_window.title("User Details")

        search_window.geometry("550x450")

        search_window.configure(bg="#f8fafc")

        search_window.resizable(False, False)


        container = Frame(
            search_window,
            bg="white",
            highlightbackground="#cbd5e1",
            highlightthickness=1
        )

        container.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=430,
            height=350
        )


        heading = Label(
            container,
            text="User Information",
            bg="white",
            fg="#0f172a",
            font=("Segoe UI", 20, "bold")
        )

        heading.pack(pady=(25, 20))


        details = [

            ("User ID", user.user_id),

            ("Name", user.name),

            ("Balance", f"₹ {user.balance}"),

            ("Mobile", user.mobile_number),

            ("DOB", user.dob),

            ("Role", user.role.title())
        ]


        for label_text, value in details:

            row = Frame(
                container,
                bg="white"
            )

            row.pack(
                fill="x",
                padx=35,
                pady=7
            )


            label = Label(
                row,
                text=label_text,
                bg="white",
                fg="#475569",
                font=("Segoe UI", 10, "bold")
            )

            label.pack(side="left")


            value_label = Label(
                row,
                text=value,
                bg="white",
                fg="#0f172a",
                font=("Segoe UI", 10)
            )

            value_label.pack(side="right")


    # ---------------- LOGOUT ----------------

    def logout():

        dashboard.destroy()

        root.deiconify()


    # ==================================================
    # BUTTON STYLE
    # ==================================================

    def admin_button(text, color, command):

        btn = Button(
            button_frame,
            text=text,
            width=24,
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


    # ==================================================
    # BUTTONS
    # ==================================================

    admin_button(
        "👨‍💼  View Profile",
        "#2563eb",
        view_profile
    )

    admin_button(
        "👥  View All Users",
        "#7c3aed",
        view_users
    )

    admin_button(
        "🔍  Search User",
        "#16a34a",
        search_user
    )

    admin_button(
        "🚪  Logout",
        "#ef4444",
        logout
    )


    # ==================================================
    # RIGHT TOPBAR
    # ==================================================

    topbar = Frame(
        right_panel,
        bg="white",
        height=80
    )

    topbar.pack(fill="x")

    topbar.pack_propagate(False)


    top_title = Label(
        topbar,
        text="Banking Management Analytics",
        bg="white",
        fg="#0f172a",
        font=("Segoe UI", 22, "bold")
    )

    top_title.pack(
        side="left",
        padx=35,
        pady=20
    )


    # ==================================================
    # DASHBOARD CARDS
    # ==================================================

    cards_frame = Frame(
        right_panel,
        bg="#f8fafc"
    )

    cards_frame.pack(pady=35)


    def create_card(title, value, color):

        card = Frame(
            cards_frame,
            bg="white",
            width=250,
            height=150,
            highlightbackground="#e2e8f0",
            highlightthickness=1
        )

        card.pack(
            side="left",
            padx=18
        )

        card.pack_propagate(False)


        title_label = Label(
            card,
            text=title,
            bg="white",
            fg="#64748b",
            font=("Segoe UI", 12)
        )

        title_label.pack(
            pady=(35, 10)
        )


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
    # CALCULATIONS
    # ==================================================

    total_accounts = 0

    total_balance = 0

    for user in bank.accounts.values():

        if user.role == "user":

            total_accounts += 1

            total_balance += user.balance


    # ==================================================
    # CARDS
    # ==================================================

    create_card(
        "Admin Name",
        acc.name,
        "#0f172a"
    )

    create_card(
        "Total Users",
        total_accounts,
        "#2563eb"
    )

    create_card(
        "Total Balance",
        f"₹ {total_balance}",
        "#16a34a"
    )


    # ==================================================
    # WELCOME SECTION
    # ==================================================

    welcome_box = Frame(
        right_panel,
        bg="white",
        highlightbackground="#e2e8f0",
        highlightthickness=1
    )

    welcome_box.pack(
        fill="both",
        expand=True,
        padx=35,
        pady=(0, 35)
    )


    welcome_title = Label(
        welcome_box,
        text=f"Welcome Back, {acc.name}",
        bg="white",
        fg="#0f172a",
        font=("Segoe UI", 26, "bold")
    )

    welcome_title.pack(pady=(90, 15))


    welcome_subtitle = Label(
        welcome_box,
        text="Manage users, monitor banking activities,\nand control the banking system securely.",
        bg="white",
        fg="#64748b",
        font=("Segoe UI", 13),
        justify="center"
    )

    welcome_subtitle.pack()
