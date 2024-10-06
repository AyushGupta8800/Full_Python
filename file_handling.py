#read operation

# this will print object

# f1=open("file1.txt","r")
# print(f1)


# f1=open("file1.txt","r")
# for data in f1:
#     print(data)


# f1=open("file1.txt","r")
# print(f1.read())


# f1=open("file1.txt","r")
# print(f1.readline())
# print(f1.readline())


# f1=open("file1.txt","r")
# print(f1.readlines())




#write operation

# f1=open("file1.txt","w")
# f1.write("hello")


# f1=open("file1.txt","w")
# f1.writelines(["line1\n","line2\n"])




## append operation


# f1=open("file1.txt","a")
# f1.write("start")
# f1.write("end")


# f1=open("file2.txt","a")
# f1.write("start\n")
# f1.write("end")




# f1=open("file1.txt","r")
# print(f1.read())
# f1.close()    # after close no operation perform
# print(f1.read())


# print("open file")
# f1=open("file1.txt","r")
# # print( 10/0)
# print("read file")
# print(f1.read())
# f1.close()
# # print(f1.read())
# # print("close file")



# try:
#     print("open file")
#     f1=open("file1.txt","r")
#     print( 10/0)
#     print("read file")
#     print(f1.read())
# except Exception as e:
#     f1.close()
#     print("close file")



# try:
#     print("open file")
#     f1=open("file1.txt","r")
#     print( 10/0)
#     print("read file")
#     print(f1.read())
# except Exception as e:
#     print( 10 / 0)
# finally:
#     f1.close()
#     print("close file")




# li=[1,2,3,4,5]
# f1=open("file1.txt","wb")    # rb= write in bytes

# import pickle
# pickle.dump(li,f1)          # dump is a write opration --> li ko f1 main write krna hai in byte form 

# f1.close()

# import pickle
# f1=open("file1.txt","rb")      #rb = read in bytes
# print(pickle.load(f1))         # load is a read operation --> f1 ko read karke outpot dena hai




# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def __str__(self):
#         return self.name + str(self.age)
    
# s1= Student("Ayush",20)
# s2=Student("vishal",21)
# s3=Student("shivansh",22)

# f1=open("file1.txt","wb")
# import pickle
# pickle.dump(s1,f1)
# pickle.dump(s2,f1)
# pickle.dump(s3,f1)
# f1.close()

# f1=open("file1.txt","rb")
# print(pickle.load(f1))
# print(pickle.load(f1))
# print(pickle.load(f1))




# tell and seek

# f1=open("file2.txt","r")
# print(f1.tell())
# print(f1.readline())
# print(f1.tell())
# print(f1.readline())
# print(f1.tell())
# print(f1.readline())
# print(f1.tell())
# print(f1.readline())
# f1.seek(8)
# print(f1.readline())
# print(f1.tell())



# file 1 kaa data file 2 main

# with open("file1.txt","r") as f1, open("file2.txt","w") as f2:
#     f2.write(f1.read())














