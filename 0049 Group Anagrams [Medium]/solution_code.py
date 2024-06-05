def groupAnagrams(strs: list[str]) -> list[list[str]]:
    
    lettdict = dict()
    
    for i in range(len(strs)):
        if "".join(sorted(list(strs[i]))) not in lettdict:
            lettdict["".join(sorted(list(strs[i])))] = [strs[i]]
        else:
            lettdict["".join(sorted(list(strs[i])))].append(strs[i])
    

    return list(lettdict.values())