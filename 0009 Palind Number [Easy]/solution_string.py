def isPalindrome(x: int) -> bool:
    
    x = str(x)  #turn int x into string
    x = list(x) #parse string x
    
    #two pointers
    left = 0
    right = len(x) - 1

    while left < right and left < len(x) and right >= 0:
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1
    
    return True
    