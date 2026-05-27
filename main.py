# from tkinter import *

# from backend import Main
# from create_account import open_create_account
# from login import open_login
# from utils import add_hover_effect

# bank = Main()

# root = Tk()

# root.title("Banking Management System")

# root.geometry("400x300")

# root.configure(bg="#dbeafe")


# # ---------------- MAIN FRAME ----------------

# main_frame = Frame(
#     root,
#     bg="#dbeafe"
# )

# main_frame.pack(expand=True)


# # ---------------- TITLE ----------------

# title = Label(
#     main_frame,
#     text="🏦 Banking Management System",
#     bg="#dbeafe",
#     # fg="#1e3a8a",
#     fg="black",
#     font=("Arial", 24, "bold")
# )

# title.pack(pady=20)


# # ---------------- CREATE ACCOUNT BUTTON ----------------

# create_btn = Button(
#     main_frame,
#     text="Create Account",
#     width=20,
#     height=2,
#     bg="#2563eb",
#     fg="white",
#     font=("Arial", 11, "bold"),
#     bd=2,
#     relief="solid",
#     cursor="hand2",
#     command=lambda: open_create_account(bank,root)
# )

# create_btn.pack(pady=10)

# add_hover_effect(create_btn)


# # ---------------- LOGIN BUTTON ----------------

# login_btn = Button(
#     main_frame,
#     text="Login",
#     width=20,
#     height=2,
#     bg="#2563eb",
#     fg="white",
#     font=("Arial", 11, "bold"),
#     bd=2,
#     relief="solid",
#     cursor="hand2",
#     command=lambda: open_login(bank, root)
# )

# login_btn.pack(pady=10)

# add_hover_effect(login_btn)


# # ---------------- EXIT BUTTON ----------------

# exit_btn = Button(
#     main_frame,
#     text="Exit",
#     width=20,
#     height=2,
#     bg="#2563eb",
#     fg="white",
#     font=("Arial", 11, "bold"),
#     bd=2,
#     relief="solid",
#     cursor="hand2",
#     command=root.destroy
# )

# exit_btn.pack(pady=10)

# add_hover_effect(exit_btn)


# root.mainloop()


from tkinter import *

from backend import Main
from create_account import open_create_account
from login import open_login
from utils import add_hover_effect

bank = Main()

# ==================================================
# ROOT WINDOW
# ==================================================

root = Tk()

root.title("Banking Management System")

root.geometry("1200x650")

root.configure(bg="white")

root.minsize(1000, 600)


# ==================================================
# MAIN FRAME
# ==================================================

main_frame = Frame(root, bg="white")

main_frame.pack(fill="both", expand=True)


# ==================================================
# LEFT FRAME (50%)
# ==================================================

left_frame = Frame(
    main_frame,
    bg="#0f172a"
)

left_frame.place(
    relx=0,
    rely=0,
    relwidth=0.5,
    relheight=1
)


# ==================================================
# RIGHT FRAME (50%)
# ==================================================

right_frame = Frame(
    main_frame,
    bg="#f8fafc"
)

right_frame.place(
    relx=0.5,
    rely=0,
    relwidth=0.5,
    relheight=1
)


# ==================================================
# LEFT SIDE CONTENT
# ==================================================

# ---------------- LOGO ----------------

logo = Label(
    left_frame,
    text="🏦",
    bg="#0f172a",
    fg="white",
    font=("Segoe UI", 52)
)

logo.pack(anchor="w", padx=70, pady=(70, 10))


# ---------------- TITLE ----------------

title = Label(
    left_frame,
    text="Banking\nManagement\nSystem",
    bg="#0f172a",
    fg="white",
    font=("Segoe UI", 38, "bold"),
    justify="left"
)

title.pack(anchor="w", padx=70)


# ---------------- BLUE LINE ----------------

line = Frame(
    left_frame,
    bg="#3b82f6",
    width=90,
    height=4
)

