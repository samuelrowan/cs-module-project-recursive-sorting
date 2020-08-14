# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    a,b=0,0
    merged_arr = []

    # Your code here
    while a<len(arrA) and b<len(arrB):
        if arrA[a]<arrB[b]:
            merged_arr.append(arrA[a])
            a+=1
        else:
            merged_arr.append(arrB[b])
            b+=1
    if a==len(arrA):
        merged_arr.extend(arrB[b:])

    else:
        merged_arr.extend(arrA[a:])

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr)<=1:
        return arr
    a = merge_sort(arr[int(:len(arr)/2)])
    b = merge_sort(arr[len(arr)/2:])
    return merge(a, b)
merge_sort([6,8,7,3,5,9])
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

