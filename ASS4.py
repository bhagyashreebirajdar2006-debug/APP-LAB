# Fibonacci using Memoization and Tabulation

# Memoization 
memo = {0: 0, 1: 1}

def fibonacci_memo(n):
    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    return memo[n]


def get_series_memo(n):
    return [fibonacci_memo(i) for i in range(n + 1)]


#  Tabulation 
def fibonacci_tab(n):
    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp


n = int(input("Enter n: "))

memo_series = get_series_memo(n)
tab_series = fibonacci_tab(n)

print("\nFibonacci Series using Memoization:")
print(memo_series)

print("\nFibonacci Series using Tabulation:")
print(tab_series)

print("\nFibonacci number at position", n)
print("Using Memoization:", fibonacci_memo(n))
print("Using Tabulation:", tab_series[n])
