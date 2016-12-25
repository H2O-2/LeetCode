var MAX_INT = 2147483647;
var MIN_INT = -2147483647;
var MAX_LEN = 10;

var reverse = function(x) {
    var num = x;

    if (num === 0) return 0;

    while (num % 10 === 0) {
        num /= 10;
    }

    var str = num.toString();
    var strReverse = "";

    var i = str.length - 1;

    if (i > MAX_LEN) return 0;

    for (; i >= 0; i--) {
        if(str[i] === '-') strReverse = str[i] + strReverse;

        strReverse += str[i];
    }

    num = parseInt(strReverse);

    if (num > MAX_INT || num < MIN_INT) return 0;

    return num;
};
