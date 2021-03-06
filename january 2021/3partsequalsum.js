// Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

// Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

 

// Example 1:

// Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
// Output: true
// Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
// Example 2:

// Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
// Output: false
// Example 3:

// Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
// Output: true
// Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

// Constraints:

// 3 <= arr.length <= 5 * 104
// -104 <= arr[i] <= 104

var canThreePartsEqualSum = function(arr) {
  //go through array twice
    //first time, get sum and divide by three to get goal sum
    //second time, got through and see if numbers add up to goal some.
    //have counter for everytime we hit sum, reset current sum to zero, for third time, must be at end of array
    
    let target = arr.reduce((a,b) => a+b, 0) / 3
    let count = 0
    let currentSum = 0
    
    arr.forEach((number,i) =>{
        currentSum += number
        if (currentSum === target){
            count += 1
            currentSum = 0
            if(count === 3 && i != arr.length - 1 && target != 0) return false
            if(count > 3 && target != 0) return false
        }
    })
    
    if (count === 3 || (target === 0 && count >= 3)){
        return true
    }else{
        return false
    }
};