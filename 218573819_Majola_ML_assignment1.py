## problem 1

def list_check(nums):
    '''
    check and return true if the sequence 0,1,3
    appers in the list somewhere
    '''
    for i in range(0,len(nums)-1):
        if nums[i]==0:
            if nums[i+1]==2:
                if nums[i+2]==3:
                    return True

    return False 

nums=[1, 0, 2, 3, 1]
print(list_check(nums))


##problem 2

def string_bits(str):
    '''
    return a new string made of every other character
    starting with the first, so "Hello" yeilds at "Hlo"
    '''
    newStr =""
    length = len(str)
    index = 0
    while index < length:
        newStr= newStr+str[index]
        index =index +2
        

    return newStr

result ="heeololeo"
print(string_bits(result))


#problem 3

def end_other(a,b):
    '''
    return true if either of the strings appears at the very end
    of other string, ignoring the upper/lower case differrences (in other words, 
    the computation should not be "case sensitive" )
    '''
    a1 =a.lower()
    b1 = b.lower()

    if(a1[-1]== b1[-1]):
        if(a1[-2]== b1[-2]):
            if(a1[-3]== b1[-3]):
                return True
    else:
        return False

#first testing 
string1="heeololeo"
string2='leo'
print(end_other(string1,string2))

#second testing 
string11="myname"
string22='mamama'
print(end_other(string11,string22))

## problem 4

def double_char(str):
    '''
    return a string where for evey char in the original,
    there are two chars
    '''
    
    i=0
    length = len(str)
    result = ""
    while i < length:
        result = result + str[i]
        result = result + str[i]
        i=i+1
        
    return result

string22='mamama'
print(double_char(string22))


## problem 5
def no_teen_sum(a, b, c):
    '''
    return their sum. However, if any of the values 
    is a teen -- in the range 13..19 inclusive -- then that value counts as 0, 
    except 15 and 16 do not count as a teens
    '''
    sum = fix_teen(a) + fix_teen(b) + fix_teen(c)
    return sum
    
def fix_teen(n):
    '''
    takes in an int value and returns that value fixed for the 
    teen rule. In this way
    '''
    if 13 <= n and n <= 19 and n != 15 and n!= 16:
        return 0
            
    return n


# testing 
q=17
f=19
h =13
print(no_teen_sum(q,f,h))

# testing2
q=17
f=9
h =3
print(no_teen_sum(q,f,h))


## problem 6
def count_evens(nums):
    '''
    returns the number of even integers in the given array
    '''

    even_count = 0
    x = 0
    
      
    while(x < len(nums)):
        
        
        if nums[x] % 2 == 0:
            even_count += 1
    return even_count


#testing 
list1 = [10, 21, 4, 45, 66, 93, 11]

print(count_evens(list1))
