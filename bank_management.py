class Bank:
    def __init__(self):
        self.balance = 0
        self.users = []
        self.loan_feature = False

    def create_account(self, email, password):
        user = User(email, password, self)
        self.users.append(user)

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
    def __init__(self, email, password, bank):
        self.email = email
        self.password = password
        self.balance = 0
        self.loan_amount = 0
        self.transaction_history = []
        self.bank = bank

    def deposit_amount(self, amount):
        self.balance += amount
        self.bank.balance += amount
        self._add_transaction("Deposited: ", amount)

    def withdraw_amount(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.bank.balance -= amount
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
            loan_amount = int(input("Enter the loan amount: "))
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
    def __init__(self, email, password, bank):
        self.email = email
        self.password = password
        self.bank = bank

    def check_total_balance(self):
        return self.bank.balance

    def get_total_loan_taken(self):
        return self.bank.get_total_loan_taken()

    def enable_loan_feature(self):
        self.bank.enable_loan_feature()

    def disable_loan_feature(self):
        self.bank.disable_loan_feature()


# Example Usage
bank = Bank()
admin = Admin('admin@gmail.com', '1234', bank)

# Creating user accounts
bank.create_account('akther@gmail.com', '123')

# Accessing user account
user = User('akther@gmail.com', '123', bank)

# Depositing money
deposit_amount = int(input("ENTER THE DEPOSIT AMOUNT: "))
user.deposit_amount(deposit_amount)

# Checking balance
balance = user.check_available_balance()
print("AFTER DEPOSIT ACCOUNT BALANCE:", balance)

# Withdrawing money
withdraw_amount = int(input("ENTER THE WITHDRAW AMOUNT: "))
withdraw = user.withdraw_amount(withdraw_amount)
if withdraw:
    print("WITHDRAW SUCCESSFUL!")
else:
    print("BANK IS BANKRUPT")

# Checking balance after withdraw
balance = user.check_available_balance()
print("AFTER WITHDRAW ACCOUNT BALANCE:", balance)

# Transferring money
transfer_amount = int(input("ENTER THE TRANSFER AMOUNT: "))
receiver = User('nowshad@gmail.com', '456', bank)
transfer = user.transfer_amount(receiver, transfer_amount)
if transfer:
    print(f"TRANSFERRED {transfer_amount} TAKA SUCCESSFULLY.")
else:
    print("YOU DO NOT HAVE SUFFICIENT BALANCE.")

# Checking balance after transferring
balance = user.check_available_balance()
print("AFTER TRANSFER ACCOUNT BALANCE:", balance)

# Checking transaction history
user.check_transaction_history()

# Taking a loan
bank.enable_loan_feature()
loan_success = user.take_loan()
if loan_success:
    print("Loan taken successfully. Loan amount:", user.loan_amount)
else:
    print("You can't take a loan from the bank.")

# Checking balance after taking loan
balance = user.check_available_balance()
print("AFTER TAKING LOAN ACCOUNT BALANCE:", balance)

# Checking the bank's total available balance
total_balance = admin.check_total_balance()
print("TOTAL BANK BALANCE:", total_balance)

# Checking total loan amount as an admin
total_loan_amount = admin.get_total_loan_taken()
print("TOTAL LOAN AMOUNT:", total_loan_amount)

# Disabling the loan feature
admin.disable_loan_feature()
