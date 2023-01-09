def mergeSort(nlist):
    print("Splitting ",nlist) 
    
    # insert your code to complete the mergeSort function
    if len(nlist) > 1:
        leftArr = nlist[:len(nlist)//2] #left side of mid   
        rightArr = nlist[len(nlist)//2:] # right side of mid
        merge(nlist, leftArr, rightArr) # left right merge to return nlist changed into full correct order 

        mergeSort(leftArr) #recursively call nlist left side
        mergeSort(rightArr)# recursively call nlist right side
        merge(nlist, rightArr, leftArr) #merge right and then left into one list in proper order
       
    print("Merging ",nlist)
    

def merge(nlist,lefthalf,righthalf):# compares left to right
    i=j=k=0       #counters I= left J= right K= final list
    while i < len(lefthalf) and j < len(righthalf): #while there are values inside of the list in left and right
        if lefthalf[i] < righthalf[j]: #compare positions
            nlist[k]=lefthalf[i] #put it in list at the left position   
            i=i+1 #increment by +1
        else:
            nlist[k]=righthalf[j] #put it in position at the right of k
            j=j+1
        k=k+1 #increment K in all instancess

    while i < len(lefthalf): #check ig I is less than the length (sorts left side)
        nlist[k]=lefthalf[i] #add left half to final list
        i=i+1 #increment
        k=k+1 #increment K for end list

    while j < len(righthalf): #already sorted left half, merge it to the end on the right side of list (sorts right side only)
        nlist[k]=righthalf[j] #add values on the right side of list to the end of list
        j=j+1 #increment moving down the right side of the list
        k=k+1 #moving position of nlist down to add more values
    return nlist #returns final list

nlist = [ 55 ,  31 ,  26 ,  20 ,  63 ,  7 ,  51 ,  74 ,  81 ,  40 ]
mergeSort(nlist) #call function
print("Sort: ",nlist) #print final list