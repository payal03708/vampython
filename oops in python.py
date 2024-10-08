#oops in python. object oriented programing-->object
#class--it is a container which collects variable, functions
#e.g.-payal class
#payal.fullname="payal"
#payal.sleeping()
#payal.watching()
#payal.eating()
#class syntax.
class className:
    print("this is my class")
    
class Payal:
    age=19
    fullName="Payal bhardwaj"
    email="p@gmail.com"
    def pocketMoney(this,amount):
       print("my pocket money is ",amount)
       
#crate class object.
payal:Payal=Payal()
payal.pocketMoney(15000)
print(payal.fullName,payal.age,payal.email)

       
       