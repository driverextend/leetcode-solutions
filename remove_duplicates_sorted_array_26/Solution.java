package LeetCode.remove_duplicates_sorted_array_26;

import java.util.Arrays;

public class Solution {
    public static int removeDuplicates(int[] nums) {
        int[] solNums = new int[nums.length];
        int k = 0;
        int temp = nums[0];

        for (int i = 0; i < nums.length-1; i++) {
            
            if (nums[i] == nums[i+1]){
                nums[i+1] = -400;
                temp = nums[i];
            } else if (i != 0){
                if (nums[i] == temp){
                    nums[i] = -400;
                }
                if (nums[i+1] == temp){
                    nums[i+1] = -400;
                }
            }
        }

        for (int i = 0; i < solNums.length; i++) {
            if (nums[i] != -400){
                solNums[k] = nums[i];
                nums[k] = solNums[k++];
            }
        }

        return k;
    }

    public static void main(String[] args) {
        int[] nums = {1,1,1};
        System.out.println(removeDuplicates(nums));
        System.out.println(Arrays.toString(nums));
    }

    
}
