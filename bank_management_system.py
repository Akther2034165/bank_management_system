class Bank:
    def __init__(self):
        self.balance = 0
        self.users = []
        self.loan_feature = False

    def create_account(self, email, password):
        user = User(email, password)
        self.users.append(user)
        self.balance += user.balance

    def is_bankrupt(self):
        return self.balance < 0

    def enable_loan_feature(self):
        self.loan_feature = True

    def disable_loan_feature(self):
        self.loan_feature = False

    def get_total_loan_taken(self):
        total_loan_amount = sum(user.loan_amount for user in self.users)
        return total_loan_amount


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.balance = 0
        self.loan_amount = 0
        self.transaction_history = []

    def get_email(self):
        return self.email

    def deposit_amount(self, amount):
        self.balance += amount
        bank.balance += amount
        self._add_transaction("Deposited: ", amount)

    def withdraw_amount(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            bank.balance -= amount
            self._add_transaction("Withdrawal: ", -amount)
            return True
        return False

    def transfer_amount(self, receiver, amount):
        if self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
            self._add_transaction("Transfer", -amount)
            receiver._add_transaction("Transfer", amount)
            return True
        return False

    def check_available_balance(self):
        return self.balance

    def check_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self):
        if bank.loan_feature:
            loan_limit = self.balance * 2
            loan_amount = int(input("ENTER THE LOAN AMOUNT : "))
            if self.loan_amount == 0 and self.loan_amount + loan_amount <= loan_limit:
                self.balance += loan_amount
                self.loan_amount += loan_amount
                bank.balance += loan_amount
                self._add_transaction("Loan", loan_amount)
                return True
        return False

    def _add_transaction(self, types, amount):
        transaction = {
            "transaction_types": types,
            "amount": amount,
        }
        self.transaction_history.append(transaction)


class Admin:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def check_total_balance(self):
        return bank.balance

    def get_total_loan_taken(self):
        return bank.get_total_loan_taken()

    def enable_loan_feature(self):
        bank.loan_feature = True

    def disable_loan_feature(self):
        bank.loan_feature = False


bank = Bank()
admin = Admin('admin@gmail.com', '1234')

# Creating user accounts for user_1
bank.create_account('aktherhosen@gmail.com', '123')
bank.create_account('nowshad@gmail.com', '456')

# Accessing user_1 account
user_1 = bank.users[0]
user_2 = bank.users[1]

# Depositing money for user_1
deposit_amount = int(input("ENTER THE DEPOSIT AMOUNT : "))
user_1.deposit_amount(deposit_amount)

# Checking balance for user_1
balance = user_1.check_available_balance()
print("AFTER DEPOSIT ACCOUNT BALANCE : ", balance)

# Withdrawing money for user_1
withdraw_amount = int(input("ENTER THE WITHDRAW AMOUNT : "))
withdraw = user_1.withdraw_amount(withdraw_amount)
if withdraw:
    print("WITHDRAW SUCCESSFULL!")
else:
    print("BANK IS BANKRUPT")

# Checking balance after withdraw for user_1
balance = user_1.check_available_balance()
print("AFTER WITHDRAW ACCOUNT BALANCE : ", balance)

# Transferring money for user_1
transfer_amount = int(input("ENTER THE TRANSFER AMOUNT : "))
transfer = user_1.transfer_amount(user_2, transfer_amount)
if transfer:
    print(
        f"TRANSFERRED {transfer_amount} TAKA SUCCESSFULLY TO :  {user_2.get_email()}")
else:
    print("YOU DO NOT HAVE SUFFICIENT BALANCE.")

# Checking balance after transferring user_1
balance = user_1.check_available_balance()
print("AFTER TRANSFER ACCOUNT BALANCE : ", balance)


# Taking a loan user_1
admin.enable_loan_feature()
loan = user_1.take_loan()
if loan:
    print(f"{user_1.loan_amount} TAKA LOAN TAKEN SUCCESSFULLY.")
else:
    print("SOMETHING WENT WRONG. YOU CAN'T TAKE LOAN.")

# Checking balance after taking loan user_1
balance = user_1.check_available_balance()
print("AFTER TAKING LOAN ACCOUNT BALANCE : ", balance)

# Checking transaction history user_1
user_1.check_transaction_history()


# Checking the bank's total available balance
total_balance = admin.check_total_balance()
print("TOTAL BANK BALANCE :", total_balance)

# Checking total loan amount as an admin
total_loan_amount = admin.get_total_loan_taken()
print("TOTAL LOAN AMOUNT :", total_loan_amount)


# Disabling the loan feature
admin.disable_loan_feature()
