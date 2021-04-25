class bank :
    bal=1000
    def deposit(selfself,am):
        self.bal=self.bal+ am
        print("after deposit:", self.bal)
    def withdrawl(self,am):
        if(am>self.bal):
            print("insufficeint amount")
        else:
            self.bal=self.bal-am
            print("after withdrwal amount:",self.bal)
    def amount(self):
            print("total amount is:", self.bal)
v=True
b=bank()
b.amount()
while(v):
    n=input("1 for deposit , 2 for withdrawl,3 for exit:")
    if(n=="1"):
        a=int(input("enter amount:1"))
        b.deposit(a)
    elif(n=="2"):
        a=int(input("enter amount:"))
        b.withdrawl(a)
    elif(n=="3"):
        print("thanks for visit")
        v=False
    else:
        print("invalid please try again")
