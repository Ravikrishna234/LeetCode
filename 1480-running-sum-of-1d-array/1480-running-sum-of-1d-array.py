class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        runSum = list()
        for ele_ in nums:
            sum += ele_
            runSum.append(sum)
        return runSum    