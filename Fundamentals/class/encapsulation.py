class BankAccount:
    def __init__(self, balance):
        self._balance = balance     # Private Attribute

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance