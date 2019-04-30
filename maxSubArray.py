from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None

        temp = 0
        subArraySum = nums[0]
        for num in nums:
            if temp <= 0:
                temp = num
            else:
                temp += num

            if temp > subArraySum:
                subArraySum = temp

        return subArraySum


sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
