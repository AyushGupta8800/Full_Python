# print("start")
# print("line1")
# print("line2")
# try:
#     print(10/0)
# except:
#     print("dont use zero for division")
# print("line 4")
# print("line 5")



# print("start")
# print("line1")
# print("line2")
# try:
#     print(10/0)
# except ArithmeticError as e:
#     print(e)
# print("line 4")
# print("line 5")




# print("start")
# print("line1")
# print("line2")
# try:
#     print(10/0) 
#     e= ArithmeticError()
# except ArithmeticError as e:
#     print(e)
# print("line 4")
# print("line 5")




# we can also use ZeroDivisionError in place of ArithmeticError

# print("start")
# print("line1")
# print("line2")
# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print(e)
# print("line 4")
# print("line 5")



# print("start")
# print("line1")
# print("line2")
# num1= int(input("enter num1- "))
# num2= int(input("enter num2- "))
# try:
#     print(num1/num2)
# except Exception:
#     num2=1
#     print("you entered zero as number 2 taking default 1")
#     print(num1/num2)
# print("line 4")
# print("line 5")




# print("start")
# print("line1")
# print("line2")
# try:
#     li=[1,2,3]
#     print(li[5])
# except Exception as e:
#     print(e)
# print("line 4")
# print("line 5")





# print("start")
# print("line1")
# print("line2")
# try:
#     li=[1,2,3]
#     print(li[5])

# except IndexError as e:
#     print("Block1")

# except Exception as e:
#     print("Block 2")
# print("line 4")
# print("line 5")



# print("start")
# print("line1")
# print("line2")
# try:
#     li=[1,2,3]
#     print(li[5])
#     try:
#         print(10/0)
#     except Exception as e:
#         print("inner block")
# except Exception as e:
#     print("outer Block")
# print("line 4")
# print("line 5")





# print("start")
# print("line1")
# print("line2")
# try:
#     try:
#         print(10/0)
#     except Exception as e:
#         print("inner block")
#         li=[1,2,3]
#         print(li[5])
# except Exception as e:
#     print("outer Block")
# print("line 4")
# print("line 5")




# print("start")
# print("line1")
# print("line2")
# try:
#     li=[1,2,3]
#     print(li[5])
#     try:
#         print(10/0)
#     except Exception as e:
#         print("inner block")
# except ArithmeticError as e:
#     print("outer Block")
# print("line 4")
# print("line 5")




# print("start")
# print("line1")
# print("line2")
# try:
#     print(10/0)
# except ArithmeticError as e:
#     print("except block")
# finally:
#     print("final Block")
# print("line 4")
# print("line 5")



# print("start")
# print("line1")
# print("line2")
# try:
#     print(10/2)
# # except ArithmeticError as e:
# #     print("except block")
# finally:
#     print("final Block")
# print("line 4")
# print("line 5")





#custom exceptional handling


# marks = int(input("Enter marks"))

# if marks < 50:
#     print("kash batch 4 me hote ye log")
#     print("next steps")
# else:
#     print("batch 1 will be good fit ")




# print("start")
# print("line1")
# marks= int(input("enter makes"))
# if marks<50:
#     raise("kash batch 4 me hote")
#     # print("next stop")
# else:
#     print("batch 1 will be good fit")
# print("line 4")
# print("line 5")



# print("start")
# print("line1")
# marks= int(input("enter makes"))
# if marks<50:
#     raise ArithmeticError("kash batch 4 me hote")
# else:
#     print("batch 1 will be good fit")

# print("line 4")
# print("line 5")



# class ITMError(BaseException):
#     def __init__(self,msg):
#         print(msg)
# marks= int(input("enter makes"))
# if marks<50:
#     raise ITMError("kash batch 4 me hote")
# else:
#     print("batch 1 will be good fit")




# class ITMError(BaseException):
#     def __init__(self,msg):
#         self.msg=msg
#         print(self.msg)
# marks= int(input("enter makes"))
# if marks<50:
#     raise ITMError("kash batch 4 me hote")
# else:
#     print("batch 1 will be good fit")




# class ITMError(BaseException):
#     def __init__(self,msg):
#         super().__init__(msg)
# marks= int(input("enter makes"))
# if marks<50:
#     raise ITMError("kash batch 4 me hote")
# else:
#     print("batch 1 will be good fit")




# print("start")
# print("line1")
# print("line2")
# try:
#     li=[1,2,3]
#     print(li[6])
# except Exception as e:
#     print("except block")
# else:
#     print("this is else")
# print("line 4")
# print("line 5")



# def divide(x, y):
#     try:
#         result = x // y
#     except ZeroDivisionError:
#         print("You are dividing by zero ")
#     else:
#         print("our answer is :", result)
   
# divide(3, 2)
# divide(3, 0)






