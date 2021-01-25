//two pointer solution (much faster)

var findClosestElements = function(arr, k, x) {
    let idx = 0;
    while (k < arr.length - idx) {
        const last = arr.pop();
        if (last - x < x - arr[idx]) {
            idx++;
            arr.push(last);
        }
    }
    return arr.slice(idx);
};



//my answer
var findClosestElements = function(arr, k, x) {
    //use binary search to find location
    // take previous/next four values
    //go through substract x from each value and get absolute (save that in subarray)
    //sort by absolute value
    //get numbers in first four array values
    let newArray = []
    
    for(i = 0;i <= arr.length - 1;i++){
       newArray.push([arr[i],Math.abs(arr[i] - x)])
    }
    
    newArray.sort((a1,a2) => a1[1] - a2[1])
    console.log('sorted new Array', newArray)

    
    let result = []
    
    while(k > 0){
        result.push(newArray.shift()[0])
        k-=1
    }
    
    result.sort((a,b) => a - b)
     
    return result
    
};

//my binary search answer

var findClosestElements = function(arr, k, x) {
    //use binary search to find location
    // take previous/next four values
    //go through substract x from each value and get absolute (save that in subarray)
    //sort by absolute value
    //get numbers in first four array values
    
    let index = binarySearch(arr,x,0,arr.length - 1)
    
    let newArray = []
    
    for(i = index - k - 1;i <= index + k + 1;i++){
        console.log('here is i',i)
       if(!!arr[i] || arr[i] == 0) newArray.push([arr[i],Math.abs(arr[i] - x)])
    }
    
    newArray.sort((a1,a2) => a1[1] - a2[1])
    console.log('sorted new Array', newArray)

    
    let result = []
    
    while(k > 0){
        result.push(newArray.shift()[0])
        k-=1
    }
    
    result.sort((a,b) => a - b)
     
    return result
    
};

function binarySearch(arr, x, start = 0, end = arr.length - 1, lastMid = 0) { 
       
    // Base Condition 
    if (start > end) return lastMid; 
   
    // Find the middle index 
    let mid=Math.floor((start + end)/2); 
   
    // Compare mid with given key x 
    if (arr[mid]===x) return mid; 
          
    // If element at mid is greater than x, 
    // search in the left half of mid 
    if(arr[mid] > x)  
        return binarySearch(arr, x, start, mid-1, mid); 
    else
  
        // If element at mid is smaller than x, 
        // search in the right half of mid 
        return binarySearch(arr, x, mid+1, end, mid); 
} 

//faster binary approach (mine)

var findClosestElements = function(arr, k, x) {
    //use binary search to find location
    // take previous/next four values
    //go through substract x from each value and get absolute (save that in subarray)
    //sort by absolute value
    //get numbers in first four array values
    
    let [low,high] = binarySearch(arr,x,0,arr.length - 1)
    console.log('low', low)
    console.log('high', high)
    
    let result = []
    
    while(result.length < k){
        lowestDistance = Math.min(distance(arr,low,x), distance(arr,high,x))
        if(lowestDistance == distance(arr,low,x)){
            result.unshift(arr[low])
            low--
            if(low < 0) low = -Infinity
        }else{
            result.push(arr[high])
            high++
            if(high >= arr.length) high = Infinity
        }

    }
    
    return result
    
};

function distance(arr,index,x){
    let result = Math.abs(arr[index] - x)
    if(!Number.isNaN(result)){
       return result
        }else{
        return Infinity
    }
}

function binarySearch(arr, x, start, end) { 
    if(start  < 0 || end < 0) return [0,1]
    if(start > arr.length - 1 || end > arr.length - 1) return [arr.length - 2, arr.length - 1]
       
   
    // Find the middle index 
    let mid=Math.floor((start + end)/2); 
   
    // Compare mid with given key x 
    if (arr[mid]===x) return [mid,mid+1]; 
    
    if(arr[mid] < x && arr[mid + 1] > x) return [mid, mid+1];
    
    if(arr[mid] > x && arr[mid - 1] < x) return [mid - 1, mid];

          
    // If element at mid is greater than x, 
    // search in the left half of mid 
    if(arr[mid] > x)  
        return binarySearch(arr, x, start, mid-1); 
    else
  
        // If element at mid is smaller than x, 
        // search in the right half of mid 
        return binarySearch(arr, x, mid+1, end); 
} 