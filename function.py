# list can store mul.data and data can be diff type like int str float.
# list can store the duplicate data.
# list is an ordered data set-> sorting ascending and desending

# create list and store the your friends name.
friendlist=["ivan","anshu","anjali","vani"] 
          
print(friendlist)  #print this names
# add the age of your friends into list.
# append will add the data into end of the list.
friendlist.append(16) 
friendlist.append(34)
friendlist.append(17) 
friendlist.append(56)
print(friendlist)      

# add the data into list using index no.
friendlist.insert(0,"payal")
print(friendlist)

#to access the data using index no.
print(friendlist[0]) 

#to delete the data from list.
friendlist.remove("ivan")
print (friendlist)
# remeove will deleye the data using value. 
friendlist.remove("payal")
print("payal")
# pop will delete the data using index.
friendlist.pop(3)
print(friendlist)
friendlist.remove("anshu")
print(friendlist)
#access the complete list.
# for name in friendlist:
#     print(name)
friendlist.sort()
#add the 5 favt city name in list.
#add any fav city kasol in index 0.
#remove the last city in list.-> using pop.
#sorting the list data.
#print the list data.