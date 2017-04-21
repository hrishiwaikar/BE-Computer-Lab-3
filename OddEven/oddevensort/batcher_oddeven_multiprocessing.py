'''
Batcher's odd even sort in sequential
1.Sort on 1st half
2. Sort on 2nd half
3. Merge on Odd Keys
4. Merge on Even Keys
5. Final merge with adjacent checks
'''
from proper_merge import smartmerge
from sequential_oddeven import seq_oddeven
import multiprocessing


sortedarr={}

def getoddeven(arr):             #TCOMP: O(n)
    odds=[]    #for storing elements at odd locations of arr
    evens=[]   #for storing elements at even locations of arr

    for i in range(len(arr)):
        if i%2==0:
            evens.append(arr[i])
        else:
            odds.append(arr[i])

    return odds,evens

def finalmerge(evens,odds):   #O(n)
    if len(evens)>len(odds):
        larger = evens
        smaller = odds
    else:
        larger=odds
        smaller=evens

    minlength = len(smaller)
    diff = len(larger)-len(smaller)

    final=[]
    for i in range(minlength):
        final.append(evens[i])
        final.append(odds[i])

    final=final+larger[minlength:]

    return final

def oddevenseq_sort(arr,result):
    arr= seq_oddeven(arr)
    for i in range(len(arr)):
        result[i]=arr[i]




def finaloddevencheck(arr):  #O(n)
    for i in range(0,len(arr)-1,2):
        if arr[i]>arr[i+1]:
            temp = arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=temp

    for i in range(1,len(arr)-1,2):
        if arr[i]>arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1]=temp

    return arr

def batcher_multiprocessed(arr):
    arr1=arr[:len(arr)/2]
    arr2 = arr[len(arr)/2:]
    # Sort 1st and second half
    result = multiprocessing.Array('i',len(arr1))
    p1 = multiprocessing.Process(target=lambda : oddevenseq_sort(arr1,result))

    p1.start()

    arr2 = seq_oddeven(arr2)


    p1.join()
    arr1 = [result[i] for i in range(len(arr1))]

    print arr1
    print arr2


    #print arr1
    #print arr2

    #extract list of odd elements and even elements from both arrs
    odds1,evens1 = getoddeven(arr1)
    odds2,evens2 = getoddeven(arr2)
    print odds1 ,odds2
    print evens1,evens2
    #Merge odds1 and odds2
    merged_odds =smartmerge(odds1,odds2)
    print 'Merged odds '+str(merged_odds)

    #Merge evens : evens1 and evens2
    merged_evens = smartmerge(evens1,evens2)
    print 'Merged evens '+str(merged_evens)

    #Finally combine the merged evens and odds alternately
    arr = finalmerge(merged_evens,merged_odds)
    #print arr

    #Final odd even check to see if adjacent elements are in proper order
    return finaloddevencheck(arr)


if __name__=='__main__':
    print batcher_multiprocessed([3,5,7,2,6,8,9,1])