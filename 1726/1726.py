from itertools import accumulate

n = int(input())

pairs =  ( list( zip(*(list(map(int, input().split())) for i in range(n))))  )

pairs[0] = sorted(list(pairs[0]))
pairs[1] = sorted(list(pairs[1]))

cumsum_x = list(accumulate(pairs[0]))
cumsum_y = list(accumulate(pairs[1]))

sum = 0
for i in range(1, n):
    sum += -cumsum_x[i-1] + i*pairs[0][i]
    sum += -cumsum_y[i-1] + i*pairs[1][i]

print(sum//(n*(n-1)//2))