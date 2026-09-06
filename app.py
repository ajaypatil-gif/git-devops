class BankAccount:

    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.__balance = balance   # Encapsulation

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")

        self.__balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount
        print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.__balance}")

    def display_account(self):
        print("\n----- Account Details -----")
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.name}")
        print(f"Balance       : ₹{self.__balance}")


class SavingsAccount(BankAccount):

    def __init__(self, account_number, name, balance=0, interest_rate=4):
        super().__init__(account_number, name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        # We cannot directly access __balance because it is private.
        # For a real application, we would provide a getter.
        print(f"Interest Rate: {self.interest_rate}%")


class Bank:

    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}

    def create_account(self, account_number, name, balance=0):

        if account_number in self.accounts:
            raise ValueError("Account already exists")

        account = BankAccount(
            account_number,
            name,
            balance
        )

        self.accounts[account_number] = account

        print("Account created successfully!")

    def get_account(self, account_number):

        if account_number not in self.accounts:
            raise ValueError("Account not found")

        return self.accounts[account_number]

    def deposit(self, account_number, amount):

        account = self.get_account(account_number)
        account.deposit(amount)

    def withdraw(self, account_number, amount):

        account = self.get_account(account_number)
        account.withdraw(amount)

    def check_balance(self, account_number):

        account = self.get_account(account_number)
        account.check_balance()

    def display_account(self, account_number):

        account = self.get_account(account_number)
        account.display_account()


# -------------------------------
# Main Application
# -------------------------------

bank = Bank("ABC Bank")


while True:

    print("\n========== BANK APP ==========")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Account Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":

            account_number = input("Enter account number: ")
            name = input("Enter account holder name: ")
            balance = float(input("Enter initial deposit: "))

            bank.create_account(
                account_number,
                name,
                balance
            )

        elif choice == "2":

            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))

            bank.deposit(
                account_number,
                amount
            )

        elif choice == "3":

            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))

            bank.withdraw(
                account_number,
                amount
            )

        elif choice == "4":

            account_number = input("Enter account number: ")

            bank.check_balance(
                account_number
            )

        elif choice == "5":

            account_number = input("Enter account number: ")

            bank.display_account(
                account_number
            )

        elif choice == "6":

            print("Thank you for using ABC Bank!")
            break

        else:

            print("Invalid choice. Please try again.")

    except ValueError as e:

        print(f"Error: {e}")