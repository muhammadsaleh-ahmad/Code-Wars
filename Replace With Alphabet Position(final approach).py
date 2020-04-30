# the logic is used to automatically generate the key pairs for the function
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'
         ,'t','u','v','w','x','y','z']
x=1
numlist=[]
for num in range (1,27):
    if x == num:
        numlist.append(str(x))
        x +=1
key=[]
for t in range (1,27):
    a,b=letters[0],numlist[0]
    letters.pop(0)
    numlist.pop(0)
    key.append((a,b))


# the function is used to perform the required action on the string entered in the function
def alphabet_position(text):
    my_str=[]
    
    for letter in text:

        for x in range (26):

            if letter == key[x][0] or letter.lower() == key[x][0]:

                my_str.append(key[x][1])
                

            else:
                pass
    
    return ' '.join(my_str)

# test used to ensure the validity of the code
from random import randint
test.assert_equals(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
test.assert_equals(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

number_test = ""
for item in range(10):
    number_test += str(randint(1, 9))
test.assert_equals(alphabet_position(number_test), "")
