import sys


class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[rx] = ry
            if self.rank[rx] == self.rank[ry]:
                self.rank[ry] += 1
        return True


def main():
    data = sys.stdin.readline().split()
    n, m = map(int, data)

    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))

    # Sort by weight
    edges.sort()

    dsu = DSU(n)
    mst_edges = []
    max_edge = 0

    for w, u, v in edges:
        if dsu.union(u, v):
            mst_edges.append((u, v))
            if w > max_edge:
                max_edge = w
            if len(mst_edges) == n - 1:
                break

    # Output
    out = []
    out.append(str(max_edge))
    out.append(str(len(mst_edges)))
    for u, v in mst_edges:
        out.append(f"{u} {v}")

    sys.stdout.write("\n".join(out))


if __name__ == '__main__':
    main()
