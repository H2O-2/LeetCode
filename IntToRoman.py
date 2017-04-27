class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_num = [1, 5, 10, 50, 100, 500, 1000]
        roman_char = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        roman_str = ""

        if num in roman_num:
            i = roman_num.index(num)
            return roman_char[i]
        elif num + 10 == 50:
            return "XL"
        elif num + 10 == 100:
            return "XC"

        divide_temp = num
        cur_posn = 1    # current position of the number being calculated

        while divide_temp > 0:
            cur_digit = divide_temp % 10
            divide_temp = divide_temp // 10

            cur_index = 2 * (cur_posn - 1)

            one_str = roman_char[cur_index]
            if cur_posn <= 3:
                five_str = roman_char[cur_index + 1]
                ten_str = roman_char[cur_index + 2]

            temp_str = ""

            if cur_digit == 0:
                pass
            elif cur_digit <= 3:
                i = cur_digit
                while i > 0:
                    temp_str += one_str
                    i -= 1
            elif cur_digit == 4:
                temp_str = one_str + five_str
            elif cur_digit == 5:
                temp_str = five_str
            elif cur_digit == 9:
                temp_str = one_str + ten_str
            else:
                j = cur_digit - 5
                temp_str += five_str
                while j > 0:
                    temp_str += one_str
                    j -= 1

            roman_str = temp_str + roman_str

            cur_posn += 1

        return roman_str

test = Solution()
print(test.intToRoman(49))
