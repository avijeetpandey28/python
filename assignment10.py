
#1. Write a python script to print the first 10 multiples of 5.
for e in range(5,55,5):
    print(e)

#2. Write a python script to print first 10 multiples of N
n =  int(input("enter the number:"  ))
for e in range(1,11,1):
    print(n*e)


#3. Write a python script to print first M multiples of N.
n =  int(input("enter the number:"  ))
m = int(input("enter the multiples:"  ))
for e in range (1,m+1,1):
    print(e*n)
    

#4. Write a python script to print the first 10 multiples of N in reverse order.
n =  int(input("enter the number:"  ))
for e in range (n,0,-1):
    print(e*n)
  
#5. Write a python script to print table of user’s choice
x = int(input("enter the number"))
for e in range (1,11,1):
    print(e*x)



#6. Write a python script to print first N even natural numbers.
n =  int(input("enter the number:"  ))
for i in range(2,2*n+1,2):
    print(i)


#7. Write a python script to print first N odd natural numbers
n =  int(input("enter the number:"  ))
for i in range(1,2*n,2):
    print(i)
  
#8. Write a python script to print squares of first N natural numbers.
n =  int(input("enter the number:"  ))
for i in range(1,n+1):
    print(i**2)

#9. Write a python script to print cubes of first N natural numbers.
n =  int(input("enter the number:"  ))
for i in range(1,n+1):
    print(i**3)

#10. Write a python script to display all prime numbers within a range.
# range
#start = 15
#end = 45

for num in range(15,45):
    if(num>1):
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num, end = '  ')
    
    


