class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            if(target - nums[i] in nums[i+1:]):
                my_dict[i] = nums[i]
            if(len(my_dict) and target-nums[i] in my_dict.values()):
                my_dict[i] = nums[i]
            #elif(len(my_dict) and target-nums[i] in my_dict.values()):
                #my_dict[i] = nums[i]
            #else:
                #pass
            
        return list(my_dict.keys())
#class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
        #my_dict = {}
        #for i in range(len(nums)):
            #if(len(my_dict) and target-nums[i] in my_dict.values()):
                #my_dict[i] = nums[i]
            #else:
                #my_dict[i] = nums[i]
        #return list(my_dict.keys())