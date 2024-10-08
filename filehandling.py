# create file for saving my laptop password.
# open func. will create the file when file is note exists and write the file.
myPassword= open("myPassword.txt","w")

#write my laptop password
myPassword.write("mypassword-payal")

#over write the new password using input
# myPassword.write(input("mynewpassword is:"))

#read the password from file.
myPassword = open("myPassword.txt","r")
print(myPassword.read())

#read the password of file.
myPassword=open("myPassword.txt","r")
mydata = myPassword.read()
if "macbook" in  mydata:
    print("yes")
else:
    print("no") 
#to close tghe file.       
myPassword.close()    
    
# #delete the file.
import os 
os.remove("myPassword.txt")

#create read write delete csv,excel,json,txt.
myCsv= open("myFile.csv","w")
myCsv.write("payal,mahi,anali,saloni,harshika")

myexcel=open("myexcel.xlsx","w")
myexcel.write("name,anjali,payal,harshika")