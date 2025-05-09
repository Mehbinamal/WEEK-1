class BankAccount:
    #constructor 
    def __init__(self, owner : str, balance = 0.0):
        self.owner = owner
        self.balance = balance

    #Functions 
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")

    def get_balance(self):
        return self.balance


# Example usage:
account = BankAccount("Amal", 1000)
account.deposit(500)
account.withdraw(300)
print("Final balance:", account.get_balance())
