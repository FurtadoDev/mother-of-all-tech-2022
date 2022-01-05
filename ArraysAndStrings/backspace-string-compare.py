# https://leetcode.com/problems/backspace-string-compare/
from collections import deque

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # assume result is true
        result = True
        stack_for_s = deque()
        stack_for_t = deque()
        
        for i, c in enumerate(s):
            if c != '#':
                stack_for_s.append(c)
            if c == '#' and stack_for_s:
                stack_for_s.pop()
        
        for i, c in enumerate(t):
            if c != '#':
                stack_for_t.append(c)
            if c == '#' and stack_for_t:
                stack_for_t.pop()

        while stack_for_s and stack_for_t:
            if(stack_for_s.pop() !=  stack_for_t.pop()):
                result = False
                break
        
        if stack_for_s or stack_for_t:
            result = False
            
        return result