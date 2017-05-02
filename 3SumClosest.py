class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        num_len = len(nums)
        cur_diff = -1

        sum_out = nums[0] + nums[1] + nums[2]

        if num_len == 3:
            return sum_out

        for i in range(num_len - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start = i + 1
            end = num_len - 1
            expected_sum = target - nums[i]
            while start < end:
                cur_sum = nums[start] + nums[end]

                if cur_diff == -1:
                    cur_diff = abs(expected_sum - cur_sum)

                if cur_sum == expected_sum:
                    sum_out = nums[start] + nums[end] + nums[i]
                    return sum_out
                elif cur_sum < expected_sum:
                    new_diff = abs(expected_sum - cur_sum)
                    if new_diff < cur_diff:
                        sum_out = nums[start] + nums[end] + nums[i]
                        cur_diff = new_diff
                    start += 1
                else:
                    new_diff = abs(expected_sum - cur_sum)
                    if new_diff < cur_diff:
                        sum_out = nums[start] + nums[end] + nums[i]
                        cur_diff = new_diff
                    end -= 1

        return sum_out


test = Solution()
print(test.threeSumClosest([1,1,1,0], 100))
