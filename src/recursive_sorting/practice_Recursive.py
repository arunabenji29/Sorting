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
      print(f'if: one is {one}')
      print(f'if: arr1[one] is {arr1[one]}')
      print(f'if: two is {two}')
      print(f'if: arr2[two] is {arr2[two]}')

      if(one == len(arr1)-1 and two<len(arr2)):
        merged_arr[i] = arr1[one]
        print('19:here')
        result = arr2[two:]
        itrack = i+1
        break
      elif(one==len(arr1)-1 and two==len(arr2)-1):
        print('24:here')
        merged_arr[i],merged_arr[i+1] = arr1[one],arr2[two]
        break
      else:
        print('28:here')
        merged_arr[i] = arr1[one]
        if(one<len(arr1)):
          one = one+1

    elif(arr1[one]>arr2[two]):
      print(f'elif: one is {one}')
      print(f'elif: arr1[one] is {arr1[one]}')
      print(f'elif: two is {two}')
      print(f'elif: arr2[two] is {arr2[two]}')

      if(two == len(arr2)-1 and one<len(arr1)):
        merged_arr[i] = arr2[two]
        print(f'41: elif: if: merged_arr[i] is {merged_arr[i]}')
        print('42:here')
        result = arr1[one:]
        print(f'result is {result}')
        itrack = i+1
        break
      elif(one==len(arr1)-1 and two==len(arr2)-1):
        print('45:here')
        merged_arr[i],merged_arr[i+1] = arr2[two],arr1[one]
        break
      else:
        print('49:here')
        merged_arr[i] = arr2[two]
        print(f'53: elif: else: merged_arr[i] is {merged_arr[i]}')
        if(two<=len(arr2)):
          two = two+1

        

  if(itrack > 0):
    print('55:here')
    count=0
    print(f'67: itrack is {itrack}')
    for i in range(itrack,len(merged_arr)):
      print(f'69: i is {i}')
      print(f'count is {count}')

      merged_arr[i]= result[count]
      count = count+1

  return merged_arr 

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
            print(f'fn merge_sort: arrLen is {arrLen}')
        arr1 = arr[:arrLen+1]
        arr2 = arr[arrLen+1:prevArrLen]
        print(f'fn merge_sort: arr1 in merge sort is {arr1}')
        print(f'fn merge_sort: arr2 in merge sort is {arr2}\n')
        # print(f'fn merge_sort: return merge from merge fn is {merge(merge_sort(arr1),merge_sort(arr2))} \n')       
        return merge(merge_sort(arr1),merge_sort(arr2)) 

    return arr

arr = [38,27,43,3,9,82,10]
print(merge_sort(arr))