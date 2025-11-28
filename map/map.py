#Example 

my_list=[1,2,3,4]

result=list(map(lambda x:x+x, my_list))
print(result)

#example

list1=[1,2,3,4]
list2=[5,6,7,8]

result=list(map(lambda x,y:x+y, list1,list2))
print(result)