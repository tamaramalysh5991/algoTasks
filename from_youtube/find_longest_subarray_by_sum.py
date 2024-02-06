

# source https://youtu.be/XFPHg5KjHoo
def solution(target_sum: int, arr: list):
    result = [-1]

    summ = left = right = 0

    while right < len(arr):
        summ += arr[right]
        while left < right and summ > target_sum:
            summ -= arr[left]
            left += 1
        if summ == target_sum and (len(result) == 1 or result[1] - result[0] < right - left):
            result = [left + 1, right + 1]

        right += 1

    return result


print(solution(15, [1,2,3,4,5,0,0,0,6,7,8,9,10]))