# #######################
# ### Problem - 1 - STRINGS ####
# #######################

s = 'fullstackslp'

# use indexing to print our the following:

# 'f'
print(s[0])

# 'p'
print(s[-1])

# 'stack'
print(s[4:9])

# 'slp'
print(s[9:])

# 'cks'
print(s[7:10])

# reverse string using indexing
print(s[::-1])

# #######################
# ### Problem - 2 - LISTS ####
# #######################

# replace 'hello' with 'goodbye'

l = [3,7,[5,[1,4,'hello']]]
l[-1][-1][-1] = 'goodbye'

# #######################
# ### Problem - 3 - DICTIONARIES ####
# #######################

# Using keys and indexing, grap hello form the following dictionaries

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

# #######################
# ### Problem - 4 - SETS ####
# #######################

# Use a set to find unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
myset = set(mylist)

print(myset)

# #######################
# ### Problem - 5 - FORMATTING ####
# #######################

# Given two variables:
age = 45
name = 'Kyle'

# Use print formatting to print the following string
"Hello my dog's name is Kyle and he looks 45 years old"

print("Hello my dog's name is {} and he looks {} years old".format(name, age))


