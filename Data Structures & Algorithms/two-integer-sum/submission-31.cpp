class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {  // = call呢個method時要provide vector同int嘅parameter

        int n = nums.size();

        unordered_map<int, int> prevMap;  // 整unordered_map要入key同pair嘅types, 呢到兩個都係int

        for (int i = 0; i < n; i++) {

            int diff = target - nums[i]; // diff加埋num[i] = target的話，num[i]同diff就可以掉入

            if (prevMap.find(diff) != prevMap.end()) { 
            // If the iterator from find(diff) is not equal to end(), then the key was found
            // end() means “not found” (past-the-end position) *******************
            // Ex.:
            // for (auto it = v.begin(); it != v.end(); ++it)
            // it != v.end() means if it 唔等於v.end() 呢個past-the-end position, 個loop會繼續

            // 所以呢到 prevMap.find(diff) != prevMap.end()，就係check diff喺唔喺prevMap入面

                return {prevMap[diff], i};
                // 因為係順序loop nums, 所以如果diff喺prevMap入面，咁佢個index一定細過i，所以咁return可以確保smaller index喺前面
            }

            prevMap.insert({nums[i], i}); 
            // diff唔喺prevMap，就會將宜家loop到嘅element掉入去prevMap
        }
        return {};
        
    }
};

// unordered_map in c++:
// it equals to dictionary in Python, but it stores key-value pairs with unique keys using HASHING
// it provides average O(1) time complexity for search, insertion, and deletion



// find() in c++:
// It is used to find the FIRST occurrence of a given value in a specified range. 
// The function works with containers that provide iterators, such as arrays, vectors, lists, and deques

// find() syntax:
// std::find(first, last, value);        >>>>  first同last整左個search range, value就係要搵嘅嘢