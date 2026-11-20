import sys
from collections import deque


def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N, M = int(next(it)), int(next(it))

    adj = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)

    for _ in range(M):
        x, y, c = int(next(it)), int(next(it)), int(next(it))
        adj[x].append((y, c))
        indegree[y] += 1

    S, F = int(next(it)), int(next(it))

    NEG_INF = -10**18
    dist = [NEG_INF] * (N+1)
    dist[S] = 0

    q = deque(i for i in range(1, N+1) if indegree[i] == 0)

    while q:
        u = q.popleft()

        for v, w in adj[u]:
            dist[v] = max(dist[v], dist[u] + w)
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if dist[F] >= 0:
        sys.stdout.write(str(dist[F]))
    else:
        sys.stdout.write("No solution")


if __name__ == "__main__":
    main()
