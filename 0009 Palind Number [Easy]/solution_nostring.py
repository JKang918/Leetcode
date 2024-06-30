def isPalindrome(x: int) -> bool:
    if x < 0: 
        return False

    xtemp  = x
    xreversed = 0
    while xtemp != 0:
        if xreversed != 0:
            xreversed *= 10             #push to the right
        xreversed += xtemp % 10         #store in xpalin the last digit of x
        xtemp = xtemp // 10             #discard the last digit of x (push to the left)
    
    return x == xreversed