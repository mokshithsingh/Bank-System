class Account :

    def __init__(self, owner, balance=0) : 

        self.owner = owner 
        self.balance = balance

    def __str__(self) : 

        return f"Account Owner : {self.owner}, Balance : {self.balance}"
    
    def deposit(self, amount) : 

        self.balance += amount 

        print(f"₹{amount} deposited successfully! New balance : {self.balance}")
    
    def withdraw(self, amount) : 

        if self.balance >= amount : 

            self.balance -= amount 

            print(f"₹{amount} withdrawn successfully! New balance : {self.balance}")
        
        else : 

            print(f"Insufficient funds!")


class Bank : 

    def __init__(self) : 

        self.account_data = {}

    def create_account(self, owner, balance=0) :

        self.account_data[owner] = Account(owner, balance)

        print(f"Account created successfully! \n Owner : {owner}, Balance : {balance}")

    def delete_account(self, owner) : 

        if owner in self.account_data : 

            del self.account_data[owner]

        else : 

            print(f"There is no account with the owner name '{owner}' in this bank")

    def show_all_accounts(self):

        for name, account in self.account_data.items():

            print(f"{name} : ₹{account.balance}")

    
    def account_check(self, owner) : 
        
        return owner in self.account_data

    def show_balance(self, owner) : 

        if self.account_check(owner) : 

            print(self.account_data[owner])

        else : 

            print(f"There is no account with the owner name '{owner}' in this bank")

    def deposit_to_account(self, owner, amount) : 

        if self.account_check(owner) : 

            self.account_data[owner].deposit(amount)

        else : 

            print(f"There is no account with the owner name '{owner}' in this bank")

    def withdraw_from_account(self, owner, amount) : 

        if self.account_check(owner) : 

            self.account_data[owner].withdraw(amount)

        else : 

            print(f"There is no account with the owner name '{owner}' in this bank")