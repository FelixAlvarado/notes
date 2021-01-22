// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

// Example 1:


// Input: l1 = [2,4,3], l2 = [5,6,4]
// Output: [7,0,8]
// Explanation: 342 + 465 = 807.
// Example 2:

// Input: l1 = [0], l2 = [0]
// Output: [0]
// Example 3:

// Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
// Output: [8,9,9,9,0,0,0,1]
 

// Constraints:

// The number of nodes in each linked list is in the range [1, 100].
// 0 <= Node.val <= 9
// It is guaranteed that the list represents a number that does not have leading zeros.

var addTwoNumbers = function(l1, l2) {
    let carry = 0
    let result = false
    let pointer
    while(!!l1 || !!l2){
        if(!l1) l1 = new ListNode()
        if(!l2) l2 = new ListNode()
        let current1 = (l1.val == undefined) ? 0 : l1.val
        let current2 = (l2.val == undefined) ? 0 : l2.val
        if (!result) {
            result = new ListNode()
            result.next = new ListNode()
            pointer = result.next
        }else{
            pointer.next = new ListNode()
            pointer = pointer.next
        }
        pointer.val = (carry + current1 + current2) % 10
        carry = carry + current1 + current2 >= 10 ? 1 : 0
        l1 = !!l1 ? l1.next : null
        l2 = !!l2 ? l2.next : null
        console.log('result', result)
    }
    if(carry == 1){
            pointer.next = new ListNode()
            pointer.next.val = 1
    }
    return result.next
};