class BankAccount:

    def __init__(self, holder, acc_number, balance=0):
        self.holder = holder
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return
        self.balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal successful")

    def transfer(self, target, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            target.balance += amount
            print("Transfer successful")

    def display(self):
        print("Account Holder:", self.holder)
        print("Account Number:", self.acc_number)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):

    def __init__(self, holder, acc_number, balance=0, interest_rate=0.03):
        super().__init__(holder, acc_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print("Interest added:", interest)


accounts = {}


while True:

    print("\n----- BANK MENU -----")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Apply Interest (Savings)")
    print("6. Display Account")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter account holder name: ")
        acc_no = input("Enter account number: ")
        balance = float(input("Enter initial balance: "))

        acc_type = input("Account type (normal/savings): ")

        if acc_type.lower() == "savings":
            account = SavingsAccount(name, acc_no, balance)
        else:
            account = BankAccount(name, acc_no, balance)

        accounts[acc_no] = account

        print("Account created successfully")

    elif choice == "2":

        acc_no = input("Enter account number: ")

        if acc_no in accounts:
            amount = float(input("Enter deposit amount: "))
            accounts[acc_no].deposit(amount)
        else:
            print("Account not found")

    elif choice == "3":

        acc_no = input("Enter account number: ")

        if acc_no in accounts:
            amount = float(input("Enter withdraw amount: "))
            accounts[acc_no].withdraw(amount)
        else:
            print("Account not found")

    elif choice == "4":

        sender = input("Enter sender account number: ")
        receiver = input("Enter receiver account number: ")

        if sender in accounts and receiver in accounts:
            amount = float(input("Enter transfer amount: "))
            accounts[sender].transfer(accounts[receiver], amount)
        else:
            print("Account not found")

    elif choice == "5":

        acc_no = input("Enter account number: ")

        if acc_no in accounts and isinstance(accounts[acc_no], SavingsAccount):
            accounts[acc_no].apply_interest()
        else:
            print("Savings account not found")

    elif choice == "6":

        acc_no = input("Enter account number: ")

        if acc_no in accounts:
            accounts[acc_no].display()
        else:
            print("Account not found")

    elif choice == "7":
        print("Exiting system")
        break

    else:
        print("Invalid choice")