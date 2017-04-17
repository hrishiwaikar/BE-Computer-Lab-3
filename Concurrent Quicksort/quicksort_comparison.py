import quicksort_serial_compressed
import quicksort_parallel
import random
import time


numbers = []

for i in range(60):

    rno = random.randint(1,100)
    while rno in numbers:
        rno = random.randint(1, 100)

    numbers.append(rno)

numbers_1=list(numbers)

numbers_2 =list(numbers)

time.sleep(1)
print 'My Serial QuickSort'
print time.ctime()
start = time.time()
print numbers_1
quicksort_serial_compressed.quicksort(numbers_1,0,len(numbers_1)-1)
print 'After serial quicksort '+str(numbers_1)
print time.ctime()
end =time.time()
print 'Time Elapsed : '+str(end-start)+'seconds'


print '\nMy Parallel QuickSort'
print time.ctime()
start = time.time()
print numbers_2
quicksort_parallel.quicksort(numbers_2,0,len(numbers_2)-1)
print 'After my parallel quicksort '+str(numbers_2)
print time.ctime()
end =time.time()
print 'Time Elapsed : '+str(end-start)+'seconds'
