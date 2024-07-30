
#in Membership operator
# initialized some sequences
list1 = [1, 2, 3, 4, 5]
str1 = "Hello World"
set1 = {1, 2, 3, 4, 5}
dict1 = {1: "V1", 2:"V2", 3:"V3"}
tup1 = (1, 2, 3, 4, 5)

# checking an integer in a list
print(2 in list1)

# checking a character in a string
print('O' in str1)

# checking an integer in aset
print(6 in set1)

# checking for a key in a dictionary
print(3 in dict1)

# checking for an integer in a tuple
print(9 in tup1)

for i in list1:
    print(i)
for j in str1:
    print(j," ")

#is membership operator

num1 = 5
num2 = 6

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = lst1

str1 = "hello world"
str2 = "hello world"

# using 'is' identity operator on different datatypes
print(num1 is num2)
print(lst1 is lst2)
print(lst1 is lst3)
print(str1 is str2)


#The equality operator is used to compare the value of two variables,
# whereas the is used to compare the memory location of two variables.

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]

# using 'is' and '==' operators
print(lst1 is lst2)
print(lst1 == lst2)
