'use strict';

/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    var roman_num = [1, 5, 10, 50, 100, 500, 1000];
    var roman_char = ['I', 'V', 'X', 'L', 'C', 'D', 'M'];

    var cur_char = 0;
    var s_len = s.length;
    var roman_number = 0;

    while (cur_char < s_len) {
        var cur_posn = Math.ceil((roman_char.indexOf(s[cur_char]) + 1) / 2),
            cur_index = 2 * (cur_posn - 1);

        var one_str = roman_char[cur_index],
            five_str = roman_char[cur_index + 1],
            ten_str = roman_char[cur_index + 2];

        switch (s[cur_char]){
            case one_str:
                if (cur_char < s_len - 1 && s[cur_char + 1] === ten_str) {
                    roman_number += 9 * Math.pow(10, cur_posn - 1);
                    cur_char += 2;
                } else if (cur_char < s_len - 1 && s[cur_char + 1] === five_str) {
                    roman_number += 4 * Math.pow(10, cur_posn - 1);
                    cur_char += 2;
                } else {
                    roman_number += Math.pow(10, cur_posn - 1);
                    cur_char++;
                }
                break;
            case five_str:
                roman_number += 5 * Math.pow(10, cur_posn - 1);
                cur_char++;
                break;
            default:
                console.log("DEBUG");

        }
    }

    return roman_number;
};

console.log(romanToInt("MMMCMXCIX"));
