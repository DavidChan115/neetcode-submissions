class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        unordered_map<int, int> count;

        vector<vector<int>> freq(nums.size() + 1);
        // the () after the name "freq", is used to call the constructor of vector.
        // It declare the vector + set the size immediately after declaring

        for (int n : nums) {  // int is cheap to copy so no need const auto&
            count[n] = count[n] + 1;
            // "count[n]" is accessing the value of "n" key
            // 
        }

        for (const auto& entry : count) {
            freq[entry.second].push_back(entry.first);
        }

        vector<int> res;

        for (int i = freq.size() - 1; i > 0; --i) {
            for (int n : freq[i]) {
                res.push_back(n);

                if (res.size() == k) {
                    return res;
                }
            }
        }
        return res;
    }
};


// bucket sort:
// 1. Create buckets: Initialize n empty lists (where n is the length of your input array).
// 2. Scatter elements: Loop through the input and place each item into its corresponding bucket.
// 3. Sort each bucket: Sort the items inside EVERY non-empty bucket using insertion sort or a built-in sort.
// 4. Gather results: Concatenate all sorted buckets in order to produce the final array.














