def strStr(haystack: str, needle: str) -> int:
    
    n = len(haystack)
    m = len(needle)
    
    #if m > n: no for loop at all
    for window in range(n - m + 1):
        for i in range(m):
            if needle[m] != haystack[window + m]:
                break
            if i == m - 1:                       #the key point of this solution
                return window
            
    
    return -1
    