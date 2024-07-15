def isIsomorphic(s: str, t: str) -> bool:
    
    #two-way mapping
    map_s_to_t = dict()
    map_t_to_s = dict()

    #first check they are same length
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        
        #when char in s is already seen
        if s[i] in map_s_to_t:
            #check whether the matching char in t is correct
            if map_s_to_t[s[i]] != t[i]:
                return False
        
        #vice versa for t
        if t[i] in map_t_to_s:
            if map_t_to_s[t[i]] != s[i]:
                return False

        #first match
        map_s_to_t[s[i]] = t[i]
        map_t_to_s[t[i]] = s[i]
    
    return True