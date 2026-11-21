class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        return unordered_set<int>(nums.begin(), nums.end()).size() < nums.size();
    }
};

// unordered_set in c++:
// 1. Internally uses a hashing to store elements which provides average constant time O(1) for insert, search and delete

//Initialize an unordered_set from a vector 
//  vector<int> v = {1, 2, 3, 4, 5}; 
//  unordered_set<int> us3(v.begin(), v.end()); 

// array::size() Syntax
// a.size();