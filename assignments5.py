#Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)
number = int(input("enter a number: "))
number = int(number/10)
print("new value of number: ")
print(number)

#2Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)

number = int(input("enter a number: "))
number = int(number%10)
print("new value of number: ")
print(number)

#3Write a python script to swap data of two variables
number_1 = int(input("enter a number: "))
number_2 = int(input("enter a number: "))
okay = number_1
number_1 = number_2
number_2 = okay
print("new value of number_1: ")
print(number_1)
print("new value of number_2: ")
print(number_2)

#4 Write a python script to find x power y, where values of x and y are given by user
number = int(input("enter the number: "))
power = int(input("enter the power: "))
result = number ** power
print(result)

#5 Write a python script which takes a three digit number from the user and displays only its first digit.
number = int(input("enter a three digit number: "))
number = int(number/100)
print("new value of number: ")
print(number)

#6 Write a python script which takes a three digit number from the user and displays only its middle digit.
number = int(input("enter a three digit number: "))
number = int(number/10)
newnumber = number%10
print(newnumber)

#8. Write a python script to use IN operator to display the data present in the list
number = int(input("enter number: "))
list_1 = [0,3,4,5,2]
print(number in list_1)

#9. Write a python script to use NOT IN operator to display the data not present in list
number = int(input("enter number: "))
list_1 = [0,3,4,5,2]
print(number not in list_1)

#10. Write a python script to use IS operator to display if both variables are the same object or not?

list_1 = [0,3,4,5,2]
list_2 = [0,3,4,5,2]
print(list_1 is list_2)
print(list_1 == list_2)
