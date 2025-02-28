for _ in range(int(input())):
    n, k = map(int, input().split())
    m = n // k
    total = (n-1)*(n) // 2 - (m * (m-1) // 2) * (k - (n%k)) - (m*(m+1) // 2) * (n % k)
    print(total)
