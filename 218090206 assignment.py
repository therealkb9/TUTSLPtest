

EXERCISE 1 30 MARKS:

## Problem 1 
# Given the string:

s = 'fullstackslp'

# Use indexing to print out the following:
# 'f'
# 'p'
# 'stack'
# 'slp'
# 'cks'
# Bonus: Use indexing to reverse the string


s = 'fullstackslp'


print(s[0])  
print(s[-1])  
print(s[4:9])  
print(s[-3:])  
print(s[7:10]) 
#  Reversing the string
print(s[::-1])  





## Problem 2 LISTS
-
5 Marks##

##======================== Problem 2 - LISTS=========================================## 

5 Marks##
# Given this nested list:
nested_list = [3,7,[5,[1,4, 'hello']]]
# Reassign "hello" to be "goodbye"

nested_list[2][1][2] = 'goodbye'

print(nested_list)





##======================= Problem 3 - DICTIONARIES 6 Marks===================================##
# Using keys and indexing, grab the 'hello' from the following dictionaries:
d1 = {'simple_key': 'hello'}
d2 = {'k1':{'k2': 'hello'}}
d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}


hello_d1 = d1['simple_key']
print(hello_d1)

hello_d2 = d2['k1']['k2']
print(hello_d2)



hello_d3 = d3['k1'][0]['nest_key'][1][0]
print(hello_d3)

















##=========================Problem 4 - SETS =================================##
# Use a set to find the unique values of the list below: 

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

values = set(mylist)

print(values)


##================================Problem 5============================================##

# You are given two variables:
age = 45
name = "Kyle"  
# Use print formatting to print the following string: "Hello my dog's name is Kyle and he looks 45 years old"
print(f"Hello my dog's name is {name} and he looks {age} years old")



