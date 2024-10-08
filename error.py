# error 1.
#print(x)

#error handling.
x=2
try:
   print(x)
except NameError:
    print("'x' is not defined")
    
# error 2.
# y=1/0   
try :
    y=1/0
except ZeroDivisionError:
    print("divide by zero")
    
# error 3.
name = "pawan"
# no= int(name) 
try:
   no=int(name)
except ValueError:
    print("str cannot convert into int.")         
    
# error 4.
friends= ["payal","riya","harshika"]
# friends[4]
try:
    friends[4]
except IndexError:
    print("you are calling wrong index.")
    
# error 5.
amount=500
email="p@gmail.com"
# total=amount+email            
try:
    total=amount+email
except TypeError:
    print("unsupported operands types.")    
    

    