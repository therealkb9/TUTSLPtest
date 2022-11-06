# Problem 1
def list_check(num):
    """
    Find pattern in num list
    """
    print(2 in num)
list_check([0,2,3])

# Problem 2
def string_bit(str):
    """
    Extract bits from string
    """
    n=0
    w=""
    i = len(str)
    while n <i:
        w = w + str[n]
        n +=2
    print(w)
string_bit("heeololeo")

# Problem 3
"""
Extract last char of string with less len
"""
def end_other(a,b):
    a= a.lower()
    b= b.lower()
    la = len(a)
    lb = len(b)
    end=""
    count = -1
    if(la>lb):
        e = lb
        e = e*-1
        c = b
    else:
        e = la
        e = e*-1
        c = a
    while e<=count:
        if(la>lb):
            end = end + a[e] 
        else:
            end = end + b[e]
        e +=1
    print(c==end)
end_other("Blue","Rediblue")

# Problem 4
def double_char(str):
    """
    Duplicate every char in a string
    """
    dup_char=""
    n = len(str)
    i=0
    while i < n:
        dup_char = dup_char + str[i] + str[i]
        i +=1
    print(dup_char)
double_char("LeseDi")

# Problem 5


# Problem 6
def count_evens(even):
    """
    Counting even numbers in array
    """
    even_number =0
    n = len(even)
    i=0
    while i < n:
        if(even[i]%2==0):
            even_number+=1
        i+=1
    print(even_number)
count_evens([2,1,2,6,4])

