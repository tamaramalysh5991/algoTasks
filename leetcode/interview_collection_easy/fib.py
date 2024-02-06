def fibonacci_of(n):
        if n in {0, 1}:  # Base case
            return n
        return fibonacci_of(n - 1) + fibonacci_of(n - 2)

'''
f0 = 0
f1 = 1
f(n) = F(n-1) + F(n-2)
'''