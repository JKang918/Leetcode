def longestCommonPrefix(strs: list[str]) -> str:
    
    #lexicographical order
    strs.sort()

    ans = ""

    #only need to compare the first string and the last string
    #iterate for smaller of the two strings' lengths

    for i in range(min(len(strs[0]),len(strs[len(strs)-1]))):
        #if same letter
        if strs[0][i] == strs[len(strs)-1][i]:
            #append
            ans += strs[0][i]
        #if not same letter
        else:
            #just return
            return ans
    #if identical -> return 
    return ans
