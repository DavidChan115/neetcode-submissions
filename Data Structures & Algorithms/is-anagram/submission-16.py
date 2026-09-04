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

        for i in count_array:
            if i != 0:
                return False
        return True
        # False True 唔可以掉轉，因為如果個loop係check i == 0就return True, 咁第一個就會停低
