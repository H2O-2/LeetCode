from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        substringIndices = []
        strlen = len(s)
        if strlen == 0 or not words:
            return substringIndices

        wordLen = len(words[0])
        originalWordTable = {}
        for word in words:
            if word in originalWordTable:
                originalWordTable[word] += 1
            else:
                originalWordTable[word] = 1
        wordTable = originalWordTable.copy()

        curStartingIndex = 0

        i = 0
        while i < strlen:
            curWord = s[i:(i + wordLen)]
            if curWord in wordTable and wordTable[curWord] > 0:
                wordTable[curWord] -= 1
                i += wordLen
            else:
                i = curStartingIndex + 1
                curStartingIndex = i
                wordTable = originalWordTable.copy()

            if sum(wordTable.values()) == 0:
                wordTable = originalWordTable.copy()
                substringIndices.append(curStartingIndex)
                i = curStartingIndex + 1
                curStartingIndex = i

        return substringIndices


sol = Solution()
print(sol.findSubstring("ababaab", ["ab","ba","ba"]))
