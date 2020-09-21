class Accounts:
    """ This class will simulate a Bank Account """
    def __init__(self, first='', last='', intial=0.0):
        """ Initializes the Users bank information"""
        self.firstname = first
        self.last = last
        self.balance = float(intial)

    def __str__(self):
        """ A string representation of the data that will be collected by input """

        return "( {0}, {1}, {2})".format(self.firstname, self.last, self.balance)

    def deposit(self):
        """ The user will be able to deposit/add money to their balance"""

        amount = input("How much more money would you like to deposit? ")
        self.balance += float(amount)
        print("You have deposited $",amount,", your balance is $", self.balance)
        return self.balance

    def withdraw(self):
        """ The user will be able to withdraw/remove money from their balance"""

        while True:
            amount = input("How much money would you like to withdraw? ")
            if float(amount) > self.balance:
                print("You have withdrawn more then you have in your your account, please try again")
            else:
                self.balance -= float(amount)
                print("You have withdrawn $",amount,", your balance is $", self.balance)
                return self.balance

    def fee(self):
        """ Will determine if a fee is necessary when the user has more then $10 and less then 1000 """

        fees = 10
        if self.balance > 10.0 and self.balance < 1000.0:
            self.balance -= fees
            print(" Your balance now is $", self.balance, "due to having less than $1000, which initiates a fee of $10")
            return self.balance
        else:
            print("You will have no fees this month")

    def interest(self):
        """ The user will be able to determine how much interest they will receive after this transaction"""

        inter = 0.03 * self.balance
        print("The interest you will accumulate this month will be $", inter)
        return inter


firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
intialD = float(input("What would you like to initially deposit? "))
r = Accounts(firstName, lastName, intialD)
print(r)
print("Your balance is $", r.balance)
r.deposit()
r.withdraw()
r.fee()
r.interest()
print("Have a great day!")
