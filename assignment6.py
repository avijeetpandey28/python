#1Write a python script to check whether a given number is positive or non-positive

#2. Write a python script to check whether a given number is divisible by 5 or not
num = int(input("enter a number: "))
if num%5==0:
    print("number is divisible by 5")
else:
    print("number is not divisible ny 5")
    #or
print("number is divisible by 5"if int(input("enter a number: "))%5==0 else "number is not divisible by 5")

      
#3. Write a python script to check whether a given number is even or odd
print( "number is even" if int(input("enter a number: "))%2==0 else "number is odd")

#4. Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.
print("enter two numbers")
a,b=int(input()),int(input())
print(a if a>b else b)

#5. Write a python script to print two given words in dictionary order
print("enter two words")
a,b=input(),input()
print((b,a) if a>b else (a,b))

#6. Write a python script to check whether a given number is a three digit number or not.
x = int(input("enter a three digit number: "))
print("number is three digit number" if 99<x<100 else "not three digit number")

#7. Write a python script to check whether a given number is positive, negative or zero.
num = int(input("enter a number: "))
if num>0:
    print("positive number")
elif num<0:
    print("negative number")
else :
    print("zero")

#8. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
print("enter value of a,b,c of a quadratic equation")
a,b,c = int(input()),int(input()),int(input())
d = b**2-4*a*c
if d>0:
    print("real and distinct roots")
elif d==0:
    print("real and equal roots")
else:
    print("imaginary roots")
    

#9. Write a python script to check whether a given year is a leap year or not.
print("enter year number: ")
year = int(input())
if year%400==0:
    print("leap year")
elif year%100!=0 and year%4==0:
    print("leap year")
else :
    print("non leap year")
    
#10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
print("enter three number: ")
a,b,c = int(input()),int(input()),int(input())
print((a if a>c else c) if a>b else (b if b>c else c))
                                      
#11. Write a python script to take the month value in numeric format and display the number of days in it.
month = int(input("enter month number"))
if month in (1,3,5,7,8,10,12):
    print("31 days")
elif month in (4,6,9,11):
    print("30 days")
elif month==2 :
    print("28 or 29 days")
else :
    print("invalid month number")
    
    
#12. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part
x = complex(input("enter complex number"))
print(x.real)if x.real>x.imag else print(x.imag)
