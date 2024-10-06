# class MyClass:
#     __name = "Gwalior"

# print(MyClass.__name)


# class MyClass:
#     __name = "Gwalior"
#     def __private_method(self):
#         print("private method")

# obj = MyClass()
# obj.__private_method()


# class MyClass:
#     def __init__(self,name,age):
#         self.__name= name
#         self.__age=age

# obj = MyClass("ITM",22)
# # print(obj.__name)   # if we dont use this then no output and if we use this then error 
# # print(obj.__age)




# class MyClass:
#     def __init__(self,name,age):
#         self.__name= name
#         self.__age=age
    
#     def access_private_members(self):
#         print(self.__name,self.__age)

# obj = MyClass("ITM",22)
# obj.access_private_members()


## use name mangling to accsee private members

# class MyClass:
#     def __init__(self,name,age):
#         self.name= name
#         self.__age=age
    
# obj=MyClass('XYZ', 20)
# print('Name: ', obj.name)
# print('Age: ', obj._MyClass__age)


# class MyClass:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def access_private_membeers(self):
#         return self.__name, self.__age

# obj = MyClass("ITM", 22)
# name , age = obj.access_private_membeers()
# print(name)
# print(age)


# class MyClass:
#     def __init__(self):
#         self._dept="CSE"

# class Student(MyClass):
#     def __init__(self,name):
#         self.name = name
#         MyClass.__init__(self)
#     def show(self):
#         print("Student Name :", self.name)
#         print("Department Name :", self._dept)

# obj = Student("XYZ")
# obj.show()
# print(obj._dept)





# class MyClass:
#     def __init__(self,name=None,age=0):
#         self.__name=name
#         self.__age=age
#     def set_name(self,name):
#         self.__name=name
#     def get_name(self):
#         return self.__name

#     def set_age(self,age):
#         self.__age=age
#     def get_age(self):
#         return self.__age

# obj = MyClass()
# obj.set_name("ITM")
# # obj.set_age("20")
# print(obj.get_name())
# # print(obj.get_age())



# class MyClass:
#     __num=10
#     __name='sahu'
#     __age=98

#     def set_num(self,num):
#         self.__num=num
#     def get_num(self):
#         return self.__num
    
#     def set_name(self,name):
#         self.__name=name
#     def get_name(self):
#         return self.__name
    
#     def set_age(self,age):
#         self.__age=age
#     def get_age(self):
#         return self.__age
    
# obj=MyClass()
# print(obj.get_num())
# print(obj.get_name())
# print(obj.get_age())



# ======validtion======
# import re
# class MyClass:
#     def __init__(self,name=None):
#         self.__name=name
#     def set_name(self,name):
#         find="vishal aulad hai"
#         match=re.search(name,find)

#         if match:
#             self.__name=name
    
#     def get_name(self):
#         return self.__name
    
# obj= MyClass()
# obj.set_name("vis")
# print(obj.get_name())





#============== ABSTRACTION=====================================

# from abc import ABC,abstractmethod
# class Bike(ABC):
#     @abstractmethod
#     def show(self):
#         pass
    
#     def defined_method(self):
#         print("hello")
#     name="ITM"

# class child(Bike):
#     def show(self):
#         print("implemented")
#     color="Navy"

# ch=child()
# ch.show()
# ch.defined_method()
# print(ch.name)
# print(ch.color)



# from abc import ABC,abstractmethod
# class Bike(ABC):
    
#     def show(self):
#         print("hello")
#     name="ITM"
    
#     @abstractmethod
#     def defined_method(self):
#         pass

# class child(Bike):
#     def defined_method(self):
#         print("implemented")
#     color="Navy"

# ch=child()
# ch.show()
# ch.defined_method()
# print(ch.name)
# print(ch.color)














