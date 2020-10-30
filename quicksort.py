
def quicksort(arr, start, end):
    
    if (start<end):
        # print(arr)
        index = partition(arr,start, end)
        # print('\n' + "left ")
        quicksort(arr,start, index-1)
        # print('\n' + "right ")
        quicksort(arr, index+1, end)
        

def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def partition(arr,start, end):
    # print("Partition ")
    # print(arr[start:end+1])
    
    pivot = arr[end]
    i = start
    for j in range (i,end):
        if (arr[j] < pivot):
            swap(arr, j, i)
            i+=1
    
    swap(arr, i, end)
    # print("``````````")
    # print(arr[start:end+1])
    # print ('\n' + str(i) + '\n')

    return i


if __name__ =='__main__':
    arr = [51,4,6,2,1,21]
    
    quicksort(arr,0,len(arr)-1)
   
    print("main ")
    print(arr)
