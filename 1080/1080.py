N = int(input())

queue = []

data = [None]+[
    [-1, list(map(int, input().split()))]
    for _ in range(N)
]

for i, node in enumerate(data[1:], start=1):
