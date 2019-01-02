/**
 * @param {number} x
 * @return {number}
 * 
 * Solved by Daniel Shwan
 */
var reverse = function(x) {
    var rNum, rNumStr, isNegative = false;

    if(x < 0){
        isNegative = true;
        rNumStr = (x*-1).toString();
    }
    else{
        rNumStr = x.toString();
    }
    
    rNum = (((rNumStr.split('')).reverse()).join("")).valueOf();

    if((rNum*-1) < -Math.pow(2,31) || rNum >= Math.pow(2,31)){
       return 0;
    }
    else if(isNegative){
        return rNum * -1;
    }
    return rNum;
};