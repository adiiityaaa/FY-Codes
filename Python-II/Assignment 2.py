class BankAccount:
    def __init__(self, acc_no, name, acc_type, bal=0):
      self.acc_no = acc_no
      self.name = name
      self.acc_type = acc_type
      self.bal = bal

    def deposit(self, amount):
        if(amount>0):
            self.bal = self.bal + amount
            print("Deposited " + str(amount) + " to your account. New Balance: " + str(self.bal))
        else:
            print("The deposit amount cannot be negative.")

    def withdraw(self, amount):
        if(amount > self.bal):
            print("The withdrawal amount cannot be greater than current bank balance.")
        else:
            self.bal = self.bal - amount
            print(str(amount) + " has been withdrawen from your bank account. New Balance: " + str(self.bal))
           
    def checkbal(self):
        print("Your bank balance is: " + str(self.bal))
       
    def viewacc(self):
        print("Account Details:\nAccount Holder: " + self.name + "\nAccount Number: " + str(self.acc_no) + "\nAccount Type: " + self.acc_type + "\nCurrent Balance: " + str(self.bal))

def main():
    name = input("\nEnter Account Holder Name: \n")
    acc_no = input("\nEnter Account Number: \n")
    acc_type = input("\nEnter Account Type: \n")
    account = BankAccount(acc_no, name, acc_type, bal=0)
    while True:
      print("\n\nAvailable Options: \n1. View Account Information\n2. Deposit Money\n3. Withdraw Money\n4. View Balance\n5. Exit")
      option = int(input("Select your choice: \n"))
      if(option == 1):
        account.viewacc()
      elif(option == 2):
        val=int(input("\nEnter the amount to deposit: \n"))
        account.deposit(val)
      elif(option == 3):
        val=int(input("\nEnter the amount to withdraw: \n"))
        account.withdraw(val)              
      elif(option == 4):
        account.checkbal()
      elif(option == 5):
        print("Have a nice day.")
        break
      else:
        print("Please enter a valid option.")              

main()
