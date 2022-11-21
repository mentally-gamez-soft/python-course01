class Account():
    balance = 0 # variable de classe

    def add_amount(self, amount):
        self.balance += amount

    def withdraw_amount(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise Exception("You don't have sufficient balance to make a withdraw !")