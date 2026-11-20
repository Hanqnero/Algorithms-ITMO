import sys
from decimal import Decimal, getcontext

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    # increase precision so that all intermediate products stay exact
    getcontext().prec = 30

    n = int(next(it))
    m = int(next(it))
    s = int(next(it))
    V = Decimal(next(it))

    edges = []
    for _ in range(m):
        a = int(next(it)); b = int(next(it))
        rab = Decimal(next(it)); cab = Decimal(next(it))
        rba = Decimal(next(it)); cba = Decimal(next(it))
        edges.append((a, b, rab, cab))
        edges.append((b, a, rba, cba))

    # amounts[i] = max money in currency i
    amounts = [Decimal(0)] * (n + 1)
    amounts[s] = V

    # Bellman–Ford: relax all edges exactly n-1 times
    for _ in range(n - 1):
        for u, v, rate, cost in edges:
            bal = amounts[u] - cost
            if bal > 0:
                new_amt = bal * rate
                if new_amt > amounts[v]:
                    amounts[v] = new_amt

    # one more pass: if anything still improves, there's a positive cycle
    for u, v, rate, cost in edges:
        bal = amounts[u] - cost
        if bal > 0 and bal * rate > amounts[v]:
            print("YES")
            return

    print("NO")

if __name__ == "__main__":
    main()
