/**
 * @param {number} x
 * @return {boolean}
 * 
 * Solved by: Daniel Shwan
 */
var isPalindrome = function(x) {
    var i, num;

    num = x.toString();
    
    for(i = 0; i < num.length/2; i++){

        if(num.charAt(i) != num.charAt(num.length-1-i)){
            return false;
        }
    }
    return true;
};