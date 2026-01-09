# Create a class BankAccount
class BankAccount: # Represents Bank Account
    # Class Attributes
    BankName = "State Bank Of India"
    BranchName = "KK Nagar"

    def __init__(self, AccountNo, AccountHolderName, InitialBalance=0):
        #Instance Attributes
        self.AccountNo = AccountNo
        self.AccountHolderName=AccountHolderName
        self.__Balance = InitialBalance
        # if InitialBalance == 0:
        #     print("Initial Balance cannot be 0")
        # else:
        #     self.__Balance=InitialBalance

    def PrintBalance(self):
        return(self.__Balance)

    def PrintAccountDetails(self):
        print(f"Account No.: {self.AccountNo}")
        print(f"Account Holder Name: {self.AccountHolderName}")
        print(f"Present Balance: {self.__Balance}")

    def deposit(self, amount):
        if amount < 0:
            print("Amount deposited must be positive")
        else:
            self.__Balance = self.__Balance + amount
        print(f"After depositing Rs{amount}, Account Balance is {self.__Balance}")

    def withdrawal(self, amount):
        self.__Balance = self.__Balance - amount
        if self.__Balance < 0:
            self.__Balance = self.__Balance + amount
            print("Balance cannot be negative")
        print(f"Present Balance after withdrawal of Rs{amount} is {self.__Balance}")

class SBAccount(BankAccount):
    AccountType="SavingsBank"

    def __init__(self, AccountNumber, AccountHolder, InitialBalance):
        self.RoI = 6
        super().__init__( AccountNumber, AccountHolder, InitialBalance)

    def PrintAccountDetails(self):
        print(f"Account Type: self.AccountType")
        print(f"Rate Of Interest: {self.RoI}")
        super().PrintAccountDetails()

    def CalInterest(self):
        interest = self.__Balance * self.RoI % 100
        self.__Balance += interest
        self.PrintBalance()

class CurrentAccount(BankAccount):
    AccountType="CurrentAccount"

    def __init(self, AccountNo, AccountHolderName, InitialBalance=0):
        super().__init__(AccountNo, AccountHolderName, InitialBalance)
        # if InitialBalance == 0:
        #     self.AccountNo = AccountNo
        #     self.AccountHolderName = AccountHolderName
        #     self.__Balance = 0
        # else:
        #     super.__init__()

    def CurrWithdrawal(self, WithdrawalAmount):
        BalAfterWithDrawal = self.__Balance - WithdrawalAmount
        if BalAfterWithDrawal < 500:
            print(f"Error Withdrawing Amount {WithdrawalAmount} and would result in penalty if you continue ")
        else:
            self.__Balance = BalAfterWithDrawal


BA1 = BankAccount("BA1", "BA1Holder", 500)
TempBal=BA1.PrintAccountDetails()
SBBA1 = SBAccount("SBA1", "SBA1Holder", 500)
SBBA1.PrintAccountDetails()
CABA1 = CurrentAccount("CABA1", "CA1Holder", 0)
CABA1.PrintAccountDetails()

SBBA1.deposit(1200)
SBBA1.withdrawal(300)
SBBA1.withdrawal(1500)
CABA1.deposit(1000)
CABA1.withdrawal(250)