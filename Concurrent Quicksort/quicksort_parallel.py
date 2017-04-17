
import time
import threading
import random




def quicksort(arr,left,right):
    #print 'Thread '+str(threading.current_thread())+'is sorting '+str(arr[left:right])
    #print str(left)+' to '+str(right)
    time.sleep(0.3)
    #print time.ctime()
    #print arr
    thread_left=None
    thread_right=None
    if left<right:
        p = partition(arr,left,right)
        #print 'Going Left'
        #quicksort(arr,left,p-1)
        thread_left = threading.Thread(target=lambda :quicksort(arr,left,p-1))
        thread_left.start()
        #print 'Going Right '
        #quicksort(arr,p+1,right)
        thread_right = threading.Thread(target=lambda :quicksort(arr,p+1,right))
        thread_right.start()

        if thread_right!=None:
            thread_right.join()
        if thread_left!=None:
            thread_left.join()






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

'''
numbers = []
for i in range(20):

    rno = random.randint(1,100)
    while rno in numbers:
        rno = random.randint(1, 100)

    numbers.append(rno)

print time.ctime()
print numbers
quicksort(numbers,0,len(numbers)-1)
print time.ctime()
print numbers

'''