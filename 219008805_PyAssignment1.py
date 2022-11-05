#### EXERCISE 1 30 MARKS##
## Problem 1 - 10 Points###
# Given the string:
s = 'fullstackslp'

print(s[0])
print(s[-1])
print(s[4:9])
print(s[9:12])
print(s[7:10])

###############
## Problem 2 - LISTS - 5 Marks##
###############

l = [3,7,[5,[1,4,'hello']]]
# Reassign "hello" to be "goodbye"
l[2][1][2] = 'goodbye'
print(l)

###############
## Problem 3 - DICTIONARIES - 6 Marks##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

## Problem 4 - SETS - 4 Marks##
# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
my_set = set(mylist)
print(my_set)

###############
## Problem 5  - FORMATTING - 5 Marks##
###############

# You are given two variables:
age = 45
name = "Kyle"

my_String = "Hello my dog's name is {} and he looks {} years old".format(name, age)
print(my_String)

# Use print formatting to print the following string:
"Hello my dog's name is Kyle and he looks 45 years old"