var lengthOfLongestSubstring = function(s) {

    var str = s;

    var maxLen = 0,
        curLen = 0,
        curStartPosn = 0,
        curEndPosn = 0;

    var stringLen = str.length;

    this.resetSearch = function (duplicatePosn) {
        curStartPosn = duplicatePosn + 1;
        if (curLen > maxLen) maxLen = curLen;
        curLen = curEndPosn - curStartPosn;
    };

    this.findStr = function (str) {
        var curChar = str.charAt(curEndPosn);

        while (curEndPosn < stringLen) {
            for (var i = curStartPosn; i < curEndPosn; i++) {
                if (str.charAt(i) === curChar) {
                    this.resetSearch(i);
                    break;
                }
            }

            curLen++;
            curEndPosn++;
            curChar = str.charAt(curEndPosn);
        }

        if (curLen > maxLen) maxLen = curLen;
    };

    this.findStr(str);

    return maxLen;
};

console.log(lengthOfLongestSubstring("bbtablud"));


