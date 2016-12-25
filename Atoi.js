var MAX_INT = 2147483647;
var MIN_INT = -2147483648;
var MAX_LEN = 10;

var isNumber = function (c) {
    var numStart = "0";
    var numEnd = "9";
    var curCode = c.charCodeAt(0);

    return ((curCode >= numStart.charCodeAt(0) && curCode <= numEnd.charCodeAt(0)));
};

var myAtoi = function(str) {
    var strToInt = str;

    strToInt = strToInt.trim();

    var strLen = strToInt.length;

    if (strToInt.length === 0 || (!isNumber(strToInt[0]) && strToInt[0] !== '-' && strToInt[0] !== '+') ||
        ((strToInt[0] === '-' || strToInt[0] === '+') && strLen <= 1) ||
        (!isNumber(strToInt[0]) && !isNumber(strToInt[1]))) return 0;

    if (strToInt[0] === '0') {
        var zeroes = 1;
        while (strToInt[zeroes] === '0') {
            zeroes++;
        }

        strToInt = strToInt.slice(zeroes);
        strLen -= zeroes;
    }

    var intOut,
        strOut = "";

    var i = 0;

    if (strToInt[0] === '-' || strToInt[0] === '+') {
        strOut = strToInt[0];
        i++;
    }

    for (; i < strLen; i++) {
        if (!isNumber(strToInt[i])) break;

        strOut += strToInt[i];
    }

    strLen = strOut.length;

    if (strLen - 1 > MAX_LEN) {
        if (strOut[0] === '-') return MIN_INT;

        return MAX_INT;
    }

    intOut = parseInt(strOut);

    if (intOut > MAX_INT) return MAX_INT;
    else if (intOut < MIN_INT) return MIN_INT;

    return intOut;
};

