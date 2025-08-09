#Create an empty lis
my_list = []
#Append values into an empty list which is my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#Print for comfirmation
print(my_list)


#Insert a value at the second position of my_list
my_list[1]=15
#Print to display the results
print(my_list)


#Extend my_list list with another list
#Create new list
my_list_2 = [50,60,70]
my_list.extend(my_list_2)
#print to see the results
print(my_list)


#Remove the last element from the list
my_list.pop()
#Print for the current results
print(my_list)


#Sort a list in ascending order
my_list.sort(reverse=False)
#Print the results
print(my_list)

#Print only the index of value 30 from my_list
index_value = my_list.index(30)
print(index_value)