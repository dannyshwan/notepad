/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 * 
 * Solved by: Daniel Shwan
 * 
 * I initially did this in binary search. While it was successful on my laptop, it caused an error on leetcode
 */
var searchInsert = function(nums, target) {
    
    if(target > nums[nums.length-1]){
        return nums.length;
    }
    else if(target <= nums[0]){
        return 0;
    }
    else{
        for(var i = 0; i < nums.length; i++){
            if(nums[i] === target || nums[i] > target){
                return i;
            }
        }
    }
};

//ALTERNATE SOLUTION (as far as I can see for now) USING BINARY SEARCH
//If this turns out to not be a solution, please let me know!
function searchInsertRecursion(nums, target) {

    if(target > nums[nums.length-1]){
        return nums.length;
    }
    else if(target <= nums[0]){
        return 0;
    }
    else{
        return searchInsert(nums, target, 0, nums.length);
    }
    
}

function searchInsert(nums, target, start, end){

    if((end-1) === start){
        if((target != end) && (target != start)){
            return end;
        }
        else if(target === start){
            return start;
        }
        return end;
    }
    else{
        const middle = Math.floor((start+end)/2);
        if(target === nums[middle]){
            return middle;
        }
        else if(target > nums[middle]){
            return searchInsert(nums, target, middle, end);
        }
        else{
            return searchInsert(nums, target, start, middle);
        }
    }
}

console.log(searchInsertRecursion([1,3,5,6], 5)); //Should print 2
console.log(searchInsertRecursion([1,3,5,6], 0)); //Should print 0
console.log(searchInsertRecursion([1,3,5,6], 7)); //Should print 4
console.log(searchInsertRecursion([1,3,5,6], 2)); //Should print 1