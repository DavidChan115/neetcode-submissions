from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 


        count = defaultdict(int) 
        # default type of this dict is int not list
        for num in nums:
            count[num] += 1
        

        freq = []
        for i in range(len(nums) + 1): # index 0: 0,1,2,3...
            freq.append([])


        for key, value in count.items():
        # dict.items() is a built-in method used to retrieve both the keys and values from a dictionary at the same time
            freq[value].append(key)
            # freq[value]係搵freq入面嘅第幾個list, value當係index
            # 只要個num喺dict入面有相同value, 咁呢啲num就會map落同一個list
            # 而因為呢個append係用index, freq點都係sort咗做freq[0], freq[1]...之後就可以loop backward starts from highest frequency

        res = []

        for i in range(len(freq) - 1, 0, -1):
        # range(start, stop, step)
        # We walk from the back of the freq list (highest frequency) toward the front. 
            for num in freq[i]: #可以有多個num有相同frequency
                res.append(num)

                # As soon as we have collected k numbers, we return.
                if len(res) == k:
                    return res

# time complexiy = build defaultdict and count list based on nums with n length = O(n)

# space complexity = build defaultdict and count list based on nums with n entries = O(n)
