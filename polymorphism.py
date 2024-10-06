# POLYMORPHISM 


# 1ST -> METHOD OVERRIDING(redefine method) --> 

# 2 CLASSES --> Inheritance --> parent class(show(num1))
#                           --> child class(show(num1))




# class Parent:
#     def my_method(self):
#         print("parent")

# class Child(Parent):
#     def my_method(self):
#         print("child")

# ch = Child()
# ch.my_method()




# error

# class Parent:
#     def my_method(self):
#         print("parent")

# class Child(Parent):
#     def my_method(self, num1):
#         print("child")
    
# ch = Child()
# ch.my_method()
# ch.my_method(10)





# 2nd -> METHOD OVERLOADING --> 

# 1 CLASS --> myclass[show(num1), show(num1, num2)]

# def addition(a, b):
#     c = a + b
#     print(c)


# def addition(a, b, c):
#     d = a + b + c
#     print(d)


# # the below line shows an error
# # addition(4, 5)

# # This line will call the second product method
# addition(3, 7, 5)


# error=======
# class MyClass:
#     def my_method(self, num1):
#         print("bye")
	
#     def my_method(self, num1, num2):
#         print("hi")	

# m1 = MyClass()
# m1.my_method(100)
# m1.my_method(100, 200)



# class MyClass:
#     def my_method(self, num1,num2,num3=None):
#         if num3 == None:
#             print(num1+num2)
#         else:
#             print(num1+num2+num3)

# m1 = MyClass()
# m1.my_method(100,200,300)
# m1.my_method(100, 200)





# 3rd -> OPERATOR OVERLOADING --> 

# class Myclass:
#     def __init__(self, num):
#         self.num = num

#     def __add__(self, other):
#         return self.num + other.num

#     def __mul__(self, other):
#         return self.num * other.num
    
#     # def __mul__(self, other):
#     #     return self.num / other.num

#     def __lt__(self, other):
#         return self.num < other.num

# m1 = Myclass(100)
# m2 = Myclass(20)
# print(m1.num + m2.num)
# print(m1 + m2)
# print(m1 * m2)
# # print(m1 * m2)
# print(m1 < m2)





#4th -> DUCK TYPE

# class Alien:
#     def fly(self):
#         print("this must be an alien")

# class animal:
#     def eat(self):
#         print("this must be an animal")

# class human:
#     def overthinker(self):
#         print("this mut be an human")

# dog=animal()
# jadu=Alien()
# ayush=human()

# def check_objs(sel):
#      sel.eat()

# check_objs(dog)












