from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # defaultdict與普通字典唯一的區別在於：當你存取一個不存在的Key時，它不會拋出 KeyError 異常，而是會自動為該鍵建立一個預設值
        # can be 'defaultdict(int)' OR 'defaultdict(list)'
        # 1. defaultdict(int): 當key不存在時，調用 int() 會返回 0
        # 2. defaultdict(list): 當key不存在時，調用 list() 會返回一個空列表 []。適合用來將資料依據某個特性進行歸類分組
        d = defaultdict(list)

        for i in strs:
            count = [0] * 26

            for j in i:
                count[ord(j) - ord('a')] += 1


            # Dictionaries (and defaultdict) require their keys to be hashable. 
            # 1. Hashable means the object’s hash value stays the same for its entire lifetime, which basically requires it to be immutable in the ways that affect equality 
            # 2. Immutable Object. 直譯「不可被改變的物件」，是什麼意思呢？ 當物件生成後，值(Value)無法被改變

            # 3. lists, dicts, sets are not hashable because they are mutable — you can change them after creation, which would break the dictionary’s internal hashing
            # 4. tuples, strings, numbers, frozensets are hashable because they are immutable
            d[tuple(count)].append(i)

            # If your default factory is a list, you can immediately call .append() or .extend() on a missing key. The defaultdict will automatically create an empty list for that key behind the scenes
            # 呢到key = count嘅list, value = str in strs

        return list(d.values())
        # .values() is a dictionary method that returns all the values stored in the dictionary (it ignores the keys)
        # use list() to include all these values returned by .values(), to fulfill the requirement of the quesition
