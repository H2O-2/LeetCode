function ListNode(val) {
    this.val = val;
    this.next = null;
}

// return the result value to put into the linked list
var processNum = function (result, overTen) {
    if (result.val < 10 && !overTen) {
        return result.val;
    } else if (result.val < 9 && overTen) {
        return ++result.val;
    } else if (overTen) {
        result.val++;
    }

    result.val %= 10;
};

var addTwoNumbers = function(l1, l2) {

    var result = null;

    var curNode1 = l1!==null ? l1 : null,
        curNode2 = l2!==null ? l2 : null;

    var endNode, newNode, rawResult;

    var overTen = false;

    while (curNode1 || curNode2) {

        if (!curNode1) newNode = new ListNode(curNode2.val);
        else if (!curNode2) newNode = new ListNode(curNode1.val);
        else newNode = new ListNode(curNode1.val + curNode2.val);

        if (result === null) {
            endNode = newNode;
            result = newNode;
            rawResult = newNode.val;
        } else {
            endNode.next = newNode;
            endNode = newNode;
            rawResult = newNode.val;
        }

        processNum(newNode, overTen);

        if (rawResult >= 10 || (rawResult === 9 && overTen)) {
            overTen = true;
        } else {
            overTen = false;
        }

        if (curNode1) curNode1 = curNode1.next;
        if (curNode2) curNode2 = curNode2.next;

    }

    if (overTen) {
        endNode.next = new ListNode(1);
    }

    return result;

};


console.log(addTwoNumbers(new ListNode(5), new ListNode(5)));

