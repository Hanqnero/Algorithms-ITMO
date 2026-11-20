import sys
from collections import defaultdict
import heapq

POWERS = [10**i for i in range(10)]

def get_digit(num, i):
    return (num // POWERS[i]) % 10

def set_digit(num, i, d):
    return num - (get_digit(num, i) * POWERS[i]) + (d * POWERS[i])

def match_prefix(num1, num2):
    matched = 0
    for i in range(9, -1, -1):
        if get_digit(num1, i) == get_digit(num2, i):
            matched += 1
        else:
            break
    return matched

def add_station(num, node_id, stations_map, graph, cost):
    neighbors = set()
    
    for i in range(10):
        curr_digit = get_digit(num, i)
        for d in range(10):
            if d == curr_digit:
                continue
            num2 = num - (curr_digit * POWERS[i]) + (d * POWERS[i])
            if num2 in stations_map:
                c = cost[match_prefix(num, num2)]
                neighbors.add((c, stations_map[num2]))
    
    for i in range(10):
        di = get_digit(num, i)
        for j in range(i + 1, 10):
            dj = get_digit(num, j)
            if di == dj:
                continue
            num2 = num - (di * POWERS[i]) - (dj * POWERS[j]) + (dj * POWERS[i]) + (di * POWERS[j])
            if num2 in stations_map:
                c = cost[match_prefix(num, num2)]
                neighbors.add((c, stations_map[num2]))
    
    stations_map[num] = node_id
    for c, neighbor_id in neighbors:
        graph[node_id].append((neighbor_id, c))
        graph[neighbor_id].append((node_id, c))

def dijkstra(graph, start, n):
    INF = float('inf')
    dist = [INF] * n
    parent = [-1] * n
    dist[start] = 0
    
    heap = [(0, start)]
    visited = set()
    
    while heap:
        d, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor, cost in graph[node]:
            if neighbor not in visited and dist[neighbor] > d + cost:
                dist[neighbor] = d + cost
                parent[neighbor] = node
                heapq.heappush(heap, (dist[neighbor], neighbor))
    
    return dist, parent

def main():
    input = sys.stdin.read().split()
    ptr = 0
    
    n = int(input[ptr])
    ptr += 1
    
    cost = [int(input[ptr + i]) for i in range(10)]
    ptr += 10
    
    stations_map = {}
    graph = defaultdict(list)
    
    for i in range(n):
        num = int(input[ptr])
        ptr += 1
        add_station(num, i, stations_map, graph, cost)
    
    dist, parent = dijkstra(graph, 0, n)
    
    if dist[n-1] == float('inf'):
        print(-1)
        return
    
    print(dist[n-1])
    
    path = []
    node = n-1
    while node != -1:
        path.append(node + 1)
        node = parent[node]
    
    print(len(path))
    print(*reversed(path))

if __name__ == "__main__":
    main() 