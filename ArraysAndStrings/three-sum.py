# https://leetcode.com/problems/3sum/
class Solution(object):
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result_list = []
        len_nums = len(nums)
        nums.sort()
        first_element_seen = set()
        
        for i in range(0, len_nums):  # last index 
            need = 0 - nums[i]
            temp_list = []
            left_idx = i + 1
            right_idx = len_nums - 1
            if nums[i] not in first_element_seen:
                first_element_seen.add(nums[i])
                second_element_seen = set()
                while left_idx < right_idx:
                    if nums[left_idx] + nums[right_idx] < need:
                        left_idx = left_idx + 1
                    elif nums[left_idx] + nums[right_idx] > need:
                        right_idx = right_idx - 1
                    else:
                        if nums[left_idx] not in second_element_seen:
                            second_element_seen.add(nums[left_idx])
                            temp_list.append(nums[i])
                            temp_list.append(nums[left_idx])
                            temp_list.append(nums[right_idx])
                            result_list.append(temp_list)
                            temp_list = []
                        left_idx = left_idx + 1
                        right_idx = right_idx - 1
                        
        return result_list