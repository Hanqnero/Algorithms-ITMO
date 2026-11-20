import sys
from array import array

def main():
    data = sys.stdin.buffer.readline().split()
    n = int(data[0]); K = int(data[1])

    bit = array('I', [0]) * (n + 1)
    for i in range(1, n+1):
        bit[i] += 1
        j = i + (i & -i)
        if j <= n:
            bit[j] += bit[i]

    max_mask = 1 << (n.bit_length() - 1)

    out = []
    append = out.append

    idx = 0
    rem = n

    bit_arr = bit
    n_local = n
    K_local = K

    for _ in range(n_local):
        idx = (idx + K_local - 1) % rem
        target = idx + 1

        pos = 0
        mask = max_mask
        bit_local = bit_arr
        while mask:
            nxt = pos + mask
            if nxt <= n_local and bit_local[nxt] < target:
                target -= bit_local[nxt]
                pos = nxt
            mask >>= 1
        pos += 1

        append(str(pos))

        j = pos
        while j <= n_local:
            bit_local[j] -= 1
            j += j & -j

        rem -= 1

    sys.stdout.write(" ".join(out))

if __name__ == "__main__":
    main()
