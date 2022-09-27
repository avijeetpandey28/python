#1. Write a python script to reverse a number.
Number = int(input("Please Enter any Number: "))
Reverse = 0
while(Number > 0):
    Reminder = Number %10
    Reverse = (Reverse *10) + Reminder
    Number = Number //10

print("\n Reverse of entered number is = %d" %Reverse)

#2. Write a python script to check whether a given number is Prime or not

n=int(input("Enter a number:"))
if n>1:
    for i in range(2,n//2):
        if(n%i)==0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is neither prime nor composite")
    
#3. Write a python script to print all Prime numbers under 100
for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
        
#4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
        
lower = int(input("Enter the lower value:"))
upper = int(input("Enter the upper value:"))
for number in range(lower,upper+1):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
            print(number)

#5. Write a python script to find next prime number of a given number
def nextprime(n):
    if n < 0:
      raise ValueError
  
    for i in range(n + 1, n +200):
        if i > 1:
            pr = True
            for j in range(2, i):
                if (i % j) == 0:
                    pr = False
                    break
            if pr:
                return i
    return 'not found'

#6. Write a python script to print first N prime numbers
i = 1
x = int(input("Enter the number:"))
for k in range(1, x+1):
    c = 0
    for j in range(1, i+1):
        a = i % j
        if a == 0:
            c = c + 1

    if c == 2:
        print(i)
    else:
        k = k - 1

    i = i + 1
#7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
num1= int(input("Please enter the first number: "))
num2= int(input("Please enter the second number: "))

mn = min(num1, num2)

for i in range(1, mn+1):

    if num1%i==0 and num2%i==0:
        hcf = i
    
if hcf == 1:
    print("Yes! They are Co-Prime.")

else:
    print("Sorry! They are not Co-Prime.")
          
#8. Write a python script to print first N terms of a Fibonacci series
number = int(input("Enter count: "))

a = 0
b = 1
sum_fib = 0
count = 1
print(a,b, end=" ")
while count <= number-2:
    sum_fib = a + b
    a = b
    b = sum_fib
    count += 1
    print(sum_fib, end=" ")
#9. Write a python script to calculate LCM of two numbers
print("Enter Two Numbers: ")
numOne = int(input())
numTwo = int(input())

if numOne>numTwo:
    lcm = numOne
else:
    lcm = numTwo

while True:
    if lcm%numOne==0 and lcm%numTwo==0:
        break
    else:
        lcm = lcm + 1

print("\nLCM =", lcm)

#10. Write a python script to calculate HCF of two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
 
HCF = 1
 
for i in range(2,a+1):
    if(a%i==0 and b%i==0):
        HCF = i
 
print("First Number is: ",a)
print("Second Number is: ",b)
print("HCF of the numbers is: ",HCF)
