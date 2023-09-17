class BanckAccount:
  def __init__(self,account_number,accountholder_name,ini_balance=0.0):
    self.__account_number=account_number
    self.__accountholder_name= accountholder_name
    self.__account_balance= ini_balance
  def deposit(self,amonut):
    if amount==0:
      self.__account_balance+=amount
      print("money deposited is  ₹{} , new balance is ₹{}".format(amount,self.__account_balance))
    else:
      print("Invalid amount")
  def withdraw(self, amount):
    if amount >0 and amount<= self.__account_balance:
      self.__account_balance-= amount
      print("Withdrawed money is ₹{} and current balance is ₹{} ".format(account,self.__account_balance,))
    else:
      print("Invalid to withdraw")
  def account_disply(self):
    print("Account balance for {} (Account #(): ₹{}".format(self.__accountholder_name,self.__account_number,self.__account_balance))

account=BanckAccount(account_number="7230223450",
                    accountholder_name="Jaya",
                    ini_balance=7000.0)

account.account_disply

account.withdraw(3000.0)