// https://leetcode.com/problems/distance-between-bus-stops/

var distanceBetweenBusStops = function(distance, start, destination) {
    if(start == destination) return 0
    let total = 0
    let position = start
    while(position != destination){
        total += distance[position]
        if(position < distance.length - 1){
            position += 1
        }else{
            position = 0
        }
    }
    
    let total2 = 0
    position = start
    while(position != destination){
        if(position > 0){
            position -= 1
        }else{
            position = distance.length - 1
        }
        total2 += distance[position] 
    }
    
    return Math.min(total,total2)
};