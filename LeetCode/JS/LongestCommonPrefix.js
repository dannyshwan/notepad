/**
 * @param {string[]} strs
 * @return {string}
 *
 * Solved by: Daniel Shwan
 */
var longestCommonPrefix = function(strs) {
    var char;
    var prefix = "";
 
    if(strs.length == 0){return prefix;}
 
    for(var i = 0; i < strs[0].length; i++){
        char = strs[0][i];
 
        for(var s in strs){
            if(strs[s][i] != char){
                return prefix;
            }
        }
        prefix = prefix.concat(char);
    }
     
    return prefix;
 };