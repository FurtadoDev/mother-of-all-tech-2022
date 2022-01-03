# https://leetcode.com/problems/next-permutation/
class Solution(object):
     
    def swap(self, nums, idx1, idx2):
        temp = nums[idx1]
        nums[idx1] = nums[idx2]
        nums[idx2] = temp
        
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        len_list = len(nums)
        last_idx = len_list - 1
        
        if len_list == 2:
            if nums[0] < nums[1]:
                self.swap(nums, 0, 1)
            else:
                nums[0:] = sorted(nums[0:])
        
        if len_list > 2:
            if nums[last_idx - 1] < nums[last_idx]: # case 1 : increasing case
                self.swap(nums, last_idx-1, last_idx)
            elif nums[last_idx-1] > nums[last_idx]: # case 2: decreasing and increasing/or only decreasing
                left_idx = last_idx-1
                right_idx = last_idx
                while(left_idx > 0):
                    if nums[left_idx] < nums[right_idx]:
                        break
                    else:
                        left_idx = left_idx-1
                        right_idx = right_idx-1
                if left_idx == 0:
                    if nums[0] > nums[1]:
                        nums[0:] = sorted(nums[0:])
                    else:
                        temp_idx = last_idx
                        while(temp_idx > left_idx):
                            if nums[temp_idx] > nums[left_idx]:
                                break
                            else:
                                temp_idx = temp_idx-1
                        self.swap(nums, temp_idx, left_idx)
                        nums[right_idx:] = sorted(nums[right_idx:])    
                else:
                    temp_idx = last_idx
                    while(temp_idx > left_idx):
                        if nums[temp_idx] > nums[left_idx]:
                            break
                        else:
                            temp_idx = temp_idx-1
                    self.swap(nums, temp_idx, left_idx)
                    nums[right_idx:] = sorted(nums[right_idx:])
            else:
                left_idx = last_idx-1
                right_idx = last_idx
                while(left_idx > 0):
                    if nums[left_idx] != nums[right_idx]:
                        break
                    else:
                        left_idx = left_idx-1
                        right_idx = right_idx-1
                if left_idx == 0:
                    if nums[0] > nums[1]:
                        nums[0:] = sorted(nums[0:])
                else:
                    if nums[left_idx] < nums[right_idx]:
                        self.swap(nums, left_idx, right_idx) # since all the consecutive right elements are the same
                        nums[right_idx:] = sorted(nums[right_idx:])      
                    else: #nums[left_idx] > nums[right_idx]:
                        temp_idx = left_idx - 1
                        while(temp_idx > 0):
                            if nums[temp_idx] >= nums[temp_idx+1]:
                                temp_idx = temp_idx - 1
                            else:
                                break
                        if temp_idx == 0 and nums[0] >= nums[1]:
                            nums[0:] = sorted(nums[0:])
                        else:
                            temp_idx1 = last_idx
                            while(temp_idx1 > temp_idx):
                                if nums[temp_idx1] > nums[temp_idx]:
                                    self.swap(nums, temp_idx1, temp_idx)
                                    nums[temp_idx+1:] = sorted(nums[temp_idx+1:])
                                    break
                                else:
                                    temp_idx1 = temp_idx1-1
                            
        return nums