import sys
import math


def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))

    pts = []
    for idx in range(n):
        x = int(next(it))
        y = int(next(it))
        pts.append([x, y, idx])

    x0, y0 = pts[0][0], pts[0][1]
    for p in pts:
        p[0] -= x0
        p[1] -= y0

    decorated = []
    for x, y, idx in pts:
        ang = math.atan2(y, x)
        dist2 = x*x + y*y
        decorated.append((ang, dist2, x, y, idx))

    _, _, x0, y0, idx0 = decorated.pop(0)
    decorated.sort(key=lambda t: (t[0], t[1]))

    pts = [[x, y, idx] for (_, _, x, y, idx) in decorated]
    pts.insert(0, [x0, y0, idx0])

    s = 0
    for i in range(1, n-1):
        x1, y1, _ = pts[i]
        x2, y2, _ = pts[i+1]
        d1x, d1y = x1 - x0, y1 - y0
        d2x, d2y = x2 - x0, y2 - y0
        cross = d1x*d2y - d1y*d2x
        dot = d1x*d2x + d1y*d2y
        if cross < 0 or (cross == 0 and dot < 0):
            s = i
            break

    # Produce output
    out = [str(n), '1']
    m = n - 1
    for i in range(m):
        j = (s + i) % m + 1
        out.append(str(pts[j][2] + 1))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
