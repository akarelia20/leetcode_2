class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict= {}
        output = []

        for s in strs:
            print(s)
            sorted_string = ''.join(sorted(s))
            
            if sorted_string not in dict:
                dict[sorted_string] = [s]
            else:
                dict[sorted_string].append(s)

            
        for key,val in dict.items():
            output.append(val)
        return output