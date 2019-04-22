class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        prev = nums[0]
        i = 1
        for num in nums:
            if num != prev:
                prev = num
                nums[i] = num
                i += 1

        return i


test = Solution()
nums = [1, 1, 2]
print(test.removeDuplicates(nums), nums)
