class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Method 1    
        my_dict = {}
        for i in range(len(nums)):
            if(target - nums[i] in nums[i+1:]):
                my_dict[i] = nums[i]
            if(len(my_dict) and target-nums[i] in my_dict.values()):
                my_dict[i] = nums[i]
            
        # return list(my_dict.keys())
        
        # Method 2
        my_dict = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if(remaining in nums[i+1:]):
                return [i, nums[i+1:].index(remaining) + (i+1)]