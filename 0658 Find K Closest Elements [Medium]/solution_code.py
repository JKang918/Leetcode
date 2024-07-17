from typing import List
import heapq

def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    
    distance = dict()

    for i in range(len(arr)):
        #{element's index in array : distance from the very element from x}
        distance[i] = abs(arr[i] - x)
    
    #heap
    dist = []

    for key, value in distance.items():
        #dist[(distance, index)]
        dist.append((value, key))
    
    #min heap for distance
    heapq.heapify(dist)

    #output(answer) array
    ans = []

    #pop the heap for k times
    for _ in range(k):
        #heappop(dist): (distance, index in arr)
        #heappop(dist)[1]: index
        #arr[index]: k-distance element 
        ans.append(arr[heapq.heappop(dist)[1]])

    #in ascending order
    return sorted(ans)
