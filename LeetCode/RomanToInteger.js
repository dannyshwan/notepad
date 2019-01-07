/**
 * @param {string} s
 * @return {number}
 * 
 * Solved by: Daniel Shwan
 */
var romanToInt = function(s) {
    var number, i;
    number = i = 0;
    
    while(i < s.length){

        if(value(s.charAt(i+1)) > value(s.charAt(i))){
            number += value(s.charAt(i+1)) - value(s.charAt(i));
            i++;
        }
        else{
            number += value(s.charAt(i));
        }
        i++;
    }
    return number;
};

function value(char){
    
    if(char == 'M'){return 1000;}
    else if(char == 'D'){return 500;}
    else if(char == 'C'){return 100;}
    else if(char == 'L'){return 50;}
    else if(char == 'X'){return 10;}
    else if(char == 'V'){return 5;}
    else if(char == 'I'){return 1;}
    else{return -1;}
}