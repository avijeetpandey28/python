#1. Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using tuple
tuple1 = ("Java" , "Java" , "Python" , "SQL" , "C")
print(tuple1)

#2. Write a python program to store only one item using tuple.
a=(10,)
print(type(a))

#3. Write a python program to reverse the tuple.
tuple2 = (10 , 20 , 30 , 40 , 50)
print(tuple2[::-1],type(tuple2))
print()

#4. Write a python program to Swap two tuples in Python.
tup_1 = ('hello', 'world')
tup_2 = (1, 2, 3)
print(tup_1, tup_2)

tup_1, tup_2 = tup_2, tup_1
print(tup_1, tup_2)


#5. Write a python program to check if all items in the tuple are the same.
x = (True, True, True)
result = all(x)
print(result)

#6. Write a python program to divide the tuple into four variables. tuple1= (100, 200, 300, 400)
tuple1 = (100, 200, 300, 400)

# unpack tuple into 4 variables
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)

#7. Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6)
tuple1=(1,2,3,4,5,6)

tuple2=tuple1[3:-1]
print(tuple2)

#8. Write a python program to Sort a tuple of tuples by the second item. tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)s

#9. Write a python program to print the value 20 from given nested tuple tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple1[1][1])

#10. Write a python program to change the first item (22) of a list within the following tuple to 222.
tuple1 = (11, [22, 33], 44, 55)
tuple2=list(tuple1)
tuple2[1][0]=222
tuple1 = tuple(tuple2)
print(tuple1)
