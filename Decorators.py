# Functions can return another function 
#Closures
def create_adder(x): 
    def multiplier(): 
        return 2*x 

    return multiplier #return the funtion which is waiting to be executed

add_15 = create_adder(15)
add_10=create_adder(10)

print(add_15())
print(add_10())

#Decorators allow us to wrap another function in order to extend 
# the behaviour of the wrapped function, without permanently modifying it.

def decorator_func(Og_func):
    def wrapper_func(*args,**kwargs): #These are like parameter to be used with the original function
        print("Executed Wrapper function before display")
        return Og_func(*args,**kwargs)
    return wrapper_func


@decorator_func
def display():
    print("This is Original Display Function")
#Equivalent to display = decorator_func(display)

@decorator_func
def display_info(name,age):
    print("Name and Age is ",name ,age)

display()   #Wrapper code added to original display function
display_info("Rajeev", 23)
#we can also pass parameters to the wrapper function


def hello_decorator(func):
    def inner1(*args, **kwargs):
        
        print("before Execution")
        
        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")
        
        # returning the value to the original frame
        return returned_value
        
    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b

x, y = 2, 3

# getting the value through return of the function
print("Sum =", sum_two_numbers(x, y))


#decorator chaining 
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 

def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 

@decor1
@decor
def num(): 
    return 10

@decor
@decor1
def num2():
    return 10
  
print(num()) 
print(num2())
