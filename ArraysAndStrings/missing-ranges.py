# https://leetcode.com/problems/missing-ranges/
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        len_nums = len(nums)
        result = []
        
        if len_nums == 0:
            if lower == upper:
                result.append(str(lower))
            else:
                result.append(str(lower)+"->"+str(upper))
        else:
            if nums[0]-lower == 1:
                result.append(str(lower))
            if nums[0]-lower > 1:
                result.append(str(lower)+"->"+str(nums[0]-1))
            for i in range(1, len_nums):
                prev = nums[i-1]
                curr = nums[i]
                if curr-prev == 2:
                    result.append(str(prev+1))
                if curr-prev > 2:
                    result.append(str(prev+1)+"->"+str(curr-1))
            if upper-nums[len_nums-1] == 1:
                result.append(str(upper))
            if upper-nums[len_nums-1] > 1:
                result.append(str(nums[len_nums-1]+1)+"->"+str(upper))
        
        
        return result