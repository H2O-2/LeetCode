from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        # Find pivot element first
        pivotIndex = -1
        first = 0
        last = len(nums) - 1
        foundPivot = False
        while not foundPivot and first < last:
            midIndex = (first + last) // 2
            if nums[midIndex] - nums[midIndex - 1] < 0:
                pivotIndex = midIndex
                foundPivot = True
            elif nums[midIndex + 1] - nums[midIndex] < 0:
                pivotIndex = midIndex + 1
                foundPivot = True
            elif nums[midIndex] - nums[first] <= 0:
                last = midIndex - 1
            else:
                first = midIndex + 1

        # Then find the element
        first = 0
        last = len(nums) - 1
        midIndex = 0

        if nums[midIndex] == target:
            return midIndex

        if nums[midIndex] < target:
            last = pivotIndex - 1 if pivotIndex > 0 else len(nums) - 1
        else:
            first = pivotIndex

        while first <= last:
            midIndex = (first + last) // 2

            if nums[midIndex] == target:
                return midIndex

            if nums[midIndex] < target:
                first = midIndex + 1
            else:
                last = midIndex - 1

        return -1



sol = Solution()
print(sol.search([3,4,5,6,1,2], 2))
# print(sol.search([1], 8))
