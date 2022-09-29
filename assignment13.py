#1. Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using list
l = ["Java","Python", "SQL", "C"]
print(l)

#2. Write a python script to get the data type of a list.
l = ["Java","Python", "SQL", "C"]
print(type(l))

#3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
mylist = ["Java", "C", "Python"]
print(mylist[2])

#4. Write a python script to Change the values "SQL" and "Reactnative" with the values "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
thislist[1] = "NoSQL"
thislist[3] = "Flutter"
print(thislist)

#5. Write a python script to add an item to the end of the list (item “Python”. (mylist = ["Java", "SQL", "C", "Reactnative"]
mylist = ["Java", "SQL", "C", "Reactnative"]
mylist.append("dot net")
print(mylist)

#6. Write a python program to append elements from another list to the current list.(firstlist = ["Java", "Python", "SQL"] secondlist = ["C", "Cpp", "NoSQL"] )
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
finallist = firstlist + secondlist
print(finallist)

#7. Write a python program to Print all items by referring to their index number (thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

for i in range(5):
    print(i,thislist[i])
    
#8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]
thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]
thislist.sort()
print(thislist)

#9. Write a Python script to create a list of city names taken from the user.
print("number of cities you want to enter ")
n = int(input())
print("enter different cities name ")

l4 = []
i=0
while i<n :
    l4.append(input())
    i+=1
    print(l4)
      

#10. Write a Python script to create a list, where each element of the list is a digit of a given number.
print("enter the number")
l4 = list(input())
print(l4)

