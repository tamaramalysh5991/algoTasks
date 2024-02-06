def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [nums[left], nums[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Test the function
print(two_sum([1, 2, 4, 6, 10], 10))  # Output should be [4, 6]

# Three Sum: Given an array, find all unique triplets that sum up to a specific target value.


def three_sum1(array, target):
    array.sort()
    result = []
    left, right = 0, len(array) - 1
    for i in range(1, len(array)-1):

        while left < right:
            fixed = array[i]
            sum = fixed + array[left] + array[right]
            if sum == target and fixed!= array[left] and fixed != array[right]:
                if [fixed, array[left], array[right]] not in result:
                    result.append([fixed, array[left], array[right]])
                left, right = 0, len(array) - 1
                break
            elif sum < target:
                left +=1
            else:
                right -=1
    return result



def three_sum(arr, target):
    arr.sort()
    result = []

    for i in range(len(arr) - 2):
        fixed = arr[i]

        left = i + 1
        right = len(arr) - 1

        while left < right:
            c_sum = fixed + arr[left] + arr[right]

            if c_sum == target:
                result.append([fixed, arr[left], arr[right]])
                left += 1
                right -= 1
            elif c_sum < target:
                left += 1
            else:
                right -= 1

    return result



def three_sum_final(arr, target):
    arr.sort()
    result = []

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i-1]:  # Skip duplicate fixed elements
            continue

        fixed = arr[i]
        left = i + 1
        right = len(arr) - 1

        while left < right:
            c_sum = fixed + arr[left] + arr[right]

            if c_sum == target:
                result.append([fixed, arr[left], arr[right]])

                # Skip duplicate elements for left and right pointers
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif c_sum < target:
                left += 1
            else:
                right -= 1

    return result

print(three_sum1([1, 3, 4, 2, 5, -1, -2], 6))
print(three_sum([1, 3, 4, 2, 5, -1, -2], 6))
print(three_sum_final([1, 3, 4, 2, 5, -1, -2, 1, 2, 5], 6))
# Here, one triplet that adds up to 6 would be [1, 2, 3]. Another would be [-1, 2, 5].
# These are unique triplets because they are not permutations of each other.


def container_with_most_water(heights):
    """"""


print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))