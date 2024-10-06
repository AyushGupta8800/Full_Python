tup1=()
print(tup1)

tup2=(1,2,3)
print(tup2)

tup3=(23,'hii',3.14)
print(tup3)

print(tup3.index(3.14))
print(tup3.count("hii"))

res_tup= tup1+tup2
print(res_tup)

res_tup1= tup2+tup3
print(res_tup1)


tuple_inside_list=[(10,20),77]
print(tuple_inside_list[0][0])
# del tuple_inside_list[0][0] 
# TypeError: 'tuple' object doesn't support item deletion

del tuple_inside_list[0]
print(tuple_inside_list)

tuple_inside_list1=[(100,2),77]
tup3=(23,'hii',3.14)
print(tuple_inside_list1[0][1]+ tup3[2])


list_inside_tuple3=(55,[30,40])
list_inside_tuple3[1][1]=12
print(list_inside_tuple3)

del list_inside_tuple3[1][0]
print(list_inside_tuple3)

tup30=()
tup31=(50)
print(tup30+tup31)
# TypeError: can only concatenate tuple (not "int") to tuple

tup30=()
tup31=(50,)
print(tup30+tup31)

print("hi"+2)
print("hi"+2+2)
print(2+"hi"+2)
# TypeError: can only concatenate str (not "int") to str




# ======dictionary===============================

# dic1={}
# print(dic1)

# dic2={1:100}
# print(dic2)

# dic3 = {1:100, 2:200, "k":"v", "k2" : 3.14}
# print(dic3)

# dic4 = {3.14:50}
# print(dic4)

# dic5 = {(1,2,3):100}
# print(dic5)


# dic3={[2,3]:500}
# print(dic3)
# TypeError: unhashable type: 'list'

# dic3={{1:2}:500}
# print(dic3)
# TypeError: unhashable type: 'dict'

# dic4={11:{"ik":"iv"}}
# print(dic4)


#access part
# dic5={11:{"ik":"iv",}}
# print(dic5[11]["ik"]) 
#chaining

#method add

# dic6={}
# dic6.update({10:100})
# print(dic6)

# dic6.update({10:200})
# print(dic6)

# dic6={}
# dic6[10]=500
# print(dic6)

#method remove
# dic1={10:500,11:500}
# dic1.pop(10)
# print(dic1)

# dic7={1:100,2:200,3:300,"ik":"it"}
# dic7.pop(3)
# print(dic7)

# dic7={1:100,2:200,3:300,"ik":"it"}
# dic7.popitem()
# print(dic7)

# del dic7
# # print(dic7)

# dic8={1:100,2:200}
# print(dic8.keys())
# print(dic8.values())

# print(dic8[1]==100)

# ===============SETS=================
# set1={}
# print(set1)

# set1 = {1}
# print(set1)

# set3 = {1, 2.2, "bye"}
# print(set3)

# set5 = {(10,20), 99}
# print(set5)

# TypeError: unhashable type: 'list'
# set6 = {[10,20], 99}
# print(set6)


#methods

# set1={10,12,13}
# set1.add(88)
# print(set1)

# set1.remove(10)
# print(set1)

# del set1
# print(set1)


set2={1,2,3,4,5}
set3={4,5,6,7,8}
set4={2,3}
print(set2.union(set3))

print(set2^set3)

print(set2.union(set3) & set4)




# ===============LOOPS===============

lis=[]
for element in range(6):
    lis.append(element)
print(lis)

i=1
for i in range (5):
    print("ITM")


element=[1,2,3,4,5]
for i in element:
    print(i)
    if i==3:
        print("three")
        
element=[1,2,3,4,5]
for i in element:
    print(i)
    if i==3:
      print("three")
    else:
        print("three")

i=3
if(i==3):
    print("the value is three")
elif(i==4):
    print("the value is four")
else:
    print("false")


lis={element*element for element in range(0,10)}
print(lis)

lis1=[1,2,3,4,5]
lis2=[6,7,8,9,0]
for elements in zip(lis1,lis2):
    print(elements)



for elements_lis1,elements_lis2 in zip(lis1,lis2):
    print(elements_lis1,elements_lis2)


i=14

if i%2==0:
    if i%7==0:
        print("both 2 and 7")
    else:
        print("only2")



s={}
print(type(s))