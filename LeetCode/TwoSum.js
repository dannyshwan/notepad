/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 * 
 * Problem solved by Daniel Shwan
 * Runtime: O(n)
 */
var twoSum = function(nums, target) {
    var i, j;

    for(i = 0; i < nums.length; i++){
        for(j = i+1; j < nums.length; j++){
            if(nums[i]+nums[j] == target){
                return [i,j];
            }
        }
    }
};