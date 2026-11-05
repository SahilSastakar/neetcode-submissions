class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        pref, postf = 1,1
    
        
        for i in range(0 , len(nums) , 1):
            #left -> right move
            output.append(pref)
            pref *= nums[i]
        
            
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postf
            postf *= nums[i]
        return output
    
            
        
