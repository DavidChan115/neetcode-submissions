from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list)

        for i in strs:
            count = [0] * 26

            for j in i:
                count[ord(j) - ord('a')] += 1

            # If your default factory is a list, you can immediately call .append() or .extend() on a missing key. The defaultdict will automatically create an empty list for that key behind the scenes
            d[tuple(count)].append(i)
            # Dictionaries (and defaultdict) require their keys to be hashable. Lists are not hashable because they are mutable — you can change them after creation, which would break the dictionary’s internal hashing
        return list(d.values())