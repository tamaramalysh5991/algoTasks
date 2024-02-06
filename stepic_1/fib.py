def fib_digit_(n):
    if n in (0, 1):
        return n
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b

    return (a + b)//10


def fib_digit(n):
    k = 0
    T = [0, 1]
    for i in range(2, n):
        T.append((T[i - 1] + T[i - 2]) % 10)
        k = k + 1
        if (T[i] == 1) and (T[i - 1] == 0):
            break
    return T[(n%k)]

def fib(n):
    if n in (0, 1):
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b
    return b

def fib_mod(n, m):
    fibPrev = 0
    fib = 1
    cached = [fibPrev, fib]

    for curr in range(1, n):
        fibOld = fib
        fib = (fib + fibPrev) % m
        fibPrev = fibOld

        if fibPrev == 0 and fib == 1:
            cached.pop()
            break
        else:
            cached.append(fib)
    return n % len(cached)

def main():
    n = int(6)
    # print(fib(n))
    # print(fib_digit(841645))
    # print(fib_digit(841645))
    # n, m = map(int, input().split())
    # print(fib_mod(n, m))
    print(fib_mod(10, 2))

if __name__ == "__main__":
    main()
