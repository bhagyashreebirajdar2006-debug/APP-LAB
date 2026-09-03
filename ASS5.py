def topdown(w, v, c, n, dp):
    if n == 0 or c == 0:
        return 0
    if dp[n][c] != -1:
        return dp[n][c]

    if w[n-1] <= c:
        dp[n][c] = max(
            v[n-1] + topdown(w, v, c-w[n-1], n-1, dp),
            topdown(w, v, c, n-1, dp)
        )
    else:
        dp[n][c] = topdown(w, v, c, n-1, dp)

    return dp[n][c]

def bottomup(w, v, c):
    n = len(w)
    dp = [[0]*(c+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(c+1):
            if w[i-1] <= j:
                dp[i][j] = max(
                    v[i-1] + dp[i-1][j-w[i-1]],
                    dp[i-1][j]
                )
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][c]


w = list(map(int, input("Weights: ").split()))
v = list(map(int, input("Values: ").split()))
c = int(input("Capacity: "))

n = len(w)
dp = [[-1]*(c+1) for _ in range(n+1)]

print("Top-Down:", topdown(w, v, c, n, dp))
print("Bottom-Up:", bottomup(w, v, c))
