from datetime import datetime



class Account:
    def __init__(self,name,phone,limit):
        self.phone=phone
        self.balance=0
        self.name=name
        self.limit=limit
        self.transaction=[]
        

    def deposit(self,amount):

        if amount<=0:
            return f"The amount must be greater than zero"
        else :  
            self.balance+=amount  
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Deposit"}
            self.transaction.append(transaction)
    
            return f"Dear {self.name} you have deposited {amount}, for account No 222 your balance is {self.balance} " 
         
    def show_balance(self):
        return self.balance
        
        #adding functionality
         
    def withdraw(self,amount):
    
        if amount>0:
             
            return f"Dear {self.name} you have withdrawn {amount}, for account No 222 your balance is {self.balance-amount} " 
        elif amount<=0:
            return f"Amount must be greater than zero"

        elif amount>self.balance :

            return f"Amount must be less than balance"
        else :
            self.balance-=amount   
            transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Deposit"}
            self.transaction.append(transaction)
    
            return f"{self.balance}"


    def borrow(self,amount):
        if amount>self.limit:
           print(f"Above loan limit ,please select a lower amount")                
        elif self.loan>0:
          print(f"you have an outstanding debt")
        else:
          self.loan+=1
          self.balance+=amount
          transaction={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"Deposit"}
          self.transaction.append(transaction)
    
          return f"loan Successful you have received amount {amount} your new balance is"

    def get_statement(self):
        for transactions in self.transaction:
            narration=transactions["narration"]
            amount=transactions["amount"]
            balance=transactions["balance"]
            time=transactions["time"]
            print(f"{time.strftime('%D')},{narration},amount{amount},balance{balance}")

    def loan_repayment(self,amount):

        if amount>=self.loan:
            return f"you have paid {amount},your new balance{amount-self.loan}"
        elif amount<self.loan:
            return f"you have a pending loan of { self.loan- amount} to pay"
        else:
            return f"you dont have a pending loan"
        


#Transaction,Amount,Balance,Time,Code/id,Narration,
#add empty list to have a place to store transactions
#self.transactions=[]
#use dictionery to capture sttributes and append to self. transtactions    >>> now.strftime("%d-%m-%Y")



