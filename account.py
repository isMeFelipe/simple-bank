class AccountNotFoundError(Exception):
    """Exception raised when an account does not exist."""
    pass

class Account:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Cannot withdraw negative amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

# depósito
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit negative amount")
        self.balance += amount

# Transferência entre contas
    def transfer(self, amount, target_account):
        if target_account is None:
            raise AccountNotFoundError("Target account does not exist")
        if amount < 0:
            raise ValueError("Cannot transfer negative amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.withdraw(amount)
        target_account.deposit(amount)
