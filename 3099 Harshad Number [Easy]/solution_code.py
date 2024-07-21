def sumOfTheDigitsOfHarshadNumber(x: int) -> int:
    
    #solution 1
    s = x
    sod = 0

    while s > 0:
        sod += s % 10
        s = s // 10

    if x % sod == 0:
        return sod
    else:
        return -1
    
    """
    #solution 2.
    sod = sum(int(digit) for digit in list(str(x)))
    
    if x % sod == 0:
        return sod
    else:
        return -1
    """