#First python code
print("Hello World!")

#Datatypes

x = "Hello World" # string
x = 5  # integer
x = 6.5  # float
x = 3j  # complex
x = ["geeks", "for", "geeks"]  # list 
x = ("geeks", "for", "geeks")  # tuple
x = {"name": "Suraj", "age": 24} # dict
x = {"geeks", "for", "geeks"} # set
x = True  # bool
x = b"Geeks" # binary


#input 

x= int(input("Enter Value of x"))
print("X is:",x)

#If-else
i = 12
if (i < 10): 
    print("i is smaller than 10") 
    print("In if Block") 
else: 
    print("i is greater than 15") 
    print("In else Block") 
print("Outside if and else Block") 


#if-else-if ladder
i = 2
if (i == 1): 
    print("i is 1") 
elif (i == 2): 
    print("i is 2") 
elif (i == 3): 
    print("i is 3") 
else: 
    print("i is not present") 


#for loop
for i in range(0,9,3): #rang(start, stop(excluding), step)
    print(i)

# while loop
# Python program to illustrate while loop 
count = 0
while (count < 3): 
    count = count + 1
    print("Count is: ",count)



# Break and continue

# loop from 1 to 10 
for i in range(1, 11): 
	if i == 6: 
		continue
	else: 
		print(i, end = " ")
          
#Functions
def func(x):
     i=1
     print("\n")
     while(i<x):
        if(x%i==0):
           print(x,"is divisible by",i)
        i+=1

func(x)