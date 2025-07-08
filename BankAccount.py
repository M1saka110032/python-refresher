class BankAccount:
    def __init__(
        self, Account_name: str, Account_number: int, ini_balence: float = 0.00
    ):
        self.Account_name = Account_name
        self.Account_number = Account_number
        self.Account_balence = ini_balence

    def withdraw(self, amount: float = 0.00):
        if amount > 0:
            if amount < self.Account_balence:
                self.Account_balence -= amount
                print("Withdraw money successfully")
                return True
            else:
                print("Insufficient balance")
                return False
        else:
            print("The amount must be greater than 0")
            return False

    def deposit(self, amount: float = 0.00):
        if amount > 0:
            self.Account_balence += amount
            print("Deposit money successfully")
            return True
        else:
            print("The amount must be greater than 0")
            return False

    def show_balence(self):
        print("Your current account balence is" + str(self.Account_balence))
        return True
