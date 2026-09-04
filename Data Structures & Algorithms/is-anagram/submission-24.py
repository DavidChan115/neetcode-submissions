class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):   # check左length先, diff length must means they are not anagram
            return False 

        count_array = [0] * 26 #即係整一個有26個0嘅list

        for i in range(len(s)):

            count_array[ord(s[i]) - ord('a')] += 1
            count_array[ord(t[i]) - ord('a')] -= 1

            # The Python ord() function returns an integer representing the Unicode code point of a single character
            # 26個字母嘅unicode減a嘅unicode就會出到相應index，唔需要dict去用key value pair記低key係邊個英文字母
            # s加完一個字母，如果t又有，咁就會-返，如果identical最後會出0

        for i in count_array:
            if i != 0:
                return False
        return True
        # False True 唔可以掉轉，因為如果個loop係check i == 0就return True, 咁第一個就會停低


# Time complexity: two for loops:
# first for loop: one for loop, two strings, so the complexity is the length of these two strings O(n+m) (bottleneck)
# second for loop: loop 26 times = constant = O(1)
# 所以complexity係bottleneck嘅O(n+m)

# Space complexity: O(1) since we have at most 26 characters, 題目冇理到其他野所以我地只build一個26 slot list去做
