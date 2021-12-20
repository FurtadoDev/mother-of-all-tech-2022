# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        dict = {}
        
        for i in range(0, len(nums)):
            dict[nums[i]] = i
        
        for i in range(0, len(nums)):
            curr_no = nums[i]
            req_no = target - curr_no
            if dict.has_key(req_no) and dict[req_no] != i:
                result.append(i)
                result.append(dict[req_no])
                break
        
        return result