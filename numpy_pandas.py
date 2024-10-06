# shallow (reference) copy

# li1=[1,2,3,4,5]
# li2=li1
# print(li1)
# print(li2)
# li1[0]=99
# print(li1)
# print(li2)


# deep copy

# li1=[1,2,3,4,5]
# li2=li1.copy()
# print(li1)
# print(li2)
# li1[0]=99
# print(li1)
# print(li2)




#======== NUMPY ============

# import numpy as np
# li1= [1,2,3,4,5]
# ar1=np.array(li1)
# print(ar1)
# print(type(ar1))
# ar2=np.array(li1)
# print(ar2)
# print(ar1+ar2)





# ==== creating with dimmention array ====

# import numpy as np
# list1=[1,2,3]
# list2=[4,5,6]
# ar3=np.array([list1,list2])
# print(ar3)


# import numpy as np
# list1=[1,2,3]
# list2=[4,5,6]
# ar3=np.array([[list1],[list2]])
# print(ar3)


# ==== accessing data ====

# import numpy as np
# list1=[1,2,3]
# list2=[4,5,6]
# ar3=np.array([list1,list2])
# print(ar3)
# print(ar3[1][0])



# ==== creating arrays once, zeros, empty ====

# import numpy as np
# arZeros = np.zeros(3, dtype=int)
# print(arZeros)

# import numpy as np
# arOnce = np.ones(4)
# print(arOnce)

# import numpy as np
# arEmpty = np.empty(3)
# print(arEmpty)



# ==== arrange array ====

# import numpy as np
# arArange = np.arange(1,25)
# print(arArange)


# ==== reshape ====

# import numpy as np
# arArange = np.arange(1,25)
# arReshape=arArange.reshape(4,6)
# print(arReshape)


# ==== arange maths method ====

# import numpy as np
# arArangeNew = np.arange(1, 11)
# print(arArangeNew.max())
# print(arArangeNew.min())
# print(arArangeNew.sum())
# print(arArangeNew.mean())




# ==== array info method ====

# import numpy as np
# aboutMyaray=np.arange(1,11).reshape(2,5)
# print(aboutMyaray)
# print(aboutMyaray.ndim)
# print(aboutMyaray.size)
# print(aboutMyaray.shape)



# ==== check address of array elements ====

# import numpy as np
# listId = [1, 2, 3]
# checkIdArray = np.array(listId)
# print(checkIdArray)
# print(id(checkIdArray))
# print(id(checkIdArray[0]))
# print(id(checkIdArray[1]))
# print(id(checkIdArray[2]))


# ==== array Homo or hetro? ====

# import numpy as np
# listId = [1, "Hello", 3.6]
# checkIdArray = np.array(listId)
# print(checkIdArray)


# ==== Slice, find elements based on query, compare elements ====

# import numpy as np
# serachArray = np.arange(20, 35)
# print(serachArray[0:5])
# print(serachArray[serachArray > 30])
# print(serachArray > 30)




# import numpy as np
# from sys import getsizeof

# # memory diff.
# li= range(20)
# print(getsizeof(10)*len(li))

# npArray = np.arange(20)
# print(npArray.size*npArray.itemsize)


# time diff.

# import numpy as np
# import time
# li1= range(20)
# li2= range(20)

# start= time.time()
# nulls=[num1*num2 for num1,num2 in zip(li1,li2)]
# print("total time for list null is -", (time.time() - start)*1000)



# import numpy as np
# import time
# li1=[1,2,3,4]
# li2=[5,6,7,8]
# start= time.time()
# arr1=np.array(li1)
# arr2=np.array(li2)
# print(arr1*arr2)
# print((time.time() - start))







#--------PANDAS--------

# ==== list Series =====

# import pandas as pd
# l1 = [1, 2, 3, 4, 5]
# s1 = pd.Series(l1)
# print(s1)

# ==== dict Series ====

# import pandas as pd
# dict1 = {1:100, 2:200, 3:300}
# s2 = pd.Series(dict1)
# print(s2)


# ==== list DataFrame ====

# import pandas as pd
# l1 = [1, 2, 3, 4, 5]
# df1 = pd.DataFrame(l1)
# print(df1)


# ==== dict DataFrame ====

# import pandas as pd
# dict1 = {1:100, 2:200, 3:300}
# df2 = pd.DataFrame([dict1])
# print(df2)


# ==== multi Objects as Series ====

# ==== list =====

# import pandas as pd
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]
# listMul = [list1, list2]
# sListMul = pd.Series(listMul)
# print(sListMul)


# === multi dictionary as series ====

# import pandas as pd
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dicMul = [dic1, dic2]
# sDicMul = pd.Series(dicMul)
# print(sDicMul)




# ==== multi Objects as DataFrame====

# ==== using list ====

# import pandas as pd
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]
# listMul = [list1, list2]
# dfListMul= pd.DataFrame(listMul)
# print(dfListMul)


# ==== using dictionary ====

# import pandas as pd
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dicMul = [dic1, dic2]
# dfDicMul = pd.DataFrame(dicMul)
# print(dfDicMul)



# import pandas as pd
# dicNames = {"name" : ["vishal", "ayush", "shivansh"],
#             "sname": ["bhgat", "gupta", "pandey"]}
# myNamesDataFrame = pd.DataFrame(dicNames)
# print(myNamesDataFrame)


# ==== Data Indexing ====

# import pandas as pd
# listNew = [1, 2, 3]
# myIndex = range(3)
# dfAboutPara = pd.DataFrame(data=listNew, index=myIndex)
# # dfAboutPara = pd.DataFrame(data=listNew, index=["a", "b", "c"])
# print(dfAboutPara)


# # Data Accessing
# # loc --> Location
# print(dfAboutPara.loc["b"])

# # iloc --> Index Location
# print(dfAboutPara.iloc[1])


# import pandas as pd
# listFindEl1 = [1, 2, 3, 4, 5]
# listFindEl2 = [6, 7, 8, 9, 0]
# findEleList = [listFindEl1, listFindEl2]

# dfFindEle = pd.DataFrame(findEleList)
# print(dfFindEle)
# print("[0][0] location elements -", dfFindEle[0][0])
# # print("[1][2] location elements -", dfFindEle[1][2])            # --> Gives Error
# print("[1][2] location elements -", dfFindEle.iloc[1][2])


# readFile using pandas

# import pandas as pd
# data = pd.read_csv("PlayTennis.csv")
# print(data)

# import pandas as pd
# data.iloc[0]["Temperature"] = "Rainy"
# print(data)




