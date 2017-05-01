class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        num_len = len(nums)

        nums_out = []

        for i in range(num_len - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start = i + 1
            end = num_len - 1
            expected_sum = -nums[i]
            while start < end:
                cur_sum = nums[start] + nums[end]

                if cur_sum == expected_sum:
                    nums_out.append((nums[start], nums[end], nums[i]))
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif cur_sum < expected_sum:
                    start += 1
                else:
                    end -= 1

        return nums_out


test = Solution()
print(test.threeSum([-1, 0, 1, 2, -1, -4]))
