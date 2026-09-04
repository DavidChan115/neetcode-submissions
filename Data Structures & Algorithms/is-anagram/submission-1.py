class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):   # check左length先, diff length must means they are not anagram
            return False    

        s_string_list = sorted(s) # string length = n
        t_string_list = sorted(t) # string length = m

        if s_string_list == t_string_list:
            return True
        return False


# Python built-in sorted() time complexity: 
# sorted() -> best: O(n), average/worst: O(n log n)
# since there are two strings with length m and n, the total time complexity would be O(n log n + m log m)

# Space complexity:
# sorted() leaves the original collection untouched and **builds a brand-new sorted list from scratch**, it inherently requires O(n) memory to store the newly created list