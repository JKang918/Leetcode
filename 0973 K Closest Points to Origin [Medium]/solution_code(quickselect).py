from typing import List
import random

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:

    #dictionary: pointIndex - distance of points[pointIndex] from origin
    n = len(points)
    distance = {i: points[i][0]**2 + points[i][1]**2 for i in range(n)}
    
    #input values are pointIndex
    def partition(left: int, right: int, pivot_pointIndex: int) -> int:

        #pivot point's distance from origin
        pivot_dist = distance[pivot_pointIndex]

        #push pivot point to the end of the given section (left, right) of points
        #do not forget to change the dictionary of distances accordingly
        points[pivot_pointIndex], points[right] = points[right], points[pivot_pointIndex]
        distance[pivot_pointIndex], distance[right] = distance[right], distance[pivot_pointIndex]

        #sorting
        store_pointIndex = left
        for i in range(left, right):
            #if a points[i]'s distance from origin is smaller than that of pivot
            if distance[i] < pivot_dist:
                #swap points[i] with points[store_pointIndex
                #do not forget to change the dictionary of distances accordingly
                points[i], points[store_pointIndex] = points[store_pointIndex], points[i]
                distance[i], distance[store_pointIndex] = distance[store_pointIndex], distance[i]
                store_pointIndex += 1
        #end of for loop
        #all points with smaller distances will be located in points[0] ... points[store_pointIndex - 1]
        #pivot will be at points[right]

        #swap points[right] (= pivot) with points[store_pointIndex]
        #pivot will be points[sotre_pointIndex] with all smaller distance points to the left of itself
        points[right], points[store_pointIndex] = points[store_pointIndex], points[right]
        distance[right], distance[store_pointIndex] = distance[store_pointIndex], distance[right]

        #return the pointIndex of pivot 
        return store_pointIndex

    def quickselect(left: int, right: int, k_closest: int) -> None:

        #no sorting required
        if left == right:
            return

        #otherwise
        #pick random pivot point
        pivot_pointIndex = random.randint(left, right)

        #sorting in order of distance from origin
        pivot_pointIndex = partition(left, right, pivot_pointIndex)

        #if pivot is at the target index
        if pivot_pointIndex == k_closest:
            return

        #otherwise
        #if pivot comes after the target index
        #do sorting again in the section that comes before pivot_pointIndex
        elif k_closest < pivot_pointIndex:
            quickselect(left, pivot_pointIndex - 1, k_closest)

        #otherwise
        #if pivot comes before the target index
        #do sorting again in the section that comes after pivot_pointIndex
        else:
            quickselect(pivot_pointIndex + 1, right, k_closest)
        
        return

    #0-index: points[k - 1] would be the k - closest point
    quickselect(0, n - 1, k - 1)

    #points[ : k] = points[0], points[1], ... , points[k -1] -> k-closest points
    return points[ : k]