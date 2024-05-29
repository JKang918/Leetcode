def longestCommonPrefix(strs: list[str]) -> str:
    
    #sort -> lexicographical order
    strs.sort()

    #aswer string
    ans = ""
    
    #compare only the first and the last elements
    for i in range(min(len(strs[0]), len(strs[len(strs)-1]))):
        if strs[0][i] == strs[len(strs)-1][i]:
            ans += strs[0][i]
        else: 
            break
    return ans

strs1 = ["flower","flow","flight"]
result = longestCommonPrefix(strs1)
print(result)