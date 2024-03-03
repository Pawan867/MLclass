class BankAccount:
    def __init__(self, account_number, balance, owner):
        self.__account_number = account_number
        self.__balance = balance
        self.__owner = owner

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")

    def set_owner(self, owner):
        if owner:
            self.__owner = owner
        else:
            print("Owner name cannot be empty.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}.")
        else:
            print("Invalid withdrawal amount")


account = BankAccount("123456789", 2000, "Acharya Pawan")


print(f"Account Number: {account.get_account_number()}")
print(f"Balance: {account.get_balance()}")
print(f"Owner: {account.get_owner()}")

account.deposit(600)
account.withdraw(400)
