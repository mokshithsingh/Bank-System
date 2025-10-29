class Account():

    accounts = {}

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

        Account.accounts[owner] = self

    def deposit(self):

        amount = input("Enter the amount you want to deposit : ")

        while not amount.isdigit():

            amount = input("Please enter a valid amount : ")

        amount = int(amount)

        self.balance += amount

        print("Deposit succesful!")

        self.display_balance()

    def withdraw(self):

        amount = input("Please enter the amount you want to withdraw : ")

        while not amount.isdigit():

            amount = input("Please enter a valid amount : ")

        amount = int(amount)

        while amount > self.balance:

            print("Insufficient balance")

            print('\n')

            amount = int(
                input("Please enter the amount you want to withdraw : "))

        self.balance -= amount

        print(f"Here's your money {amount}")

        self.display_balance()

    @classmethod
    def transactions(cls):

        name = input("Please enter your name : ")

        while not name in Account.accounts:

            name = input("Please enter the name of the owner : ")

        account = Account.accounts[name]

        choice_2 = input("What do you want to do ( Deposit or Withdraw )? : ")

        while choice_2.capitalize() not in ("Deposit", "Withdraw"):

            print("Invalid input")

            choice_2 = input(
                "What do you want to do ( Deposit or Withdraw )? : ")

        if choice_2.capitalize() in "Deposit":

            account.deposit()

        if choice_2.capitalize() in "Withdraw":

            account.withdraw()

    def display_balance(self):

        choice = input(
            "Do you want your balance to be displayed on the screen ( Y or N )? : ")

        if choice.upper() in "Y":

            print(f"Here's your balance {self.balance}")
