class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        num_len = len(nums)

        nums_out = []

        for i in range(num_len - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break

            for j in range(i + 1, num_len - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[j] + nums[j + 1] + nums[j + 2] > target - nums[i]:
                    break

                start = j + 1
                end = num_len - 1
                expected_sum = target - nums[i] - nums[j]
                while start < end:
                    cur_sum = nums[start] + nums[end]

                    if cur_sum == expected_sum:
                        nums_out.append((nums[start], nums[end], nums[i], nums[j]))
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
print(test.fourSum([-3,-1,0,2,4,5], 0))
