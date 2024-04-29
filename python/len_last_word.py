class Solution:
    def lengthOfLastWord(self, s) -> int:
        s_list = s.split()
        return len(s_list[(len(s_list)-1)])