# --------functions ----------

def func(num1,num2):
    return(num1+num2)
# should leave two empty lines after the function

print("Result is ",func(6,7))


# question:- ek func big uske andar small function

def big(num1,num2):
    add=num1+num2
    def small(num):
        res=add**2
        return res
    return small(add)


print(big(10,20))

# alternate

def big(num1,num2):
    add=num1+num2
    def small():
        res=add**2
        return res
    return small()

print(big(10, 20))



# -------Decorator-------


# fuctions as objects  

def fun(text):
    return text.upper()
 
 
yell = fun
print(yell('Hello'))


# function as argument
def mul(x, y):
    return x * y

def calculate(func, x, y):
    return func(x, y)

result = calculate(mul, 4, 6)
print(result)  

# used as function wrapped inside function  argument bhi as function dete




def decorator(func):
    def inner():
        print("krishna")
        func()
    return inner
def fun():
    print("radha")
new_val= decorator(fun)
new_val()




def uppercase(function):
    def wrapped():
        fun=function()
        return fun.upper()
    return wrapped
# @uppercase
def hi():
    return "hi"

dec=uppercase(hi)
print(dec())
        

# -----iterators-------

my_list=[10,11,12,13]
iterator=iter(my_list)

for i in iterator:
    print(i)


char="my world"

iterator=iter(char)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# iterator--> jo iterate krta h , iterable--> jo iterate hota h  
# -------generator--------

def gen(num):
     value=0
     while value < num:
         yield value
         value += 1

for value in gen(3):
    print(value)

# example 2
def gen(num1):
    num=0
    while num<num1:
        yield num
        num+=1

for i in gen(5):
    print(i)


def gen():
    yield 1
    print("abc")
    yield 2
    print("hi")
    yield 3
    print("hello")
    yield 4
    print("ok")


new=gen()
print(next(new))
print(next(new))
print(next(new))
print(next(new))
# print(next(new))

def gen():
    yield 1
    yield 2
    yield 3
    yield 4

new=gen()
print(next(new))
print(next(new))
print(next(new))
print(next(new))









