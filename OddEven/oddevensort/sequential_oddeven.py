
def seq_oddeven(arr):
    found = False

    while not found:
        found = True

        for i in range(0,len(arr)-1,2):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
                found=False

        for i in range(1,len(arr)-1,2):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
                found=False

    return arr


