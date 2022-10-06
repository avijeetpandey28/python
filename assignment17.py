#1. Write a python program to store all the programming languages known to you using Set.
thisset = {"Python", "c", "JavaScript","c++","SQL"}
print(thisset)
#2. Write a python program to store your own information {name, age, gender, so on..}
my_info = {"avijeet",27,"male","jnu"}
print(my_info)
#3. Write a python script to get the data type of a Set.
s3={"Python", "Django", "JavaScript", "SQL"}
print(type(s3))

#4. Write a Python script to find if “Python” is present in the set this set = {"Java", "Python", "Django"}
this_set = {"Java", "Python", "Django"}
print("Python"in this_set)

#5. Write a python program to add items from another set to the current set. this set ={"Java", "Python", "SQL"}  secondset= {"C", "Cpp", "NoSQL"}
thisset ={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
for e in secondset:
    thisset.add(e)
print(thisset)

#6. Write a python program to add elements of list to a set this set = {"Python", "Django", "JavaScript"} mylist = ["Java", "C"]
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
thisset.update(mylist)
print(thisset)

#7. Write a python program to remove last item of the given set this set = {"Python", "Django", "JavaScript", “SQL”}
s = {"Python", "Django", "JavaScript", "SQL"}
s.remove("SQL")
print(s)

#8. Write a python program to delete the set completely.
s3 = {"Python", "Django", "JavaScript", "SQL"}
del(s3)


#9. Write a python program to loop through the set and print values this set = {"Python", "Django", "JavaScript", “SQL”}
s3 = {"Python", "Django", "JavaScript", "SQL"}
for e in s3:
    print(e)
#10. Write a python program to find the maximum and minimum value in a set.

s2 = {10,2,8,10,40,8}
print(max(s2))
print(min(s2))
