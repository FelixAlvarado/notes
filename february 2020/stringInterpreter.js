// did goal parser interpreter question
// You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

// Given the string command, return the Goal Parser's interpretation of command.


var interpret = function(command) {
    let result = ''
    
    for(i = 0;i < command.length;i++){
        if(command[i] == 'G'){
            result += 'G'
        }else if (command[i] == '(' && command[i + 1] == ')'){
            result += 'o'
        }else if(command[i] == '(' && command[i + 1] == 'a'){
            result += 'al'
        }
    }
    
    return result
    
};