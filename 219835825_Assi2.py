#################
### Problem 1 ###
#################

def list_check(num):
    s = ''.join(str(i) for i in num)
    print('023' in s)
    
list_check([0,1,2,3,0,2,3,4,5])

#################
### Problem 2 ###
#################
def string_bit(str):
    x=0
    y=""
    i = len(str)
    while x <i:
        y =y + str[x]
        x = x+ 2
    print(y)
string_bit("Hello")

#################
### Problem 3 ###
#################
def last_char(a,b):
    a= a.lower()
    b= b.lower()
    cd = len(a)
    de = len(b)
    end=""
    count = -1
    if(cd>de):
        e = de
        e = e*-1
        c = b
    else:
        e = cd
        e = e*-1
        c = a
    while e<=count:
        if(cd>de):
            end = end + a[e]
        else:
            end = end + b[e]
        e +=1
    print(c==end)
    
last_char("Blue","Rediblue")

#################
### Problem 4 ###
#################
def double_value(str):
    dup_char=""
    n = len(str)
    i=0
    while i < n:
        dup_char = dup_char + str[i] + str[i]
        i +=1
    print(dup_char)
double_value("Great stuff")


#################
### Problem 6 ###
#################
def count_even(even):
    even_number =0
    n = len(even)
    i=0
    while i < n:
        if(even[i]%2==0):
            even_number+=1
        i+=1
    print(even_number)
count_even([2,1,2,6,4])
