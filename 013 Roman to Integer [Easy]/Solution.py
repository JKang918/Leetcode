class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I'  : 1,
            'IV' : 4,
            'V'  : 5,
            'IX' : 9,
            'X'  : 10,
            'XL' : 40,
            'L'  : 50,
            'XC' : 90,
            'C'  : 100,
            'CD' : 400,
            'D'  : 500,
            'CM' : 900,
            'M'  : 1000 
        }
        
        num = 0 #return value (arabian num)
        ptr = 0 #pointer
        
        while ptr < len(s):
            #if the two concatanate letters are not found in dict key 
            if roman.get(s[ptr:ptr+2], 0) == 0:
                num += roman[s[ptr]]
                ptr += 1
            #if the two concatanate letters are found in dict key
            else:
                num += roman[s[ptr:ptr+2]]
                ptr += 2

        return num
