def take_loan(self, loan_amount):
        if bank.loan_feature:
            loan_limit = self.balance * 2
            if self.loan_amount == 0 and bank.loan_amount + loan_amount <= loan_limit:
                self.balance += loan_amount
                self.loan_amount += loan_amount
                bank.balance += loan_amount
                bank.loan_amount += loan_amount
                self._add_transaction("Loan", loan_amount)
                return True
        return False