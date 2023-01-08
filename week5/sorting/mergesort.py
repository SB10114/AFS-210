def mergeSort(nlist):
    
    
    # insert your code to complete the mergeSort function
    if len(nlist) > 1:
        leftArr = nlist[:len(nlist)//2]
        rightArr = nlist[len(nlist)//2:]

        mergeSort(leftArr)
        mergeSort(rightArr)

        i=j=k= 0

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                nlist[k] = leftArr[i]
                i += 1
            else:
                nlist[k] = rightArr[j]
                j += 1
            k+= 1
        
        while i < len(leftArr):
            nlist[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(rightArr):
            nlist[k] = rightArr[j]
            j += 1
            k += 1
    
    print("Merging ",nlist)
    print("Splitting ",nlist)
    

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