#1. Write a Python script to create a list of first N natural numbers.
n= int(input("enter the natural number"))
l = list(range(1,n+1))
print(l)

#2. Write a Python script to create a list of first N odd natural numbers.
n= int(input("enter the natural number"))
l = list(range(1,n+1,2))
print(l)
#3. Write a Python script to create a list of first N even natural numbers.
n= int(input("enter the natural number"))
l = list(range(2,n+1,2))
print(l)
#4. Write a Python script to find the greatest number in a given list of numbers.
l = [1,2,3,4,5,6,78,9]
print(max(l))

#5. Write a Python script to find the smallest number in a given list of numbers.
l = [1,2,3,4,5,6,78,9]
print(min(l))

#6. Write a Python script to calculate the sum of elements in a given list of numbers.
l = [1,2,3,4,5,6,8,9]
print(sum(l))

#7. Write a Python script to remove all non int values from a list.

# initializing list
test_list = [1, None, 4, None, None, 5, 8, None]
 
# printing original list
print ("The original list is : " + str(test_list))
 
# using naive method
# to remove None values in list
res = []
for val in test_list:
    if val != None :
        res.append(val)
 
# printing result
print ("List after removal of None values : " + str(res))

#8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
l = [1,2,3,4,5,6,8,9,1,3,4,4,4,6,7,7]
print(l.count(4))

#9. Write a Python script to print indices of all occurrences of a given element in a given list.
l1 = [1, 5, 1, 8, 9, 15, 6, 2, 1]
pos = []
x = 1 #The required element

for i in range(len(l1)):
   
        pos.append(i)
print(pos)

#10. Write a python script to sort a list.
l = [1,2,3,4,5,6,8,9,1,3,4,4,4,6,7,7]
print(sorted(l))
