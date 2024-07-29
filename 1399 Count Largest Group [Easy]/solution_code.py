from collections import defaultdict

def countLargestGroup(n: int) -> int:

    digits = defaultdict(int)
    
    
    def sumDigits(a: int) -> int:
        sumdig = 0
        while a > 0:
            sumdig += a % 10
            a = a // 10
        return sumdig
    

    for k in range(n):
        sumdig = sumDigits(k + 1)
        digits[sumdig] += 1
    
    size = max(digits.values())
    
    # Count the number of groups with the largest size
    count = sum(1 for count in digits.values() if count == size)
    
    return count