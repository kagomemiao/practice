# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number
def bigger(a,b):
    if a > b:
        return a
    else:
        return b
def numbers_in_lists(s):
    # YOUR CODE
    n = len(s)
    i = 0
    r = []
    z = []
    j = 0
    while i < n:
        d = int(s[i])
        if d > j:
            if not z == []:
                r.append(z)
                z = []
            r.append(d)
            j = d
        else:
            z.append(d)
        i = i + 1
    if not z == []:
        r.append(z)
    return r
        
    

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
print numbers_in_lists(string)
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
print numbers_in_lists(string)
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
print numbers_in_lists(string)
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result
print numbers_in_lists(string)
