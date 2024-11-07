#  Quck Sort Algorithm

#  Input Array
#  if length of array <=1 return array
#  pivot = first/last/random element of array
#  rearrange array such that elements > pivot are on right of pivot and elements < pivot are on left of pivot
#  select pivot in left and right subarrays and perform last operation recursively
#  end recursion wahen size of array becomes 1 (subarrays are completely sorted)
#  return complete array


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]                                              #  Random element selected as pivot
    left = [x for x in arr if x < pivot]                                    #  If element < pivot it goes to left of array
    middle = [x for x in arr if x == pivot]                                 #  Pivot placed in middle
    right = [x for x in arr if x > pivot]                                   #  If element > pivot it goes to right of array
    return quick_sort(left) + middle + quick_sort(right)                    #  Recursively calls function to perform same operation in both subarrays left & right of pivot
                                                                            #  when called again a pivot is selected again in each subarray and sorted and same operation repeated
                                                                            #  Recursion stops once there are no elements to be placed left or right of the most recent pivot
