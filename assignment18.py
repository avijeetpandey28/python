#1. Write a python program to create and print a dictionary which stores your information.(name, age, gender .....)
dict_1 = {'name':'avijeet','gender':'male','occupation':'student'}
print(dict_1)
print(type(dict_1))

#2. Write a python program to access the items of a dictionary by referring to its key name.
d1 = {102 :'Rahul ',105 :'Payal ',106 :'Arjun',107 :'Prachi '}
print(d1[102],d1[105],d1[106],d1[107])

#3. Write a python program to get a list of the values from a dictionary.
d1 = {102 :'Rahul ',105 :'Payal ',106 :'Arjun',107 :'Prachi '}
for k in d1:
    print(d1[k])
#4. Write a python program to change the value of a specific item by referring to its key name.
d1 = {102 :'Rahul ',105 :'Payal ',106 :'Arjun',107 :'Prachi '}

d1[102]="avijeet"
print(d1)

#5. Write a python program to print all key names in the dictionary, one by one.
d1 = {102 :'Rahul ',105 :'Payal ',106 :'Arjun',107 :'Prachi '}
for k in d1:
    print(k)
    
#6. Write a python program to create a dictionary that contains three dictionaries. (nested)
myfamily = { "child1" : {"name" : "Emil", "year" : 2004 }, "child2" : { "name" : "Tobias", "year" : 2007},"child3" : { "name" : "Linus", "year" : 2011}}
print(myfamily)
    
#7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
dictionary1 = {  'Pen': 5, 'Pencil': 4, 'Chocolate' : 15 }
dictionary2 = {'Apple': 25,'Ball': 10,'Doll' : 20 }
dictionary3 = {'banana':11,'mango':32}
dictionary1.update(dictionary2)
dictionary1.update(dictionary3)
print(dictionary1)


#8. Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]
 
# Printing original keys-value lists
print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))
 
# using naive method
# to convert lists to dictionary
res = {}
for key in test_keys:
    for value in test_values:
        res[key] = value
        test_values.remove(value)
        break
 
# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))

#9. Write a python program to merge two python dictionaries into one dictionary.
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)

#10. Write a python program to get the key of lowest value from the dictionary. sample_dict = {'C': 92,'Java': 66,'Python': 85}
sample_dict = {'C': 92,'Java': 66,'Python': 85}
d= min(sample_dict,key=sample_dict.get)
print(d)
 
