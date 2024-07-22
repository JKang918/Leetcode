from typing import List
import random

def topKFrequent(nums: List[int], k: int) -> List[int]:
    
    #freq: {each num in nums : counts}
    #unique: [each distinct num in nums]

    freq = dict()

    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    
    unique = list(freq.keys())

    ###
    def partition(left: int, right: int, pivot_index: int) -> int:

        #get the frequency of the selected pivot element
        pivot_frequency = freq[unique[pivot_index]]

        #put pivot at the end of the to-be sorted list
        unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

        #iterate from the leftmost element and compare its frequency to that of pivot
        #whenever less frequent element comes up, push it to the left 
        
        store_index = left
        for i in range(left, right):
            #if ith element's frequency is less than that of pivot
            if freq[unique[i]] < pivot_frequency:
                #swap ith element and store_index element                    
                unique[i], unique[store_index] = unique[store_index], unique[i]
                
                #note that i increases regardless but store_index increases only when if statement is run
                store_index += 1
        
        #move pivot (unique[right]) to store_index
        #now, all elements to the left is less frequent than pivot
        unique[right], unique[store_index] = unique[store_index], unique[right]

        #return the index of pivot
        return store_index


    def quickselect(left: int, right: int, k_smallest: int) -> None:

        #base case: the list contains only one element
        if left == right:
            return
        
        #pick a random index for pivot in unique
        pivot_index = random.randint(left, right)

        #Find the pivot position in a sorted list
        pivot_index = partition(left, right, pivot_index)
        
        if k_smallest == pivot_index:
            return
        
        #if pivot is (k+1), ... (k+..) smallest
        elif k_smallest < pivot_index:
            #than gotta find less frequent index
            quickselect(left, pivot_index - 1, k_smallest)
        
        #if pivot is (k-1), ... , (k- ...) smallest
        elif k_smallest > pivot_index:
            #then gotta find more frequent index
            quickselect(pivot_index + 1, right, k_smallest)
        
        return

    n = len(unique)
    quickselect(0, n - 1, n - k)
    

    return unique[n - k:]