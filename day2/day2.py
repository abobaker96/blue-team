my_num =[]
d =[x for x in range(21) if x%2==0]
#print(d)

# class Person:
#     def __init__( self, name, year_old, city):
#         self.name= name
#         self.year_old= year_old
#         self.city = city
#     def greet(self):
#        # print(f"name {self.name} year old {self.year_old} city {self.city}")


# p = Person("abobaker" , 29 , "hoon" )
#p.greet()

class Bank:
    def __init__(self,owner, balance=200):
        self.owner =owner
        self.balance =balance
    def withdrow(self,withdraw):
        if withdraw>self.balance:
            raise ValueError()
        self.ba=self.owner-withdraw
            
    def deposit(self,deposit):
        self.balance=self.balance+deposit
    print("owner{self.owner} balance{self.balance} ")


A1= Bank("abobaker")   
A1.deposit(100)
print(A1.balance)
    

        











