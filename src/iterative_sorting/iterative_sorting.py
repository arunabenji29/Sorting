# TO-DO: Complete the selection_sort() function below 
# def selection_sort( arr ):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc) 
             



#         # TO-DO: swap




#     return arr

def selection_sort(arr):
    i = 0
    
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            print(f'i is {i}')
            print(f'j is {j} \n')
            if(arr[i]>arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

            j=j+1
        i=i+1
    return arr

array = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]    
print(selection_sort(array))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    j=0
    for j in range(0,len(arr)-1):
        for i in range(0,len(arr)-1):
            print(f'arr[{i}] is {arr[i]}')
            print(f'arr[{i+1}] is {arr[i+1]} \n')            
            if(arr[i]>arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1]=temp
            i=i+1
        j=j+1
    return arr

array = [7,6,5,4,3,1]
print(bubble_sort(array))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr