# # --> Without Class
        

# from threading import *
# def new():
#     for x in range(10):
#         print("Child Executing", current_thread().getName())
# t1 = Thread(target=new)
# print(current_thread().getName())
# t1.start()
# t1.join()
# print("Bye", current_thread().getName())
		


# #  --> Extending Thread Class
# #      note -> Override two methods (run(), __init__())
      

# from threading import *
# class UserThreadClass(Thread):
# 	def run(self):
# 		for x in range(10):
# 			print("Child - ", current_thread().getName())

# obj = UserThreadClass()
# obj.start()
# obj.join()
# print("Control returned to", current_thread().getName())




# # --> Without Extending Thread Class


# from threading import *
# class UserThreadClass():
# 	def jobOfThread(self):
# 		for x in range(10):
# 			print("Child - ", x)

# obj = UserThreadClass()
# t1 = Thread(target=obj.jobOfThread())
# t1.start()
# t1.join()
# print("Done")

      
	  
  
# # TIME COMAPARISON
    
# # // Without Thread
# from threading import *
# import time

# def job():
# 	for x in range(20):
# 		print(x/2)

# def otherJob():
# 	for x in range(20):
# 		print(x / 10)
# startTime = time.time()

# job()
# otherJob()
# endTime = time.time()
# print(endTime - startTime )
	
	

# # // With Thread
	
# from threading import *
# import time

# def job():
# 	for x in range(20):
# 		print(x/2)

# def otherJob():
# 	for x in range(20):
# 		print(x / 10)

# startTime = time.time()
# thread1 = Thread(target=job())
# thread2 = Thread(target=otherJob())
# thread1.start()
# thread2.start()

# endTime = time.time()

# print(endTime - startTime )



# # RACE CONDITION, SYNCHRONIZATION, LOCKS

# # Code without SYNCHRONIZATION

# import threading
# x = 0
# def thread_task():
# 	global x
# 	for i in range(100000):
# 		x += 1

# def main_task():
#     t1 = threading.Thread(target=thread_task)
#     t2 = threading.Thread(target=thread_task)

#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

# if __name__ == "__main__":
# 	main_task()
# 	print("{0}".format(x))
		
		
		
# # Code with SYNCHRONIZATION
	
# from threading import *
# x = 0
# def laptop(lock):
# 	global x
# 	lock.acquire()
# 	for i in range(1000000):
# 		x += 1
# 	lock.release()

# def main_task():
# 	lock = Lock()
# 	t1 = Thread(target=laptop, args=(lock,))
# 	t2 = Thread(target=laptop, args=(lock,))
# 	t1.start()
# 	t2.start()
# 	t1.join()
# 	t2.join()

# if __name__ == "__main__":
# 	main_task()
# 	print(x)
		



# # Asynchronous MultiThreading


# from threading import Thread,Lock

# class TV:
#     def sony(self, name, l1):
#         print("First", name)
#         l1.acquire()
#         for count in range(1, 100):
#             print(name)
#         l1.release()
#         print("Out First", name)


# class Person1(Thread):
#     def __init__(self,tv,name, l1):
#         super().__init__()
#         self.tv = tv
#         self.name = name
#         self.l1 = l1

#     def run(self):
#         self.tv.sony(self.name,self.l1)

# class Person2(Thread):
#     def __init__(self, tv, name,l1):
#         super().__init__()
#         self.tv = tv
#         self.name = name
#         self.l1 = l1

#     def run(self):
#         self.tv.sony(self.name, self.l1)



# if __name__ == "__main__":
#     tv = TV()
#     l1 = Lock()
#     r = Person1(tv,"rahul", l1)
#     a = Person2(tv,"Abhi", l1)
#     r.start()
#     a.start()