line.pack(anchor="w", padx=70, pady=25)


# ---------------- SUBTITLE ----------------

subtitle = Label(
    left_frame,
    text="Secure • Reliable • Modern Banking\nManage your accounts with confidence.",
    bg="#0f172a",
    fg="#cbd5e1",
    font=("Segoe UI", 13),
    justify="left"
)

subtitle.pack(anchor="w", padx=70)


# ---------------- FEATURES ----------------

features = [
    "✔  Secure Banking",
    "✔  Fast Transactions",
    "✔  Easy Account Access",
    "✔  24/7 Customer Support"
]

for item in features:

    feature_label = Label(
        left_frame,
        text=item,
        bg="#0f172a",
        fg="white",
        font=("Segoe UI", 11)
    )

    feature_label.pack(anchor="w", padx=70, pady=8)


# ---------------- FOOTER ----------------

footer = Label(
    left_frame,
    text="Your Security • Our Priority",
    bg="#0f172a",
    fg="#94a3b8",
    font=("Segoe UI", 10)
)

footer.pack(side="bottom", pady=30)


# ==================================================
# RIGHT SIDE LOGIN CARD
# ==================================================

card = Frame(
    right_frame,
    bg="white",
    highlightbackground="#e2e8f0",
    highlightthickness=1
)

card.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    relwidth=0.68,
    relheight=0.72
)


# ==================================================
# CARD CONTENT
# ==================================================

# ---------------- TITLE ----------------

card_title = Label(
    card,
    text="Welcome",
    bg="white",
    fg="#0f172a",
    font=("Segoe UI", 26, "bold")
)

card_title.pack(pady=(40, 10))


# ---------------- SUBTITLE ----------------

card_subtitle = Label(
    card,
    text="Choose an option to continue",
    bg="white",
    fg="#64748b",
    font=("Segoe UI", 11)
)

card_subtitle.pack()


# ---------------- BLUE LINE ----------------

small_line = Frame(
    card,
    bg="#2563eb",
    width=70,
    height=3
)

small_line.pack(pady=25)




# ==================================================
# BUTTON STYLE
# ==================================================

btn_font = ("Segoe UI", 12, "bold")


# ==================================================
# CREATE ACCOUNT BUTTON
# ==================================================

create_btn = Button(
    card,
    text="Create New Account",
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    font=btn_font,
    relief="flat",
    bd=0,
    cursor="hand2",
    padx=20,
    pady=14,
    width=24,
    command=lambda: open_create_account(bank, root)
)

create_btn.pack(pady=12)

add_hover_effect(create_btn)


# ==================================================
# LOGIN BUTTON
# ==================================================

login_btn = Button(
    card,
    text="Login",
    bg="#078605",
    fg="white",
    activebackground="#159305",
    activeforeground="white",
    font=btn_font,
    relief="flat",
    bd=0,
    cursor="hand2",
    padx=20,
    pady=14,
    width=24,
    command=lambda: open_login(bank, root)
)

login_btn.pack(pady=12)
add_hover_effect(login_btn)



# ==================================================
# EXIT BUTTON
# ==================================================

exit_btn = Button(
    card,
    text="Exit",
    bg="#ef4444",
    fg="white",
    activebackground="#dc2626",
    activeforeground="white",
    font=btn_font,
    relief="flat",
    bd=0,
    cursor="hand2",
    padx=20,
    pady=14,
    width=24,
    command=root.destroy
)

exit_btn.pack(pady=12)

add_hover_effect(exit_btn)



# ==================================================
# COPYRIGHT
# ==================================================

copyright_label = Label(
    card,
    text="© 2026 Banking Management System",
    bg="white",
    fg="#94a3b8",
    font=("Segoe UI", 9)
)

copyright_label.pack(side="bottom", pady=25)


# ==================================================
# MAIN LOOP
# ==================================================

root.mainloop()