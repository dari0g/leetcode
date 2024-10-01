"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""

class Solution:
    def majorityElement(self, nums) -> int:
        num_set = set(nums)
        max_val = 0
        max_element = None

        for num in num_set:
            if nums.count(num) > max_val:
                max_val = nums.count(num)
                max_element = num
        
        return max_element