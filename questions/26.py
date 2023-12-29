# Define a BankClient that represent each of the bank client concept.
# Each of the bank client has a name, account_number, balance. Also, 
# each of them are able to deposit(self, amount) and withdrawal(self, amount).
# Be careful to check if the withdrawal amount is greater than the balance of
# the client, reject the request.

class BankClient:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        print(("A new BankClient is created for %s with " + 
              "initial balance of %d.") % (self.name, self.balance))

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.print_action("deposit", amount)

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            self.print_action("withdrawal", amount)
        else :
            print("The action was withdrawal, but the balance is insufficient!")

    def print_action(self, action_name, amount):
        print("The action was %s with amount of %d." % (action_name, amount))
        self.print_balance()
    
    def print_balance(self):
        print("Your balance is %d." % self.balance)

amirali = BankClient("AmirAli Motameni", 6104, 100)
amirali.withdrawal(50)
amirali.deposit(33)
amirali.withdrawal(100)

ali = BankClient("Ali Motameni", 5505, 1000)
ali.withdrawal(1000)
