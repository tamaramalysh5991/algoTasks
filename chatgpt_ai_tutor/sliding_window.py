def find_averages_of_subarrays(K, arr):
    result = []
    window_sum, window_start = 0.0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'K'
        if window_end >= K - 1:
            result.append(window_sum / K)  # calculate the average
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead

    return result


# print("Averages of subarrays of size K: " + str(find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])))


# Problem: Given a string, find the length of the longest substring without repeating characters.
#
# Example: Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Here's how we can approach it using the sliding window technique:
#
# We start with an empty window at the beginning of the string (let's call the left edge of the window start and the right edge end).
#
# We add characters to the window by moving end one step to the right until we get a repeated character.
#
# When we find a repeated character, we move start one step to the right and remove the character at the left edge of the window.
#
# We keep track of the maximum window size during this process, which is the length of the longest substring without repeating characters.
#
# Try solving this problem and let me know if you face any difficulties! I'll be here to help.

def find_longest_substring_without_repeating_characters(string):
    result = []
    window = []
    window_start = 0
    window_end = 0
    while window_end < len(string):
        if string[window_end] not in window:
            window.append(string[window_end])
            window_end += 1
        else:
            result.append(''.join(window))
            window = window[window_start+1:]
            window_start += 1

    return max(result, key=len)


# print(find_longest_substring_without_repeating_characters("abcabcbb"))
# print(find_longest_substring_without_repeating_characters("acabasssssssssssssss"))


def _find_longest_substring_without_repeating_characters(s):
    window_start = 0
    max_length = 0
    char_index_map = {}

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in char_index_map:
            window_start = max(window_start, char_index_map[right_char] + 1)

        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)

    return max_length



# print(_find_longest_substring_without_repeating_characters("abcabcbb"))
# print(_find_longest_substring_without_repeating_characters("acabasssssssssssssss"))




def find_averages_of_subarrays(K, arr):
    result = []
    window_sum, window_start = 0.0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'K'
        if window_end >= K-1:
            result.append(window_sum/K)  # calculate the average
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead

    return result



#print(find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))




# Problem 1: Maximum Sum Subarray of Size K
#
# Given an array of positive numbers and a positive number ‘k,’ find
# the maximum sum of any contiguous subarray of size ‘k’.
#
# Example:
# Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9 (Subarray with maximum sum is [5, 1, 3])

def find_max_sum_subarray(arr, K):
    result = -float("inf")
    window_sum, window_start = 0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'K'
        if window_end >= K - 1:
            result = max(window_sum, result)  # calculate the average
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead

    return result


# res = find_max_sum_subarray([2, 1, 5, 1, 3, 2], 3)
# print(res)



# Problem 2: Smallest Subarray with a given sum
#
# Given an array of positive numbers and a positive number ‘s,’ find the length of the smallest contiguous subarray
# whose sum is greater than or equal to ‘s’. Return 0 if no such subarray exists.
#
# Example:
# Input: [2, 1, 5, 2, 3, 2], s=7
# Output: 2 (Smallest subarray with a sum greater than or equal to 7 is [5,2])
#
# These problems still utilize the sliding window pattern, but with slight variations.
#
# Give them a shot, and let me know if you need hints or solutions!


def dynamic_sliding_window(arr, target):
    pass


def smallest_subarray_with_given_sum(arr, s):
    length = float("inf")
    window_sum, window_start, window_end = 0, 0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            length = min(length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    if length == float("inf"):
        # in this case when no such subarray exists
        return 0
    return length

res = smallest_subarray_with_given_sum(arr=[2, 1, 5, 2, 3, 2], s=7)
print(res)
print(smallest_subarray_with_given_sum(arr=[], s=-1))