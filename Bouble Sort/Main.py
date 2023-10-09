def Bsort123(arr: list):
    i = 0
    for _ in range(len(arr)-1): #Loop (array length - 1) times
        i = 0
        while i+1<len(arr): 
            if arr[i+1]<arr[i]: #If next element is bigger:
                temp = arr[i+1] #Add next element value to temp
                arr[i+1] = arr[i] #Change next element to current
                arr[i] = temp #Change current element to temp (previous next element)
            i+=1
    return arr #Return array


print(Bsort123([1,1,1,9,33,8,6,7,6,6,5,4,3,2,1]))

        