#1. Write a python program to create a simple function which prints “MySirG” .
def myfun():
    a="MySirG\n"
    a*5
    print(a*5)


myfun()

#2. Write a python program to create a function which expects two arguments and print them in the function body.
def greet(name, msg):
    print("Hello", name + ', ' + msg)

greet("Monica", "Good morning!")
#3. Write a python program to create a function which expects an unknown number ofarguments.
def mult(*args):
    ans = 1
    for i in args:
        ans *= i
    print(ans)
mult(1,2,3,4)
#4. Write a python program to create a function which expects kwargs arguments.
def myFunction(**kwargs):
    for kw in kwargs:
        print(kw, '-', kwargs[kw])

if __name__ == "__main__":
    myFunction(a = 24, b = 87, c = 3, d = 46)
#5. Write a python program to create a function which expects a list as an argument.
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
#6. Write a python program to create a function that finds a maximum of four numbers.
lst = []
 
num = 4
 
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
     
print("Maximum element in the list is :", max(lst))

#7. Write a python program to sum all the numbers in a list.
list1 = [11, 5, 17, 18, 23]


def sumOfList(lst, size):
    if size == 0:
        return 0
    else:
        return lst[size - 1] + sumOfList(lst, size - 1)


total = sumOfList(list1, len(list1))

print(total)
#8. Write a python program to multiply all the numbers in a list.
 
def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result
 
 
# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))
#9. Write a python program to create a function to check whether a number falls in agiven range.
def test_range(n):
     if n in range(3,9):
       print( " %s is in the range"%str(n))
     else :
       print("The number is outside the given range.")
test_range(5)
#10. Write a python program to create a function to check whether a given number is even or odd.
def CheckEvenOdd(num): 
  if (num % 2 == 0): 
    print(num," is EVEN")
  else: 
    print(num," is ODD")
    
CheckEvenOdd(6)
