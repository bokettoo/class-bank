import random

class BankAccount:
    def __init__(self):
        self.Account = {}
        self.Client = {}
        self.CustomerCompte = {}

    def generateAccountNum(self, numCl):
        randomNum = random.randint(0, 100)
        accountNum = numCl + randomNum
        return accountNum

    def addClient(self, numCl, MPC, numC, BalanceC):
        if numCl in self.Client:
            print("Customer number already exists")
            return

        accountNum = self.generateAccountNum(numCl)
        self.Client[numCl] = MPC
        self.CustomerCompte[numC] = accountNum
        self.Account[accountNum] = BalanceC
        print("Account successfully created for customer number", numCl)
        print("Account number:", accountNum)

    def DeleteClient(self, numC):
        if numC not in self.CustomerCompte:
            print("Account does not exist for the specified customer number")
            return

        accountNum = self.CustomerCompte[numC]
        del self.Account[accountNum]
        del self.Client[numC]
        del self.CustomerCompte[numC]
        print("Account successfully deleted")

    def ModifyMPClient(self, numC, newMP):
        if numC not in self.CustomerCompte:
            print("Account does not exist for the specified customer number")
            return

        self.Client[numC] = newMP
        print("Secret code successfully updated")

    def Deposit(self, numC, amount):
        if numC not in self.CustomerCompte:
            print("Account does not exist for the specified customer number")
            return

        accountNum = self.CustomerCompte[numC]
        currentBalance = self.Account[accountNum]
        updatedBalance = currentBalance + amount
        self.Account[accountNum] = updatedBalance
        print("Deposit of", amount, "successful. Your current balance is", updatedBalance)

    def Withdraw(self, numC, amount):
        if numC not in self.CustomerCompte:
            print("Account does not exist for the specified customer number")
            return

        accountNum = self.CustomerCompte[numC]
        currentBalance = self.Account[accountNum]

        if amount > currentBalance:
            print("Insufficient funds. Your current balance is", currentBalance)
            return

        updatedBalance = currentBalance - amount
        self.Account[accountNum] = updatedBalance
        print("Withdrawal of", amount, "successful. Your current balance is", updatedBalance)
