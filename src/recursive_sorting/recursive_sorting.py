# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arr1,arr2):
  elements = len(arr1) + len(arr2)
  merged_arr = [0] * elements

  one = 0
  two = 0
  result = []
  itrack = 0
  for i in range(0,len(merged_arr)):
    print(i)

    if(arr1[one]<arr2[two]):

      if(one == len(arr1)-1 and two<len(arr2)):
        merged_arr[i] = arr1[one]
        result = arr2[two:]
        itrack = i+1
        break
      elif(one==len(arr1)-1 and two==len(arr2)-1):
        merged_arr[i],merged_arr[i+1] = arr1[one],arr2[two]
        break
      else:
        merged_arr[i] = arr1[one]
        if(one<len(arr1)):
          one = one+1

    elif(arr1[one]>arr2[two]):

      if(two == len(arr2)-1 and one<len(arr1)):
        merged_arr[i] = arr2[two]
        result = arr1[one:]
        itrack = i+1
        break
      elif(one==len(arr1)-1 and two==len(arr2)-1):
        merged_arr[i],merged_arr[i+1] = arr2[two],arr1[one]
        break
      else:
        merged_arr[i] = arr2[two]
        if(two<=len(arr2)):
          two = two+1

        

  if(itrack > 0):
    count=0
    for i in range(itrack,len(merged_arr)):
      merged_arr[i]= result[count]
      count = count+1

  return merged_arr 

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    arrLen = len(arr)

    arr1 = []
    arr2 = []
    prevArrLen = arrLen    

    while arrLen > 1:
        if(arrLen%2 ==0):
            prevArrLen = arrLen
            arrLen = int(arrLen/2)-1
        else:
            arrLen = int(arrLen/2)
        arr1 = arr[:arrLen+1]
        arr2 = arr[arrLen+1:prevArrLen]
        return merge(merge_sort(arr1),merge_sort(arr2)) 

    return arr

arr = [38,27,43,3,9,82,10]
print(merge_sort(arr))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
