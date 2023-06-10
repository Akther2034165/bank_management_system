class Bank:
    def __init__(self):
        self.balance = 0
        self.users = []
        self.loan_feature = False

    def create_account(self, email, password):
        user = User(email, password)
        self.users.append(user)
        self.balance += user.balance

    def enable_loan_feature(self):
        self.loan_feature = True

    def disable_loan_feature(self):
        self.loan_feature = False

    def total_loan_takes(self):
        total_loan = sum(user.loan_amount for user in self.users)
        return total_loan

    def is_bankrupt(self):
        return self.balance < 0


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
        self._adding_transaction("Deposited: ", amount)

    def withdraw_amount(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            bank.balance -= amount
            self._adding_transaction("Withdrawal: ", -amount)
            return True
        return False

    def transfer_amount(self, receiver, amount):
        if self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
            self._adding_transaction("Transfer", -amount)
            receiver._adding_transaction("Transfer", amount)
            return True
        return False

    def take_loan(self):
        if bank.loan_feature:
            loan_limit = self.balance * 2
            loan_amount = int(input("ENTER THE LOAN AMOUNT : "))
            if self.loan_amount == 0 and self.loan_amount + loan_amount <= loan_limit:
                self.balance += loan_amount
                self.loan_amount += loan_amount
                bank.balance += loan_amount
                self._adding_transaction("Loan", loan_amount)
                return True
        return False

    def _adding_transaction(self, types, amount):
        transaction = {
            "transaction_types": types,
            "amount": amount,
        }
        self.transaction_history.append(transaction)

    def check_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)

    def check_available_balance(self):
        return self.balance


class Admin:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def check_total_balance(self):
        return bank.balance

    def total_loan_takes(self):
        return bank.total_loan_takes()

    def enable_loan_feature(self):
        bank.loan_feature = True

    def disable_loan_feature(self):
        bank.loan_feature = False


print("_WELCOME TO BANK MANAGEMENT SYSTEM_")
bank = Bank()
admin = Admin('admin@gmail.com', '1234')


bank.create_account('aktherhosen@gmail.com', '123')
bank.create_account('nowshad@gmail.com', '456')

user_1 = bank.users[0]
user_2 = bank.users[1]


print("\n________________USER________________\n")
deposit_amount = int(input("ENTER THE DEPOSIT AMOUNT : "))
user_1.deposit_amount(deposit_amount)


balance = user_1.check_available_balance()
print("AFTER DEPOSIT ACCOUNT BALANCE : ", balance)


withdraw_amount = int(input("ENTER THE WITHDRAW AMOUNT : "))
withdraw = user_1.withdraw_amount(withdraw_amount)
if withdraw:
    print("WITHDRAW SUCCESSFULL!")
else:
    print("BANK IS BANKRUPT")
    exit()

balance = user_1.check_available_balance()
print("AFTER WITHDRAW ACCOUNT BALANCE : ", balance)


transfer_amount = int(input("ENTER THE TRANSFER AMOUNT : "))
transfer = user_1.transfer_amount(user_2, transfer_amount)
if transfer:
    print(
        f"TRANSFERRED {transfer_amount} TAKA SUCCESSFULLY TO :  {user_2.get_email()}")
else:
    print("YOU DO NOT HAVE SUFFICIENT BALANCE.")


balance = user_1.check_available_balance()
print("AFTER TRANSFER ACCOUNT BALANCE : ", balance)


admin.enable_loan_feature()
loan = user_1.take_loan()
if loan:
    print(f"{user_1.loan_amount} TAKA LOAN TAKEN SUCCESSFULLY.")
else:
    print("SOMETHING WENT WRONG. YOU CAN'T TAKE LOAN.")


balance = user_1.check_available_balance()
print("AFTER TAKING LOAN ACCOUNT BALANCE : ", balance)

print("\n________________ADMIN________________\n")
total_balance = admin.check_total_balance()
print("TOTAL BANK BALANCE :", total_balance)


total_loan_amount = admin.total_loan_takes()
print("TOTAL LOAN AMOUNT :", total_loan_amount)

admin.disable_loan_feature()

print("\n________________TRANSACTION HISTORY________________\n")
user_1.check_transaction_history()
