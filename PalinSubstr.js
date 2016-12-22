var longestPalindrome = function(s) {
    var str = s,
        len = s.length;

    if (len === 0) return "";
    if (len < 2) return str[0];

    var palinStr = "",
        palinLen = 0,
        palinExist = true,
        palinDuplicate = 0;

    for (var i = 0; i < len - 1; i++) {
        for (var j = i + 1; j < len; j++) {

            if (str[i] !== str[j] || j - i + 1 <= palinLen) continue;

            if (palinDuplicate >= 0 && str[i] === str[j - 1]) {
                palinDuplicate++;
            } else {
                palinDuplicate = -1;
            }

            var startPosn = i,
                endPosn = j;
            while (palinDuplicate <= 0 && startPosn < endPosn) {
                startPosn++;
                endPosn--;

                if (str[startPosn] !== str[endPosn]) {
                    palinExist = false;
                    break;
                }
            }

            if (palinExist) {
                palinStr = str.substring(i, j + 1);
                palinLen = palinStr.length;
            } else {
                palinExist = true;
            }
        }
    }

    if (palinLen === 0) palinStr = str[len - 1];

    return palinStr;
};
