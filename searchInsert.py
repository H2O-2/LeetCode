from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        first = 0
        last = len(nums) - 1
        found = False

        while not found and first <= last:
            midIndex = (first + last) // 2
            if nums[midIndex] == target:
                return midIndex

            if nums[midIndex] < target:
                first = midIndex + 1
            else:
                last = midIndex - 1

        return first

sol = Solution()
print(sol.searchInsert([], 10))
