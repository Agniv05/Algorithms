#  Bubble Sort Algorithm

#  Accept unsorted array
#  n = length of array
#  run a loop from i=0 to n
#     run a loop from j=0 to n-i-1
#        if element on right > element on left
#           replace both elements
#  return sorted array


def bubble_sort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place, so we only go up to n-i-1
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
      #  Return sorted array
      return arr
