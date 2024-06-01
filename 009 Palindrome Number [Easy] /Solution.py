class Solution:
    def isPalindrome(self, x: int) -> bool:

        #negative num: no palindrome    
        if x < 0:
            return False
        
        #positive single digit: palindrom
        elif x//10 == 0:
            return True
        
        #otherwise
        #xtemp to modify x value leaving the original x intact
        xtemp = x
        
        #xpal being the palindrome number of x
        xpal  = x%10            #store the last digit of x first
        
        while xtemp//10 > 0:    #loop only when x >= 10
            xpal *= 10          #shift digits to the left (last digit of xpal being 0)
            xtemp = xtemp//10   #discard the last digit of x
            xpal += xtemp%10    #the new last digit of x added to the right if xpal

        return x == xpal

#Example
example = Solution()
x1 = 12345
x2 = 12321
print(example.isPalindrome(x1))
print(example.isPalindrome(x2))
