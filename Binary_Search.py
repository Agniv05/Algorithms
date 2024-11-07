#  Binary Search Algorithm
#  
#  Take a sorted array
#  Calculate length of array
#  Go to the middle of the array
#  If target > middle element perform operations on right side of middle element
#  If target < middle element perform operations on left side of middle element
#  If target = middle element return adress
#  Update middle element on right or left according to problem
#  Perform same operation in search space
#  Until target = middle element


def binary_search(arr, target):
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1
    
    # Loop until the search space is exhausted
    while left <= right:
        # Calculate the middle index of the current search space
        mid = (left + right) // 2
        
        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        
        # If the target is greater than the middle element,
        # adjust the left pointer to search the right half
        elif arr[mid] < target:
            left = mid + 1
        
        # If the target is less than the middle element,
        # adjust the right pointer to search the left half
        else:
            right = mid - 1
    
    # Return -1 if the target is not found in the array
    return -1
