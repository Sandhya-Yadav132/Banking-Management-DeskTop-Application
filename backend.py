import os
import re
from datetime import datetime


# ------------------- BANK CLASS -------------------

class Bank:

    def __init__(
        self,
        user_id,
        name,
        password,
        mobile_number,
        dob,
        balance=0.0,
        role='user'
    ):

        self.user_id = user_id
        self.name = name
        self.balance = balance
        self.__password = password
        self.mobile_number = mobile_number
        self.dob = dob
        self.role = role


    def to_line(self):

        return (
            f"{self.user_id},"
            f"{self.name},"
            f"{self.__password},"
            f"{self.balance},"
            f"{self.mobile_number},"
            f"{self.dob},"
            f"{self.role}"
        )


    def check_password(self, password):

        return self.__password == password


    def view_account(self):

        return (
            f"\nAccount Details\n"
            f"UserID : {self.user_id}\n"
            f"Name : {self.name}\n"
            f"Balance : ₹ {self.balance}\n"
            f"Mobile : {self.mobile_number}\n"
            f"DOB : {self.dob}\n"
        )


    def deposit(self, amount):

        if amount > 0:

            self.balance += amount

            return "Deposit Successful"

        return "Invalid Amount"


    def withdraw(self, amount):

        if amount <= 0:

            return "Invalid Amount"

        if amount > self.balance:

            return "Insufficient Balance"

        self.balance -= amount

        return "Withdraw Successful"


    def transaction(self, accounts, reciever_id, amount):

        if reciever_id not in accounts:

            return "Account Not Found"

        if amount <= 0:

            return "Invalid Amount"

        if amount > self.balance:

            return "Insufficient Balance"

        self.balance -= amount

        accounts[reciever_id].balance += amount

        return f"{amount} Rs. Transfer Successful"


# ------------------- ADMIN CLASS -------------------

class Admin(Bank):

    def search_user(self, accounts, user_id):

        if (
            user_id in accounts
            and accounts[user_id].role == "user"
        ):

            return accounts[user_id].view_account()

        return "User Not Found"


# ------------------- MAIN CONTROLLER -------------------

class Main:

    def __init__(self):

        self.accounts = {}

        if os.path.exists("accounts.txt"):

            self.load_accounts()

        if not self.accounts:

            self.exist_accounts()

            self.save_accounts()


    # ---------- SAVE ----------

    def save_accounts(self):

        with open("accounts.txt", "w") as f:

            for acc in self.accounts.values():

                f.write(acc.to_line() + "\n")


    # ---------- LOAD ----------

    def load_accounts(self):

        with open("accounts.txt", "r") as f:

            for line in f:

                line = line.strip()

                if line == "":

                    continue

                data = line.split(",")

                uid = int(data[0])
                name = data[1]
                password = data[2]
                balance = float(data[3])
                mobile = data[4]
                dob = data[5]
                role = data[6]

                if role == "admin":

                    acc = Admin(
                        uid,
                        name,
                        password,
                        mobile,
                        dob,
                        balance,
                        role
                    )

                else:

                    acc = Bank(
                        uid,
                        name,
                        password,
                        mobile,
                        dob,
                        balance,
                        role
                    )

                self.accounts[uid] = acc


    # ---------- DEFAULT ADMIN ----------

    def exist_accounts(self):

        admin = Admin(
            1001,
            "Admin",
            "Admin@123",
            "9999999999",
            "01-01-2000",
            role="admin"
        )

        self.accounts[1001] = admin


    # ---------- NAME VALIDATION ----------

    def validate_name(self, name):

        pattern = r"^[A-Za-z]+(?: [A-Za-z]+)*$"

        if not name:

            return "Required Field"

        elif len(name.replace(" ", "")) < 3:

            return "Please enter valid name"

        elif len(name) > 30:

            return "Too long, please enter valid name"

        elif not re.fullmatch(pattern, name):

            return "Please enter valid name"

        return True


    # ---------- PASSWORD VALIDATION ----------

    def validate_password(self, password):

        pattern = (
            r"^(?=.*[A-Z])"
            r"(?=.*\d)"
            r"(?=.*[^A-Za-z0-9]).{8,}$"
        )

        if not password:

            return "Required Field"

        elif not re.match(pattern, password):

            return """Password must contain:
- Minimum 8 characters
- At least 1 uppercase letter
- At least 1 number
- At least 1 special symbol"""

        return True


    # ---------- MOBILE VALIDATION ----------

    def validate_mobile(self, mobile):

        pattern = r"^[6-9]\d{9}$"

        if not mobile:

            return "Required Field"

        elif not re.match(pattern, mobile):

            return "Please enter valid number"

        elif mobile == mobile[0] * 10:

            return "Please enter valid number"

        return True


    # ---------- DOB VALIDATION ----------

    def validate_dob(self, dob):

        pattern = r"^\d{2}-\d{2}-\d{4}$"

        if not re.match(pattern, dob):

            return "Please enter DOB in DD-MM-YYYY format"

        try:

            dob_obj = datetime.strptime(
                dob,
                "%d-%m-%Y"
            )

            year = dob_obj.year

            if year < 1900 or year > 2025:

                return "Please enter valid year"

        except ValueError:

            return "Please enter valid date"

        return True