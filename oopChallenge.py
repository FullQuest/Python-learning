class Account():

    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.balance = balance

    def __str__(self):
        return f'Account owner:\t {self.owner_name}\nAccount balance: ${self.balance}'

    def deposit(self, deposit_sum):
        self.balance += deposit_sum
        print(f'Deposit ${deposit_sum} accepted')

    def withdraw(self, withdraw_sum):
        if withdraw_sum > self.balance:
            print(f'Withdraw ${withdraw_sum} denied. Withdraw sum is more than balance.\nUse lower value to withdraw')
        else:
            self.balance -= withdraw_sum
            print(f'Withdrawal ${withdraw_sum} accepted')


# 1. Instantiate the class
acct1 = Account('Jose', 100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
acct1.owner_name

# 4. Show the account balance attribute
acct1.balance

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
