/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */


var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++){
        let check = target - nums[i];
        if (nums.indexOf(check) != -1 && nums.indexOf(check) != i) {
            return [i, nums.indexOf(check)];
        }
    }
    return [-1, -1]
};

console.log(twoSum([3,3], 6));