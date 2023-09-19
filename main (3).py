class BankAccount:

  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
   self._account_number = account_number
  self._account_holder_name=account_holder_name
  self._account_balance =initial_balance 
def deposit(self,amount ):
  if amount >0:
    self._account_balance +=amount 
    print("deposited ₹{}.new balance:₹{}".format (amount,self._account_balance )) 
else:  
print("Invalid deposit amount.please deposit a positive amount. ")
    def withdraw(self,amount ):
      if amount >0 and amount <=self.__account_balance -= amount 
      print("withdraw ₹{}.New balance:₹{}".format(amount,self__account_balance))
  else:
    print("invalid withdrawal amount or insufficient balance  ")
    def display_balance (self ):
      print ("account balance for{}(account #{}):".format(
        self__account_holder_name,self.__account_number,
        self__account_balance))
      #create an instance of the BankAccount class
      account=BankAccount(account_number ="123456789",
                account_holder_name="keerthika",
                         initial_balance=5000.0)
      #Test deposit and withdrawal functionality 
      account.display_balance ()
      account.deposit(500.0)
      account.withdrawal(200.0)
      account.display_balance()
      
                      
      
    