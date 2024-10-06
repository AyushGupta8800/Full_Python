# 3rd major piller
# inheritance

# type of inheritance 
# 1. simple inheitance


# lets create two classes

# class Parents:
#     def parents_method(self):
#         print("this is perent method")
# class Child(Parents):
#     pass

# ch=Child()
# ch.parents_method()




# lets add child own properties

# class Parents:
#     def parents_method(self):
#         print("this is perent method")
    
# class Child(Parents):
#     def children_method(self):
#         print("this is child method")

# ch=Child()
# ch.parents_method()
# ch.children_method()



# can we access parents properties with only child object if have two same method name====>

# class Parents:
#     def child_method(self):
#         print("this is perent method")
    
# class Child(Parents):
#     def child_method(self):
#         print("this is child method")

# ch=Child()
# ch.child_method()
# ch.child_method()




#2. Multilevel inheritance

# class GrandParents:
#     def grandparent_method(self):
#         print("this is grand parents method")
# class Parent(GrandParents):    
#     def parents_method(self):
#         print("this is parents method")
# class Child(Parent):
#     def children_method(self):
#         print("this is child methods")
# ch=Child()
# ch.grandparent_method()
# ch.parents_method()
# ch.children_method()




# 3. multiple inheritance

# class ParentOne:
#     def parent_one_method(self):
#         print("this is parent one method")

# class ParentTwo:
#     def parent_two_method(self):
#         print("this is parent two method")

# class child(ParentOne, ParentTwo):
#     def child_method(self):
#         print("this is child method")

# ch=child()
# ch.parent_one_method()
# ch.parent_two_method()
# ch.child_method()




# 4. hybrid inheritance

# class GrandParent:
#     def grand_parent_method(self):
#         print("this is grand parent method")
    
# class Parent_One(GrandParent):
#     def parent_one_method(self):
#         print("this is parent one method")

# class Parent_Two(GrandParent):
#     def parent_two_method(self):
#         print("this is parent two method")

# class Child(Parent_One,Parent_Two):
#     def child_method(self):
#         print("this is child method")

# ch=Child()
# ch.grand_parent_method()
# ch.parent_one_method()
# ch.parent_two_method()
# ch.child_method()




# 5. hierarchical inheritance

# class Parent:
#     def parent_method(self):
#         print("this is parent method")

# class ChildOne(Parent):
#     def child_one_method(self):
#         print("this is child one method")

# class ChildTwo(Parent):
#     def child_two_method(self):
#         print("this is child two method")

# ch1=ChildOne()
# ch2=ChildTwo()

# ch1.parent_method()
# ch1.child_one_method()

# ch2.parent_method()
# ch2.child_two_method()




# class Parent:
#     def __init__(self):
#         print("this is parent")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("this is child")
# ch=Child()




# class Parent:
#     def __init__(self):
#         print("this is parent")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("this is child")
#         super().__init__()
# ch=Child()




# class Parent:
#     def __init__(self,surname):
#         self.surname=surname
#         print("this is parent")
    
# class Child(Parent):
#     def __init__(self):
#         super().__init__("Gupta")
#         print("this is child")

# ch1=Child()
# print(ch1.surname)




# class Parent:
#     def __init__(self,surname):
#         self.surname = surname
#         print(surname)

#     def show(self, age):
#         print("this is parent method")
#         print(age)

# class Child(Parent):
#     def __init__(self):
#         super().__init__("Gupta")
#     def child_method(self):
#         print("this is child method")
#         super().show(29)


# ch = Child()
# ch.child_method()




# class ParentOne:
#     def method(self):
#         print("this is parent one logic")

# class ParentTwo:
#     def method(self):
#         print("this is parent two logic")

# class Child(ParentOne, ParentTwo):
#     pass

# ch = Child()
# ch.method()




# class ParentOne:
#     def method(self):
#         print("this is parent one logic")

#     def method_parentOne(self):
#         print("this is parent one calling")

# class ParentTwo:
#     def method(self):
#         print("this is parent two logic")

#     def method_parentTwo(self):
#         print("this is parent two calling")
# class Child(ParentOne, ParentTwo):
#     pass

# ch = Child()
# ch.method()
# ch.method_parentOne()
# ch.method_parentTwo()




# class ParentOne:
#     def __init__(self):
#         print("ParentOne")
# class ParentTwo:
#     def __init__(self):
#         print("ParentTwo")
# class Child(ParentOne, ParentTwo):
#     def __init__(self):
#         super().__init__()
#         print("Child")

# ch = Child()




# class ParentOne:
#     def __init__(self):
#         print("ParentOne")
# class ParentTwo:
#     def __init__(self):
#         print("ParentTwo")
# class Child(ParentOne, ParentTwo):
#     def __init__(self):
#         ParentTwo.__init__(self)
#         print("Child")

# ch = Child()



















