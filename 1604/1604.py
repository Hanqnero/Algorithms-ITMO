import heapq

def solve(k, signs):

    sign_counts = [(-count, i + 1) for i, count in enumerate(signs)]
    heapq.heapify(sign_counts)  # Convert list into a heap
    
    result = []
    prev = None 
    
    while sign_counts:
        first = heapq.heappop(sign_counts) 
        if prev and prev[0] < 0:
            heapq.heappush(sign_counts, prev) 
        
        result.append(first[1])
        prev = (first[0] + 1, first[1]) if first[0] <= -1 else None
    
    if prev:
        result += [prev[1]] * -prev[0]
    
    print(" ".join(map(str, result)))
    return result

k = int(input().strip())
signs = list(map(int, input().strip().split()))

solve(k, signs)