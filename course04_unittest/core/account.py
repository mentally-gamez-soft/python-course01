class Account():
    """ Classe Account: represente un compte bancaire

    Un account possede une propriété:
    - balance: le solde du compte en banque

    Raises:
        Exception: 
          levée si le client essaye de retirer plus que son solde
    """    
    balance = 0 # variable de classe

    def add_amount(self, amount):
        self.balance += amount

    def withdraw_amount(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise Exception("You don't have sufficient balance to make a withdraw !")