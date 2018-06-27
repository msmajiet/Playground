class BankAccount(object):
    def __init__(self):
        self.accountid = ""
        self.balance = 0.00


    def openSavingsAccount(self,accountid,amounttodeposit):
        if (amounttodeposit > 1000.00):
            self.accountid = accountid
            self.balance = amounttodeposit
        else:
            raise ValueError("Insufficient deposit amount")
        
    def openCurrentAccount(self,accountid):
        self.accountid = "C" + str(accountid)
        self.balance = 0.00
        # Implement Overdraft

    def withdraw(self, accountid, amounttowithdraw):
        accountid = str(accountid)
        print ("This is a current account",accountid[0])

        if (accountid[0]== "C"):
            #Allow for Overdraft
            print ("This is a current account")
        if amounttowithdraw > self.balance:
            raise ValueError("Withdrawal Amount too Large")
        self.balance -= amounttowithdraw
        
    def deposit(self, accountid, amounttodeposit):
        self.balance += amounttodeposit
              
    def printBalance(self):
        print("balance",self.balance,"accountid",self.accountid)

def main():
    c1 = BankAccount()
    c1.openSavingsAccount(12345,1100)
    c1.printBalance()
    c1.deposit(12345,200)
    c1.printBalance()
    c1.withdraw(12345,200)
    c1.printBalance()
    
    c2 = BankAccount()
    c2.openCurrentAccount(3456)
    c2.printBalance()
    c2.deposit(3456,250)
    c2.printBalance()
    c2.withdraw(3456,150)
    c2.printBalance()

if __name__ == "__main__":
    main()
