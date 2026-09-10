from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # From question:
        # strs[i] is made up of lowercase English letters = data structure of 26 spaces

        # defaultdict is a subclass of the built-in Python dict that automatically provides a default value for any key that does not exist yet

        count_dict = defaultdict(list) # 當傳入 list 時，預設值為空串列 []，適合用來把資料分類

        for s in strs:
            count_list = [0] * 26

            for j in s: 
                count_list[ord(j) - ord('a')] += 1

            count_dict[tuple(count_list)].append(s)
        return list(count_dict.values()) 

