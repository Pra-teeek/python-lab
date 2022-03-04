
def bs1(start,end,key,list1):
    try:
        if start<end:
            mid=start+end//2
            print(mid)
            if key==list1[mid]:
                return mid    
            if key<list1[mid]:
                return  bs1(0,mid-1,key,list1)
            elif key>list1[mid]:
                return  bs1(mid+1,end,key,list1)    
    except RecursionError:
        print('RecursionError')

list1=[1,2,3,4,5,6]
# key=int(input("Enter value to search from list"))
a=bs1(0,len(list1)-1,2,list1)
print(a)