def lengthOfLongestSubstring(s: str) -> int:
    
    letset = set()
    ans  = 0
    left = 0
    
    for right in range(len(s)):

        while s[right] in letset:
            letset.remove(s[left])
            left += 1
            
        letset.add(s[right])
        ans = max(ans, right + 1 - left)
    
    return ans