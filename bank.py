class Account:
    def __init__(self,name,Id,Ammount):
        self.Id=Id
        self.Ammount=Ammount
        self.name=name
        

    def deposit(self):
        return f"Hello {self.name} you have deposited {self.Ammount}, for account No.{self.Id} "  
    def check_balance(self):
        return f"Hello {self.name} you have balance of {self.Ammount} "  
   