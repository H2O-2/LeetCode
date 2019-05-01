from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        tempTargetIndex = -1
        first = 0
        last = len(nums) - 1
        found = False
        while not found and first <= last:
            midIndex = (first + last) // 2
            if nums[midIndex] == target:
                tempTargetIndex = midIndex
                found = True
            elif nums[midIndex] < target:
                first = midIndex + 1
            else:
                last = midIndex - 1

        if tempTargetIndex < 0:
            return [-1, -1]

        targetRange = [tempTargetIndex, tempTargetIndex]

        rangeOpen = True
        leftIndex = tempTargetIndex
        # Left side of the range
        while rangeOpen and leftIndex > 0:
            leftIndex -= 1
            if nums[leftIndex] != target:
                rangeOpen = False
                targetRange[0] = leftIndex + 1
            elif leftIndex == 0:
                rangeOpen = False
                targetRange[0] = leftIndex

        rangeOpen = True
        rightIndex = tempTargetIndex
        # Right side of the range
        while rangeOpen and rightIndex < len(nums) - 1:
            rightIndex += 1
            if nums[rightIndex] != target:
                rangeOpen = False
                targetRange[1] = rightIndex - 1
            elif rightIndex == len(nums) - 1:
                rangeOpen = False
                targetRange[1] = rightIndex

        return targetRange


sol = Solution()
print(sol.searchRange([1,1,2], 1))
