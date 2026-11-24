class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        unordered_map<int, int> count;

        vector<vector<int>> freq(nums.size() + 1); 
        // the () after the name "freq", is used to call the "constructor of vector". It declare the vector + set the size immediately after declaring
        // num.size() + 1 because for frequency count freq[0] is useless here, we don't need to record the number that didn't appear
        // Ex. nums = [1, 1], nums.size() = 2, = freq[0], freq[1]
        // freq[0]用唔到, and there is no freq[2]
        // so we need "nums.size() + 1" to add freq[2]
        

        for (int n : nums) {  // int is cheap to copy so no need const auto&
            count[n] = count[n] + 1;
            // "count[n]" is accessing the value of "n" key, but also saying that n is a new key if it doesn't exist yet
            // If a key does not exist yet, count[n] will automatically return 0.
            // so we initialize this new key value pair but adding 1 to it when we see the first n (0 + 1 = 1)
            // 之後如果個n有更多entry, 都可以繼續+1
        }

        for (const auto& entry : count) {
            freq[entry.second].push_back(entry.first);
            // entry = key value pair from count
            // entry.second = value = the count of n
            // "freq" is a vector with a lot of count vectors in it
            // freq[entry.second] = initializing vectors based on the count, Ex. count "1" vector, count "2" vector ...
            // then we push_back the key, which is n, into those count vectors
            // 呢到將唔同n，按照count分類落唔同的count bucket
        }

        vector<int> res;

        for (int i = freq.size() - 1; i > 0; i--) {
            // loop的次數要減走特登加的一個slot (-1)
            // 
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














