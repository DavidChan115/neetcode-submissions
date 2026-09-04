class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):   # check左length先, diff length must means they are not anagram
            return False 

        s_dict = {}  # build empty dictionary
        t_dict = {}

        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1   
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1   
            #前面已經有 =, 唔可以再寫 +=
            # = 後面 has to be an expression that produces a number, s_dict.get(s[i]) += 1 is itself an assignment statement, so Python just rejects it
            # get() syntax: dictionary.get(keyname, value), 
            # value is optional. A value to return if the specified key does not exist. Default value None, 
            # 如果一開始個key未有value, 咁就會用get()嘅value頂住先，所以一開始如果冇填get()嘅value, 然後個key又未有value住，就會出none，咁之後arithmetic就會做唔到，因為none + 1 = error
            

        if s_dict == t_dict:
            return True
        return False
        



# 1. Hash table is a data structure. You take a key, run it through a hash function, get an integer, and use that to jump straight to a slot in an array with that integer extracted by the hash function. 

# 2. Collisions of a hash table get handled with open addressing (what CPython actually uses for dict/set). 

# 3. Hash table with fast average O(1) lookup, insert, delete



# 1. hashable =  an object that has a stable __hash__ and __eq__ so it can be used as a dict/set key. That’s a property of the objects you put in.)
# 2. hash-based = the container itself(set/dict/...) uses a hash table



# In python:
# 1. hash set = set
#    hash set/set = a hash table used only to store **unique keys** (no associated values, or dummy values internally)

# 2. hash map = dict
#    A hash table used as a key → value mapping. Keys must be hashable and unique (values can be anything)



# In other languages (Java/c++/...), you can have a “set” or “dict” that never hashes anything. It just compares keys and walks a tree. 

# Python doesn’t give you that option out of the box; both set and dict are always hash tables, so the things you put in them **must be hashable**