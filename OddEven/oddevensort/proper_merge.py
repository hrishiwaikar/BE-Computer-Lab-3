import random
import time


def binarysearch(no,arr,left,right):
    if left<=right:
        mid = (left+right)/2
        if no >arr[mid] and no<arr[mid+1]:
            return mid+1
        elif no<arr[mid]:
            return binarysearch(no,arr,left,mid-1)
        elif no>arr[mid]:
            return binarysearch(no,arr,mid+1,right)
    else:
        return -1


def getrank(no,arr):
    if no<arr[0]:
        rank=0
    elif no>arr[len(arr)-1]:
        rank=len(arr)
    else:
        rank=binarysearch(no,arr,0,len(arr)-1)

    return rank


#smartmerge
#takes in two sorted arrs => arr1 and arr2 and merges them

def smartmerge(arr1,arr2):
    mergedict={}
    print arr1
    for index,i1 in enumerate(arr1):
        print index, i1
        #print '\n'+str(i1)
        #print 'index = '+str(index)
        foreignrank=getrank(i1,arr2)
        #print 'foreign = '+str(foreignrank)

        rank= index+foreignrank
        #print rank
        #print 'rank = '+str(rank)
        mergedict[rank]=i1
    #print
    for index,i2 in enumerate(arr2):
        #print '\n' + str(i2)
        #print 'index = ' + str(index)
        foreignrank = getrank(i2, arr1)
        #print 'foreign = ' + str(foreignrank)
        #print i1, foreignrank
        rank = index + foreignrank
        #print rank
        #print 'rank = '+str(rank)
        mergedict[rank] = i2

    mergelist=[]
    #time.sleep(0.1)
    for e in range(len(arr1)+len(arr2)):
        mergelist.append(mergedict[e])

    return mergelist



'''

#edit the size of range to edit the size of arr created to be sorted

def create_unsortedarr(size = None):
    arr=[]
    for i in range(size):
        rno = random.randint(1,5*size)
        while rno in arr:
            rno = random.randint(1,5*size)

        arr.append(rno)
    return arr

arr=create_unsortedarr(10)
arr1=arr[:len(arr)/2]
arr2=arr[len(arr)/2:]
arr1.sort()
arr2.sort()
'''
#arr1=[7, 15, 22, 34, 37]
#arr2=[10, 23, 25, 28, 39]
'''
print arr1
print arr2
time.sleep(0.3)
print smartmerge(arr1,arr2)
'''