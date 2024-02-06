import math
n=10
print(n/(math.log(n,2)))
print (n-math.log(n,2))
print(n*(n**1/2)-n*math.log(n,2))
print(n**2)
print(2**n)
print(math.factorial(n))
print(n**n)


cnt, n = 0, int(input())
for i in range(2, n+1):
    j = 2
    while j*j <= i:
        if not n % j:
            cnt += 1
        j += 1
print(cnt)