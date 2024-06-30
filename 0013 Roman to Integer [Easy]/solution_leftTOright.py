def romanToInt(s: str) -> int:
        
        #solution 1. left to right
    romantable = {
            "I" : 1,        #V, X
            "IV": 4,
            "IX": 9,
            "V" : 5,
            "X" : 10,       #L, C
            "XL": 40,
            "XC": 90,
            "L" : 50,
            "C" : 100,      #D, M
            "CD": 400,
            "CM": 900,
            "D" : 500,
            "M" : 1000
            }

    ans = 0 #output integer
    i = 0   #index
    while i < len(s):
        if i < len(s) - 1 and s[i:i+2] in romantable:
            ans += romantable[s[i:i+2]]
            i += 2
        else:
            ans += romantable[s[i]]
            i += 1

    return ans