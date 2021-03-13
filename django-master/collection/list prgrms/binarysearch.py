arr=[1,2,3,4,6,7,8]
arr.sort()
low=0
flag=0
element=int(input("enter number"))
up=len(arr)-1
while(low<=up):
    mid=(low+up)//2
    if element>arr[mid]:
        low=mid+1
    elif element<arr[mid]:
        up=mid-1
    elif element==arr[mid]:
        flag=1
        break
if flag==0:
    print("element not found")
else:
    print("element found")
