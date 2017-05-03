class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_num = len(digits)
        if digit_num == 0:
            return []

        num_to_letter = [[' '], ['*'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                         ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        ascii_num = 48

        i = 1
        letters = num_to_letter[ord(digits[0]) - ascii_num]

        while i < digit_num:
            next_letters = num_to_letter[ord(digits[i]) - ascii_num]
            new_letters = []

            for letter in letters:
                for next_letter in next_letters:
                    new_letters.append(letter + next_letter)

            letters = new_letters
            i += 1

        return letters


test = Solution()
print(test.letterCombinations("5"))
