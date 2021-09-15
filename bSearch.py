#2001203004 - Do The Sang (nhom 5)
#Binary Search in Python
def bSearch(arr,x,low,high):
	while low<=high:
		mid=(low+high)//2
		if arr[mid]==x:
			return mid
		elif arr[mid]<x:
			low=mid+1
		else:
			high=mid-1
	return -1
arr=[3,4,6,7,8,9]
x=4
result=bSearch(arr,x,0,len(arr)-1)
if result!=-1:
   print("Phan tu",arr[result], "xuat hien tai vi tri", result+1)
else:
	print("Khong tim thay.")
