import sys
from collections import deque


data = sys.stdin.read().strip().split()

it = iter(data)
N = int(next(it))


adj = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    while True:
        v = int(next(it))
        if v == 0:
            break

        adj[i].append(v)
        adj[v].append(i)


color = [-1] * (N + 1)
color[1] = 0
dq = deque([1])

while dq:
    u = dq.popleft()
    for w in adj[u]:
        if color[w] == -1:
            color[w] = 1 - color[u]
            dq.append(w)
        elif color[w] == color[u]:
            
            print(-1)
            exit()


out = ''.join(str(color[i]) for i in range(1, N + 1))
print(out)
