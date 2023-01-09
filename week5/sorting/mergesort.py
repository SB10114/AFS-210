def mergeSort(nlist):
    print("Splitting ",nlist) 
    
    # insert your code to complete the mergeSort function
    if len(nlist) > 1:
        leftArr = nlist[:len(nlist)//2]
        rightArr = nlist[len(nlist)//2:]
        merge(nlist, leftArr, rightArr) 

        mergeSort(leftArr)
        mergeSort(rightArr)
        merge(nlist, rightArr, leftArr)
       
    print("Merging ",nlist)
    

def merge(nlist,lefthalf,righthalf):
    i=j=k=0       
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1

    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    return nlist

nlist = [ 55 ,  31 ,  26 ,  20 ,  63 ,  7 ,  51 ,  74 ,  81 ,  40 ]
mergeSort(nlist)
print("Sort: ",nlist)