from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    
    m = len(matrix)
    n = len(matrix[0])

    left = 0
    right = m * n - 1

    while left <= right :
        mid = (left + right) // 2
        r = mid // n
        c = mid % n
        count += 1

        if matrix[r][c] > target:
            right = mid - 1
        
        elif matrix[r][c] < target:
            left = mid + 1
        
        else: #matrix[r][c] == target:
            return True
    
    return False