#Program for binary search in python

def binarySearch(arr,l,r,element):

    if(r>=l):
        mid = (l+r)/2

        if arr[mid]==element:
            return mid
        elif element<arr[mid]:
            return binarySearch(arr,l,mid-1,element)
        elif element>arr[mid]:
            return binarySearch(arr,mid+1,r,element)

    else:
        return -1




#Accept numbers
arr= raw_input("\nEnter the numbers :\n").split()

for index,no in enumerate(arr):
    arr[index]=int(no)
#sort them

arr.sort()

#Print them
print arr

element = int(raw_input("\nEnter the number to be searched:\n"))

location = binarySearch(arr,0,len(arr)-1,element)

if location!=-1:
    print "Found at "+str(location)
else:
    print "Not Found"