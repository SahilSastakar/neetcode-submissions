class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # key: eg: [1a , 1c, 1t] , 
                     #value: strs corresponding to the char freq in the list which is the key

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            #print(count)
            res[tuple(count)].append(s)
            #print(res)
        return list(res.values())

            

        

    
            








        

       


