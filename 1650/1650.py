import sys
import heapq


input = sys.stdin.readline

n = int(input())
city_map = {}
city_names = []
money = []
days = []
version = []

person = {}


def add_city(name):
    nonlocal city_map, city_names, money, days, version
    cid = len(city_names)
    city_map[name] = cid
    city_names.append(name)
    money.append(0)
    days.append(0)
    version.append(0)
    return cid


for _ in range(n):
    pname, cname, w = input().split()
    w = int(w)
    if cname not in city_map:
        add_city(cname)
    cid = city_map[cname]
    person[pname] = [w, cid]
    money[cid] += w

heap = []
for cid in range(len(city_names)):
    version[cid] = 1
    heapq.heappush(heap, (-money[cid], cid, 1))

m, k = map(int, input().split())
events = []
for _ in range(k):
    d, pname, dest = input().split()
    events.append((int(d), pname, dest))
events.append((m, None, None))

prev_day = 0


def award(to_day):
    popped = []
    found = []
    seen = set()
    while len(found) < 2 and heap:
        negw, cid, ver = heapq.heappop(heap)

        if ver != version[cid]:
            continue

        if cid in seen:
            continue
        seen.add(cid)
        found.append((-negw, cid))
        popped.append((negw, cid, ver))

    if found:
        top_w, top_c = found[0]
        if len(found) == 1 or top_w > found[1][0]:
            days[top_c] += (to_day - prev_day)

    for negw, cid, ver in popped:
        heapq.heappush(heap, (negw, cid, ver))


for d, pname, dest in events:
    if d != prev_day:
        award(d)
    if pname is None:
        break

    w, old_cid = person[pname]

    if dest not in city_map:
        new_cid = add_city(dest)

    else:
        new_cid = city_map[dest]

    money[old_cid] -= w
    version[old_cid] += 1
    heapq.heappush(heap, (-money[old_cid], old_cid, version[old_cid]))

    money[new_cid] += w
    version[new_cid] += 1
    heapq.heappush(heap, (-money[new_cid], new_cid, version[new_cid]))

    person[pname][1] = new_cid

    prev_day = d

result = [(city_names[cid], cnt)
          for cid, cnt in enumerate(days) if cnt > 0]
result.sort(key=lambda x: x[0])

out = sys.stdout.write
for cname, cnt in result:
    out(f"{cname} {cnt}\n")
