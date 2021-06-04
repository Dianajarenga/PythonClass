class Account:
    def __init__(self,name,phone,limit):
        self.phone=phone
        self.balance=0
        self.name=name
        self.limit=limit
        

    def deposit(self,amount):

        if amount<=0:
            return f"The amount must be greater than zero"
        else :  
            self.balance+=amount  
            return f"Dear {self.name} you have deposited {amount}, for account No 222 your balance is {self.balance} " 
         
    def show_balance(self):
        return self.balance
        
        #adding functionality
        # 
        #  
    def withdraw(self,amount):
    
        if amount>0:
             
            return f"Dear {self.name} you have withdrawn {amount}, for account No 222 your balance is {self.balance} " 
        elif amount<=0:
            return f"Amount must be greater than zero"

        elif amount>self.balance :

            return f"Amount must be less than balance"
        else :
            self.balance-=amount 
            return f"{self.balance}"


    def borrow(self,amount):
        if amount>self.limit:
           print(f"Above loan limit ,please select a lower amount")
        elif self.loan>0:
          print(f"you have an outstanding debt")
        else:
          self.loan+=1
          self.balance+=amount
          return f"loan Successful"



