#1. Write a python script to calculate sum of first N natural numbers

N = int(input("Enter a natural number: "))

answer=0

for i in range(0,N+1):
	answer = answer + i;

print(answer)

#2. Write a python script to calculate sum of squares of first N natural numbers
N = int(input("Enter a natural number: "))

answer=0

for i in range(0,N+1):
	answer = answer + i;

print(answer)

#3. Write a python script to calculate sum of cubes of first N natural numbers
N = int(input("Enter a natural number: "))

answer=0

for i in range(0,N+1):
	answer = answer + i**3;

print(answer)

#4. Write a python script to calculate sum of first N odd natural numbers
N = int(input("Enter first n  natural number: "))

answer=0

for i in range(1,2*N+1,2):
	answer = answer + i;

print(answer)

#5. Write a python script to calculate sum of first N even natural numbers
N = int(input("Enter first n  natural number: "))

answer=0

for i in range(2,2*N+1,2):
	answer = answer + i;
print(answer)

#6. Write a python script to calculate factorial of a given number
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
   

#7. Write a python script to count digits in a given number
count = 0
number = int(input("Enter a number "))

while (number > 0):
  number = number//10
  count = count + 1
  print ("Total number of digits : ",count)


#8. Write a python script to calculate sum of digits of a given number
num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)

#9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
print("Enter the Binary Number: ", end="")
bnum = int(input())

dnum = 0
m = 1
blen = len(str(bnum))

for k in range(blen):
    rem = bnum%10
    dnum = dnum + (rem * m)
    m = m * 2
    bnum = int(bnum/10)

print("\nEquivalent Decimal Value = ", dnum)

#10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
num = int(input('Enter a Decimal number to Convert into Octal:'))
q=num
octal=0
i=0

while q!=0:
    rem = q%8
    octal = octal + rem * (10**i)
    q = q // 8
    i+=1

print('Octal Number=',octal)
