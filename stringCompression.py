class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        if len(chars) < 2:
          return len(chars)

        i = 1
        charNum = 1
        prevChar = chars[0]

        for c in chars[1:]:
          if c == prevChar:
            charNum += 1
            chars.pop(i)
          elif charNum > 1:
            for cNum in list(str(charNum)):
                chars.insert(i, cNum)
                i += 1
            charNum = 1
            i += 1
          else:
            i += 1


          prevChar = c

        if charNum > 1:
            for cNum in list(str(charNum)):
                chars.insert(i, cNum)
                i += 1
            charNum = 1

        return len(chars)

