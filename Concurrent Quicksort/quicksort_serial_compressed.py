
import time


def quicksort(arr,left,right):
    #print 'In partition '+str(arr[left:right])
    time.sleep(0.3)
    #print arr
    if left<right:
        p = partition(arr,left,right)
        quicksort(arr,left,p-1)
        quicksort(arr,p+1,right)




def partition(arr,left,right):

    pivot = left
    l = left+1
    r = right

    while l<=r:
        while l<=r and arr[l]<arr[pivot]:
            l=l+1
        while l<=r and arr[r]>arr[pivot]:
            r=r-1

        if l<=r:
            temp = arr[l]
            arr[l]=arr[r]
            arr[r]=temp
        else:
            break

    #exchange pivot with r
    temp = arr[pivot]
    arr[pivot]=arr[r]
    arr[r]=temp

    return r

#quicksort([9,1,4,11,6,2,5],0,6)