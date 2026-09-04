class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_string_list = sorted(s)
        t_string_list = sorted(t)

        if s_string_list == t_string_list:
            return True
        return False