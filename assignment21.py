#1. Write a recursive python function to print first N natural numbers.
def f(n):
    if n>0:
        f(n-1)
        print(n)
f(9)   
#2. Write a recursive python function to print first N natural numbers in reverse order
def f(n):
    if n>0:
        print(n,end=' ')
        f(n-1)
print()

f(6)

#3. Write a recursive python function to print first N odd natural numbers
def f(n):
    if n>0:
        
        f(n-1)
        print(2*n-1,end=' ')
print()
        
        
        
f(10)    
#4. Write a recursive python function to print first N odd natural numbers in reverse order
def f(n):
    if n>0:
        print(2*n-1,end=' ')
        
        f(n-1)
      
print()

f(10)
#5. Write a recursive python function to print first N even natural numbers.
def f(n):
    if n>0:
        
        f(n-1)
        print(2*n,end=' ')
print()
        
        
        
f(10)
#6. Write a recursive python function to print first N even natural numbers in reverse order.
def f(n):
    if n>0:
        print(2*n,end=' ')
        f(n-1)
print()       
        
f(10)
#7. Write a recursive python function to print squares of first N natural numbers
def square(n):
    if n>=1:
        square(n-1)
        print(n**2)
        
print()

square(10)

#8. Write a recursive python function to print cubes of first N natural numbers
def cube(n):
    if n>=1:
        cube(n-1)
        print(n**3)
        
print()

cube(10)
#9. Write a recursive python function to print first N multiples of a given number.
def mul_table(N, i):
     
    # Base Case
    if (i > 10):
        return
     
    # Print the table for
    # current iteration
    print(N,"*",i,"=",N * i)
     
    # Recursive call to next
    # iteration
    return mul_table(N, i + 1)
 
# Driver Code
 
# Input number whose table
# is to print
N = 8
 
# Function call to print
# the table
mul_table(N, 1)



#10.Write a recursive python function to print a number in reverse order.
Reverse = 0
# Defining a Recursive Function
def Reverse_Integer(Number):
    global Reverse
    if(Number > 0):
        Reminder = Number %10
        Reverse = (Reverse *10) + Reminder
        Reverse_Integer(Number //10)
    return Reverse

# Take the Input From the User
Number = int(input("Enter any Number: "))
Reverse = Reverse_Integer(Number)
print("Reverse of entered number is = %d" %Reverse)
