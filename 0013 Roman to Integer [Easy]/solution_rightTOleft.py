def romanToInt(s: str) -> int:
        
        
    #solution 2. right to left
    romantable = {
            "I" : 1,        #V, X
            "V" : 5,
            "X" : 10,       #L, C
            "L" : 50,
            "C" : 100,      #D, M
            "D" : 500,
            "M" : 1000
            }
    
    #output integer
    ans = romantable[s[len(s) - 1]] #right most roman letter
    
    #going from back to front
    for right in range(1, len(s)):
        if romantable[s[(len(s) - 1) - right]] < romantable[s[(len(s) - 1) - right + 1]]:
            ans -= romantable[s[(len(s) - 1) - right]]
        else:
            ans += romantable[s[(len(s) - 1) - right]]
    
    return ans