# with class with inheritance (thread)

# from threading import Thread
# class MyThreadClass(Thread):
#     def run(self):
#         for count in range(1,6):
#             print(count)

# if __name__ == "__main__":
#     th1=MyThreadClass()
#     th1.start()
#     th2=MyThreadClass()
#     th2.start()




## with class without inheritance
   
# from threading import Thread
# class MyThreadClass:
#     def show(self):
#         for count in range(1,6):
#             print(count)

# if __name__ == "__main__":
#     th1=MyThreadClass()
#     th2=MyThreadClass()
#     t1=Thread (target=(th1.show))
#     t2=Thread (target=(th2.show))
#     t1.start()
#     t2.start()




## without class

# from threading import Thread
# def show():
#     for count in range(1,6):
#         print(count)

# if __name__ == "__main__":
#     t1=Thread(target = show)
#     t2=Thread(target = show)
#     t1.start()
#     t2.start()





## sleep method

# from threading import Thread
# import time 
# def show():
#     for count in range(1,6):
#         try:
#             time.sleep(2)
#             print(count)
#         except Exception as e:
#             print(e) 
    
# if __name__ == "__main__":
#     t1=Thread(target = show)
#     t1.start()
#     t2=Thread(target = show)
#     t2.start()



# from threading import Thread
# from time import sleep 
# def show():
#     for count in range(1,6):
#         try:
#             sleep(2)
#             print("th1")
#         except Exception as e:
#             print(e) 
    
# if __name__ == "__main__":
#     t1=Thread(target = show)
#     t1.start()
#     for count in range(1,6):
#         print("main")




## print thread individually

# from threading import Thread
# class MyThread(Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
#     def run(self):
#         for count in range(1,6):
#             print(self.name)

# if __name__ == "__main__":
#     t1=MyThread("Tone")
#     t1.start()
#     t2=MyThread("TTwo")
#     t2.start()



## use join function(niche wala code sahi hai)

# import threading
# class MyThread(threading.Thread):
#     def run(self):
#         for count in range(1,6):
#             print(threading.current_thread)

# if __name__ == "__main__":
#     t1=MyThread()
#     t1.setName("one")
#     t1.start()
#     t1.join()
#     t2=MyThread()
#     t2.setName("two")
#     t2.start()
    


# import threading

# class MyThread(threading.Thread):
#     def run(self):
#         for count in range(1, 6):
#             print(threading.current_thread().getName())  # Call current_thread() and then getName()

# if __name__ == "__main__":
#     t1 = MyThread()
#     t1.setName("one")
#     t1.start()
#     t1.join()

#     t2 = MyThread()
#     t2.setName("two")
#     t2.start()
#     t2.join()









