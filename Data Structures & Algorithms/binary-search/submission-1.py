class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lhs = 0
        rhs = len(nums) - 1

        while lhs <= rhs:
            mid = int(lhs + rhs) // 2

            if nums[mid] == target:
                return mid
        
            elif target < nums[mid]:
                rhs = mid - 1
            
            elif target > nums[mid]:
                lhs = mid + 1
                
        return -1
    

        