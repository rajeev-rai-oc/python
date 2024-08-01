#Try and except statements are used to catch and handle exceptions in Python

#Type Error
x = 5
y = "hello"
try:
	z = x + y
except TypeError:
	print("Error: cannot add an int and a str")

a = [1, 2, 3]
try: 
	print ("First element = %d" %(a[0]))

	print ("Fourth element = %d" %(a[4]))

except:
	print ("Error Occured")


#The code enters the else block only if the try clause does not raise an exception.
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)



#A try statement can have more than one except clause,
#  to specify handlers for different exceptions.

def fun(a):
	if a < 4:

		b = a/(a-3)
	print("Value of b = ", b)
	
try:
	fun(3)
	fun(5)
except ZeroDivisionError:
	print("ZeroDivisionError Occurred and Handled")
except NameError:
	print("NameError Occurred and Handled")
finally:
	print("This is always executed")
	

#The raise statement allows to force a specific exception to occur
try: 
	raise NameError("Hi there")
except NameError:
	print ("An exception")
