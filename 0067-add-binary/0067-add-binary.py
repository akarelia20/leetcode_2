class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum= 0
        carry = 0
        result= ""
        
        index_a = len(a)-1
        index_b= len(b)-1
        
        while index_a >= 0 or index_b >=0 or carry != 0:
            print("a",index_a,"b", index_b)
            if index_a >= 0 and index_b >= 0:
                sum = (int(a[index_a]) + int(b[index_b]))  +carry
                result = str(sum%2)+ result 
                carry = sum//2
                index_a -= 1
                index_b -= 1
            elif index_a >= 0:
                sum = int(a[index_a]) + carry
                result = str(sum%2)+ result
                carry = sum//2
                index_a -=1
            elif index_b >= 0:
                sum  = int(b[index_b])+ carry
                result = str(sum%2)+ result
                carry = sum//2
                index_b -=1
            elif carry > 0:
                result = str(carry)+ result
                carry = 0
            print( "carry", carry, "result", result)
                
                
        return result
                
            
            