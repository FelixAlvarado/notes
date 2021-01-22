// You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

// Example 1:

// Input: amount = 5, coins = [1, 2, 5]
// Output: 4
// Explanation: there are four ways to make up the amount:
// 5=5
// 5=2+2+1
// 5=2+1+1+1
// 5=1+1+1+1+1
// Example 2:

// Input: amount = 3, coins = [2]
// Output: 0
// Explanation: the amount of 3 cannot be made up just with coins of 2.
// Example 3:

// Input: amount = 10, coins = [10] 
// Output: 1

var change = function(amount, coins) {
    if (!amount)    return 1
    
    
    coins.sort((a, b) => b - a)
    
    // key => number of ways
    const map = new Map()
    function toKey(index, remaining) {
        return JSON.stringify([index, remaining])
    }
    
    
    const coinsLen = coins.length
    function countWays(index, remaining) {
        if (remaining === 0)   return 1
        if (index >= coinsLen)  return 0
        
        const key = toKey(index, remaining)
        if (map.has(key))   return map.get(key)
        
        
        let result = 0
        const coin = coins[index]
        for (let coinCount = 0; coinCount * coin <= remaining; coinCount++) {
            const coinTotal = coinCount * coin
            const leftover = remaining - coinTotal
            let subresult = countWays(1 + index, leftover)
            result += subresult
        }
        
        
        map.set(key, result)
        return result
    }
    
    
    let result = countWays(0, amount)
    return result
};