def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]


def fibonacci_tabulation(n):
    if n <= 1:
        return n

    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


n = int(input("Enter the value of n: "))

print("Using Memoisation:", fibonacci_memo(n))
print("Using Tabulation:", fibonacci_tabulation(n))
