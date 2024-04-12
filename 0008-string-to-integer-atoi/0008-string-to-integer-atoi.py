class Solution:
    def myAtoi(self, s: str) -> int:
        # strip the white spaces
        s = s.strip()
        
        # if the string is non-empty
        if s == "":
            return 0
        
        # check if "-" exsist in the begining and if so  you will have sign variable change to -1 from 1(default)
        sign = 1
        num = 0
        m = 0
        
        if s[0].isnumeric() == False and s[0] == "-" :
            sign = -1
            m+=1
    
        
        for i in range(m, len(s)):
            if i == 0 :
                if s[i] =="+":
                    continue
            if s[i].isnumeric() == True:
                num = num*10 + int(s[i])
                # print(num)
            else:
                break
     
        if num < 2**31 and num > -2**31:
            return num*sign
        else:
            return sign*(2**31) if sign == -1 else sign*(2**31)-1