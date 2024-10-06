# #Using Property Function

# class GetterSetter:
#     def _init_(self,age=0,name=None):
#         self.__name=name
#         self.__age=age
#     def set_name(self,name):
#         print('Setter for name')
#         self.__name=name
#     def get_name(self):
#         print('Getter for name')
#         return self.__name
#     def set_age(self,age):
#         print('Setter for age')
#         self.__age=age
#     def get_age(self):
#         print('Getter for age')
#         return self.__age
    
#     name=property(get_name,set_name)
#     age=property(get_age,set_age)

# #obj=GetterSetter()
# #obj.set_name('Rahul')
# #print(obj.get_name())

# obj=GetterSetter()
# obj.name='Rahul'
# print(obj.name)
# obj.age=18
# print(obj.age)







## Using Decorator

# class GetterSetter:
#     def _init_(self,age=0,name=None):
#         self.__name=name
#         self.__age=age
#     @property
#     def name(self):
#         print('Getter for name')
#         return self.__name
#     @name.setter
#     def name(self,name):
#         print('Setter for name')
#         self.__name=name
#     @property
#     def age(self):
#         print('Getter for age')
#         return self.__age
#     @age.setter
#     def age(self,age):
#         print('Setter for age')
#         self.__age=age

# #obj=GetterSetter()
# #obj.set_name('Rahul')
# #print(obj.get_name())

# obj=GetterSetter()
# obj.name='Rahul'
# print(obj.name)
# obj.age=18
# print(obj.age)

# #data=  "0101010"
# #print(data[1::2])
