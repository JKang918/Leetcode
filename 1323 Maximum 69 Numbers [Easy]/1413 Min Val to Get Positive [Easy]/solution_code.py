def maximum69Number (num: int) -> int:
    
    numstr = list(str(num))

    for i in range(len(numstr)):
        if numstr[i] == '6':
            numstr[i] = '9'
            break
    
    return int(''.join(numstr))