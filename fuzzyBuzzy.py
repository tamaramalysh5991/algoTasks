
def fizz_buzz():
    for n in range(1, 101):
        if n % 15 == 0:
            print('FizzBuzz')
            continue
        if n % 3 == 0:
            print('Fizz')
            continue
        if n % 5 == 0:
            print('Buzz')
            continue
        print(n)
    [
        print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i) for i in range(1, 101)
    ]
    for i in range(1, 101):
        print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i)


(fizz_buzz())

from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return next(num for num, count in Counter(sorted(nums)).items() if count == 1)
