class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
    // return vector that contains vectors of strings
    // Ex. Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        
        unordered_map<string, vector<string>> res;  
        // like dictionary in Python
        // key = a string
        // value = a vector with strings in it
        
        for (const auto& s : strs) {

            vector<int> count(26, 0);  
            // strs[i] is made up of lowercase English letters
            // We can initialize all the elements of the vector to a single value: 
            // Ex.      vector<type> v(n, val);

            for (char c : s) {    // traditional range-based for loop
                count[c - 'a']++;
            }

            string key = to_string(count[0]); 
            // converts the first number in the count array into a string, and stores it as the starting point of the key

            for (int i = 1; i < 26; ++i) {
                key += ',' + to_string(count[i]);
            }
            res[key].push_back(s);  
            // res[key]係用key去access value
            // 而res入面嘅value, 佢個type係"vector<string>", 所以insert element係用push_back()

            // push_back in c++:
            // 1. Inserts an element at the END of the vector
            // 2. **Automatically** reallocates memory when additional capacity is required
        }

        vector<vector<string>> result; // same type as the method "groupAnagrams"

        for (const auto& pair : res) {
            result.push_back(pair.second);
        }
        return result;
    }
};

// Range-based for loop in C++:
// 1. Most common syntax:
//    Ex.      for (int i : v) {...}
//    "int i" already declares the type of i, so you don't need const auto&
//    "int" is very cheap to copy, so using a copy (int i) instead of a reference is perfectly fine


// 2. Range-based for loop with some add-on
//    Ex.         for (const auto& s : strs) {...}

// const in C++:
// it means the element is read-only (you cannot modify it)

// auto in C++:
// it means it will automatically deduce(推斷) the type of the element

// & in C++:
// Use a reference (avoid copying the element)

// so what "for (const auto& s : strs) {...}" is it automatically deduce the type of elements in strs, and use the reference of those elements rather than directly copying them, because "&" doesn't allow us to copy the elements in strs.


// different version of range-based for loop:
// 1. Copy (slower for big objects like string)
// for (auto s : strs)

// 2. Use reference, faster, but still can modify the original element
// for (auto& s : strs)

// 3. Use reference, faster, read-only (best default to keep it safe)
// for (const auto& s : strs)


// *** No matte when, if we use range-based for loop, const auto& is the best default choice ***



