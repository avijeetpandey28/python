#1. Write a recursive python function to calculate sum of first N natural numbers
def sumn(n):
    if n==1:
        return(1)
    s = sumn(n-1)+n
    return s

print(sumn(5))

#2. Write a recursive python function to calculate sum of first N odd natural numbers
def sumn(n):
    if n==1:
        return(1)
    return ((2*n)-1) + sumn(n-1)

print(sumn(3))
    
#3. Write a recursive python function to calculate sum of first N even natural numbers
def sumn(n):
    if n==1:
        return(2)
    return (2*n) + sumn(n-1)

print(sumn(8))
#4. Write a recursive python function to calculate sum of squares of first N natural numbers
def sumn(n):
    if n==1:
        return 1
    return (n**2) + sumn(n-1)

print(sumn(4))
#5. Write a recursive python function to calculate sum of cubes of first N natural numbers
def sumn(n):
    if n==1:
        return 1
    return (n**3) + sumn(n-1)

print(sumn(4))
#6. Write a recursive python function to calculate the factorial of a number.
def fact(n):
    if n==0:
        return 1
    return (n*fact(n-1))

print(fact(4))
#7. Write a recursive python function to calculate sum of the digits of a given number
tot = 0
def calcSOD(Num):
    global tot
    if(Num > 0):
        Reminder = Num % 10
        tot = tot + Reminder
        calcSOD(Num //10)
    return tot

Num = int(input("Please Enter any Value: "))
tot = calcSOD(Num)
print("\n Sum of the digits = %d" %tot)

#8. Write a recursive python function to print binary of a given decimal number.
# Function to print binary number using recursion
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = 34

convertToBinary(dec)
print()
#9. Write a recursive python function to print octal of a given decimal number
def DecimalOctal(num):
    if(num > 0):
        DecimalOctal((int)(num/8))
        print(num%8, end='')

# take input
num = int(input('Enter a decimal number: '))

# calling function and display result
print('Octal value: ', end='')
DecimalOctal(num)
#10. Write a recursive python function to find the Nth term of the Fibonacci series.
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Reading number of terms
term = int(input("Which term of Fibonacci series? "))

result = fib(term)
print("\n%dth term of Fibonacci series is: %d" %(term, result))
