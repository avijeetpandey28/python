#1. Write a python script to create a String in 3 different possible ways
St1="MySirG"
St2='MySirG'
St3="""MySirG"""


#2. Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)
st="iNeuron"
print(st[0:6:1])

#3. Write a python script to Get the characters from position 2 to position 5 (Given String “Hello Learners” using the slice syntax)
st="Hello Learners"
print(st[2:6:1])

#4. Write a python script to demonstrate String Concatenation adding space in between ( Given Strings a=”Learning” b=”Python” )
a="Learning"
b="Python"
print(a+' '+b)

#5. Write a python script to get the count of total number of characters in String a= “iNeuron”
a="iNeuron"
print(len(a))

#6. Write a python script to reverse a String. (“iNeuron”)
a="iNeuron"
print(a[::-1])

#7. Write a python script to determine whether a string contains a specific substring.
String1 = "A man in need is a man indeed"
 
if "need" in String1:
    print("Yes! it is present in the string")
else:
    print("No! it is not present")
#8. Write a python script to check if a string contains only numbers.
ini_string1 = '1234556'
ini_string2 = 'ab123bc'
 
# printing initial string
print ("Initial Strings : ", ini_string1, ini_string2)
 
# Using isnumeric()
if ini_string1.isnumeric():
    print ("String1 contains all numbers")
else:
    print ("String1 doesn't contains all numbers")
     
if ini_string2.isnumeric():
    print ("String2 contains all numbers")
else:
    print ("String2 doesn't contains all numbers")
    
#9. Write a python script to check if a string contains only characters of the alphabet
my_string1 = "25482x736y54"                  # Create character string with letters
my_string2 = "395634875"
print(any(c.isalpha() for c in my_string1))
print(any(c.isalpha() for c in my_string2))  # Check if letters are contained in string

#10. Write a python script to convert an integer to a string.
num = 10
 
# check  and print type of num variable
print("Type of variable before convertion : ", type(num))
 
# convert the num into string
converted_num = str(num)
 
# check  and print type converted_num variable
print("Type After convertion : ",type(converted_num))
