var findMedianSortedArrays = function(nums1, nums2) {

        var len1 = nums1.length,
            len2 = nums2.length,
            len = len1 + len2;

        var fullArr = [];

        var pointer1 = 0,
            pointer2 = 0;

        var val1, val2;

        var i = 0;

        while (i < len) {
            val1 = nums1[pointer1];
            val2 = nums2[pointer2];

            if (pointer1 >= len1) {
                fullArr.push(val2);
                pointer2++;
            } else if (pointer2 >= len2) {
                fullArr.push(val1);
                pointer1++;
            } else if (val1 <= val2) {
                fullArr.push(val1);
                pointer1++;
            } else {
                fullArr.push(val2);
                pointer2++;
            }

            i++;
        }

        if (len % 2 === 0) {
            return (fullArr[len / 2] + fullArr[len / 2 - 1]) / 2;
        }

        return fullArr[Math.floor(len / 2)];
};

console.log(findMedianSortedArrays([1,6,10], [2,11]));


