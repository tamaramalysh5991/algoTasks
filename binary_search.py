def binary_search(array, item):
    """
    """
    low = 0
    high = len(array) - 1

    # While you haven't narrowed it down to one element ...
    while low <= high:
        # ... check the middle element
        mid = (low + high) // 2
        guess = array[mid]
        # Found the item.
        if guess == item:
            return mid
        # The guess was too high.
        if guess > item:
            high = mid - 1
        # The guess was too low.
        else:
            low = mid + 1

    # Item doesn't exist
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))  # => 1

# 'None' means nil in Python. We use to indicate that the item wasn't found.
print(binary_search(my_list, -1))  # => None

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
heapq.heappop()