# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(0,len(arr)):
    if(arr[i] == target):
      return i

  return -1   # not found

array = [5,3,1,4]   
target = 1
print(linear_search(array,target))


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  newArr=arr[:]    
  low = 0
  high = len(newArr)

  if len(newArr) == 0:
    return -1 # array empty
  elif(len(newArr)==1):
    if(target == newArr[0]):
        return arr.index(target)
  else:
    for i in range(low,high):
      middle = int((len(newArr))/2)
      low = 0
      high = len(newArr)-1
      if(target == newArr[middle]):
        return arr.index(target)
      elif(target < newArr[middle]):
        array = newArr[low:middle]
        newArr = array[:]
        
        high = middle
      elif(target > newArr[middle]):
        array = newArr[middle+1:]
        newArr = array[:]        
        low = middle+1

  # TO-DO: add missing code

  return -1 # not found

binaryArray = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]  
print(binary_search(binaryArray,9))


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):

  high=len(arr)
  low=0
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 

  elif len(arr) == 1:

    if target == arr[0]:
      return bin1.index(target)

  else:

    if target == arr[middle]:
      return bin1.index(target)

    elif target<arr[middle]:
      high=middle
      dang = arr[low:high]
      return binary_search_recursive(dang[:],target,low,high)

    elif target>arr[middle]:
      low=middle+1
      dang = arr[low:high]
      return binary_search_recursive(dang[:],target,low,high)

    return 'else'
  return 'wait'  


bin1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]


print(f'fin: {binary_search_recursive(bin1,-3,0,len(bin1))}')
