def longestCommonPrefix(self, strs: list[str]) -> str:
    
    #take the first word as a common prefix
    prefix = strs[0]

    #compare this to all the others starting with the second word
    for i in range(1, len(strs)):
        
        #if the prefix exists in another word in a string list, then it will not be 0
        #so being zero means it is not a common prefix
        while strs[i].find(prefix) != 0:

            #because it is not a common prefix, let's reduce the given prefix by each letter at the end
            prefix = prefix[0: len(prefix) - 1]

            if prefix == "":
                return prefix

    return prefix
    