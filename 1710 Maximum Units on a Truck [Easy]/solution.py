from typing import List
import heapq


def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    
    boxTypes2 = []

    for boxcnt, unit in boxTypes:
        #-unit to simulate max heap
        boxTypes2.append([-unit, boxcnt])
    
    heapq.heapify(boxTypes2)

    totalUnits = 0
    
    #if trucSize == 0 => no left space in truct, skip the loop and return current totalUnits loaded
    #if boxTpyes2 is empty => all loaded but the truck still has some spaces left, skip the loop return current totalUnits loaded
    while truckSize and boxTypes2:
        #unit is negative, boxcnt is positive
        unit, boxcnt = heapq.heappop(boxTypes2)
        
        #still spaces left or perfectly fit
        if (truckSize - boxcnt) >= 0:
            truckSize -= boxcnt #if perfectly fit, would be zero, ending the loop
            #because unit is negative
            totalUnits -= (unit * boxcnt)
        
        #current empty space if not large enough
        else:
            totalUnits -= (unit * truckSize)
            truckSize = 0

    return totalUnits