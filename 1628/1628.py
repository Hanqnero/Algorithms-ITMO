import sys

data = sys.stdin.read().split()
it = iter(data)
m = int(next(it))
n = int(next(it))
k = int(next(it))

# read in unlucky days
pts = [(int(next(it)), int(next(it))) for _ in range(k)]

ans = 0
# map from (i,j) -> 1 if seen in row‐pass, 2 after counting in col‐pass
v_count = {}
dups = 0

# ——— Row‐major sweep ———
# sentinels (1,0) and (m,n+1)
prow = pts + [(1, 0), (m, n+1)]
prow.sort()
for (x0, y0), (x1, y1) in zip(prow, prow[1:]):
    dy = x1 - x0
    dx = y1 - y0 - 1

    if dy == 0:
        # same row -> horizontal gap
        if dx == 1:
            v_count[(x1, y1-1)] = 1
        elif dx > 1:
            ans += 1
    else:
        # gap between different rows
        # left side of row x1
        if y1 == 2:
            v_count[(x1, 1)] = 1
        elif y1 > 2:
            ans += 1
        # right side of row x0
        if y0 == n-1:
            v_count[(x0, n)] = 1
        elif y0 < n-1:
            ans += 1

        # any full empty rows in between become 1-wide horizontal streaks
        if n > 1:
            ans += (dy - 1)
        elif dy == 2:
            # exactly one row of width-1
            v_count[(x1-1, 1)] = 1

# ——— Col‐major sweep ———
# sentinels (0,1) and (m+1,n)
pcol = pts + [(0, 1), (m+1, n)]
pcol.sort(key=lambda t: (t[1], t[0]))
for (x0, y0), (x1, y1) in zip(pcol, pcol[1:]):
    dy = y1 - y0
    dx = x1 - x0 - 1

    if dy == 0:
        # same column -> vertical gap
        if dx == 1:
            key = (x1-1, y1)
            if v_count.get(key, 0) == 1:
                dups += 1
                v_count[key] = 2
        elif dx > 1:
            ans += 1
    else:
        # gap between different columns
        # top side of column y1
        if x1 == 2:
            key = (1, y1)
            if v_count.get(key, 0) == 1:
                dups += 1
                v_count[key] = 2
        elif x1 > 2:
            ans += 1
        # bottom side of column y0
        if x0 == m-1:
            key = (m, y0)
            if v_count.get(key, 0) == 1:
                dups += 1
                v_count[key] = 2
        elif x0 < m-1:
            ans += 1

        # full empty columns in between
        if m > 1:
            ans += (dy - 1)
        elif dy == 2:
            key = (1, y1-1)
            if v_count.get(key, 0) == 1:
                dups += 1
                v_count[key] = 2

# final answer = all >= 2-long streaks + isolated 1x1s
sys.stdout.write(str(ans + dups))
