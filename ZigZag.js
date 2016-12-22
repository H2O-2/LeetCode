var convert = function(s, numRows) {
    if (s.length === 0) return "";

    var strNum = numRows;

    if (s.length < strNum) strNum = s.length;

    if (strNum === 1) return s;

    var strArr = new Array(strNum);

    var curStr = 0;
    var dirIsDown = false;

    this.dirToggle = function () {
        if (dirIsDown) dirIsDown = false;
        else dirIsDown = true;
    };

    for (var i = 0; i < s.length; i++) {
        if (curStr >= strNum - 1 || curStr <= 0) {
            this.dirToggle();
        }

        if (strArr[curStr] === undefined) strArr[curStr] = "";

        strArr[curStr] += s[i];

        if (dirIsDown) curStr++;
        else curStr--;
    }

    var strFinal = "";

    for (var j = 0; j < strArr.length; j++) {
        strFinal += strArr[j];
    }

    return strFinal;
};

