from typing import List
import heapq
    
def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
    
    countmap = dict()
    #key: element in arr
    #values: their counts
    for i in range(len(arr)):
        if arr[i] not in countmap:
            countmap[arr[i]] = 1
        else:
            countmap[arr[i]] += 1

    counts = []
    for cnt in countmap.values():
        counts.append(cnt)

    heapq.heapify(counts)
    
    for _ in range(k):
        if counts[0] > 1:
            counts[0] -= 1
        else: #counts[0] == 1
            heapq.heappop(counts)
    
    return len(counts)