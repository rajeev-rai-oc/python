#Lambda Funtion
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())

#map function(applies the function to each element of the list)
n=[1,2,3,4]
print("Map Function:",list(map(lambda x:x**2, n)))

#filter function
print("Filter Function:",list(filter(lambda x:x>2, n)))


#List Comprehension
#Syntax: newList = [ expression(element)if else expresion for element in old List if condition(Filter) ]

list = [i*10 for i in range(5) if i % 2 == 0] 
print(list)

list2=[{"name":"Joe"},{"name":"Mon" }]

print([i["name"] for i in list2])

#Dictionary Comprehension 
#{key: value for (key, value) in iterable if condtion}


keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  
 
myDict = { k:v for (k,v) in zip(keys, values)}  
# myDict = dict(zip(keys, values))  

print (myDict)

dict={i:i**3 for i in range(5)}
print(dict)
