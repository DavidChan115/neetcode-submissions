class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        count_list = [0] * 26

        for i in range(len(s)):
            count_list[ord(s[i]) - ord('a')] += 1
            count_list[ord(t[i]) - ord('a')] -= 1
        
        for i in count_list:
            if i != 0:
                return False
        return True