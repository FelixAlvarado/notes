



// Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k. The same Fibonacci number can be used multiple times.

// The Fibonacci numbers are defined as:

// F1 = 1
// F2 = 1
// Fn = Fn-1 + Fn-2 for n > 2.
// It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to k.
 

// Example 1:

// Input: k = 7
// Output: 2 
// Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
// For k = 7 we can use 2 + 5 = 7.
// Example 2:

// Input: k = 10
// Output: 2 
// Explanation: For k = 10 we can use 2 + 8 = 10.
// Example 3:

// Input: k = 19
// Output: 3 
// Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
/**
 * @param {number} k
 * @return {number}
 */
var findMinFibonacciNumbers = function(k) {
    var fib = [];
	//constructing Fibonacci table
    calcFib(fib,k);
    var count = 0, j = fib.length - 1;
    while(k > 0) 
    { 
        // divide k by j'th Fibonacci term to find number of terms it contributes in sum. 
        count += Math.floor(k / fib[j]); 
        k %= fib[j]; 
        j--; 
    } 
    return count; 

};

var calcFib = function(fib, k) {
    var i = 3, nextTerm = 0;
    fib.push(0); 
	fib.push(1); 
	fib.push(1); 
    while(true) 
	{ 
        nextTerm = fib[i - 1] + fib[i - 2]; 
        if(nextTerm>k){
			return; 
		}
        fib.push(nextTerm); 
        i++; 
	} 
};