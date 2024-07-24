from typing import List
import random

def findKthLargest(nums: List[int], k: int) -> int:

    
    def partition(left, right, pivot_index):
        
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        store_index = left
        for i in range(left, right):
            if nums[i] > pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        nums[store_index], nums[right] = nums[right], nums[store_index]
        
        return store_index

    def quickselect(left, right, k_largest) -> None:
        
        if left == right:
            return
        
        pivot_index = random.randint(left, right)

        pivot_index = partition(left, right, pivot_index)

        if pivot_index == k_largest:
            return
        elif pivot_index > k_largest:
            quickselect(left, pivot_index - 1, k_largest)
        else:
            quickselect(pivot_index + 1, right, k_largest)
        
        return

    n = len(nums)
    quickselect(0, n - 1, k - 1)
    return nums[k - 1]        