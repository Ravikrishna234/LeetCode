class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
		# left sum at beginning is 0
        left = 0

		# right sum at beginning is total sum of nums
        right = sum(nums)

        for p, val in enumerate(nums):
			# remove pivot from the right sum
            right -= val

            if left == right:
                return p
			
			# if left not equal to right sum, add pivot to the left sum
            left += val

        return -1 