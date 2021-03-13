lst=[1,2,3,4]
op=[num**2 for num in lst]
print(op)



#find even numbers from list
evens=[num for num in lst if num%2==0]
print(evens)


#common elements from 2 lists
lst1=[1,2,3]
lst2=[2,3,4]
common=[num1 for num1 in lst1 for num2 in lst2 if num1==num2]
print(common)


#pairs from 2 list ie., (1,4)(1,5)(1,6)(1,7)(2,6).......
lst1=[1,2,3]
lst2=[4,5,6,7]
pairs=[(num1,num2) for num1 in lst1 for num2 in lst2]
print(pairs)

#print lst1
lst1=[1,2,3]
list=[num1 for num1 in lst1]
print(list)


#question1
list1=[[10,20],[30,40],[50,60]]
#get output as [10,20,30,40,50]
new_list=[num for lst in list1 for num in lst]
print(new_list)


#question2
list=[4,3,2,6,7,9,8]
#get output as [3,2,1,7,8,10,9]
new=[num-1 if num<5 else num+1 for num in list]
print(new)


#same question2 change is return 5 if 5 is present in the list
list=[4,3,2,6,5,7,9,8]
new=[num-1 if num<5 else num+1 if num>5 else 5 for num in list]
print(new)