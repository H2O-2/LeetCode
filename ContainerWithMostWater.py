class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start_ptr = 0
        end_ptr = len(height) - 1
        max_area = 0

        while start_ptr < end_ptr:
            start_height = height[start_ptr]
            end_height = height[end_ptr]

            max_area = max(max_area, (end_ptr - start_ptr)*min(start_height, end_height))

            if start_height > end_height:
                end_ptr -= 1
            else:
                start_ptr += 1

        return max_area

''' TIME LIMIT EXCEEDED
        max_height = max(height)
        height_num = len(height)
        i = 0
        max_area = 0

        if height.count(max_height) > 1:
            max_height = -1

        while i < height_num:
            cur_height = height[i]

            if cur_height == max_height:
                i += 1
                continue

            if i < height_num - 1:
                j = height_num - 1

                while j > i and height[j] < cur_height:
                    j -= 1

                if j > i:
                    max_temp = (j - i) * cur_height
                    if max_temp > max_area:
                        max_area = max_temp

            if i > 0:
                k = 0

                while k < i and height[k] < cur_height:
                    k += 1

                if k < i:
                    max_temp = (i - k) * cur_height
                    if max_temp > max_area:
                        max_area = max_temp
            i += 1

        return max_area
'''


test = Solution()
print(test.maxArea([1, 1]))
