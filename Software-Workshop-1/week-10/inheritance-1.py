class BankAccount:
    def __init__(self, owner, balance, currency):
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def print_balance(self):
        print("Your current balance is:")
        print(self.balance)

    def make_deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Please enter a valid amount.")

    def make_withdrawal (self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("You don't have enough funds to make this withdrawal.")

    
class SavingsBankAccount(BankAccount):
    INTEREST_RATE = 0.035

    def __init__(self, owner, balance, currency):
        BankAccount.__init__(self, owner, balance, currency)
        self.interest_rate = SavingsBankAccount.INTEREST_RATE

    def deposit_interest_earned(self):
        interest_earned = self.balance * SavingsBankAccount.INTEREST_RATE
        self.balance += interest_earned


class CheckingBankAccount(BankAccount):
    def __init__(self, owner, balance, currency, debit_card=None, credit_card=None):
        super().__init__(owner, balance, currency)
        self.debit_card = debit_card
        self.credit_card = credit_card

print("SavingsBankAccount class:")
my_savings_account = SavingsBankAccount("Jon Smith", 45600, "GBP")
my_savings_account.print_balance()
my_savings_account.make_deposit(5000)
my_savings_account.make_withdrawal (200)
my_savings_account.deposit_interest_earned()
my_savings_account.print_balance()
print(my_savings_account.owner)
print(my_savings_account.currency)

print("\nCheckingBankAccount class:")

my_checking_account = CheckingBankAccount("Jon Smith", 67899, "USD")
my_checking_account.print_balance()
my_checking_account.make_deposit(4000)
my_checking_account.make_withdrawal(100)
my_checking_account.print_balance()
print(my_checking_account.owner)
print(my_checking_account.currency)


