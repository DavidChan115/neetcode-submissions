class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        vector<int> counter(26, 0);    // s and t ONLY consist of lowercase English letters.

        for (int i = 0; i < s.length(); i++) {     // c++ for loop 間開係用; 唔用,
            counter[s[i] - 'a']++;   
            counter[t[i] - 'a']--;
            // In ASCII (and in UTF-8 / Unicode for the basic Latin alphabet): 'a' = 97
            // Ex. 'a' - 'a' = 97 - 97 = 0
        }

        for (int i : counter) {
            if (i != 0) {
                return false;
            }
        }
        return true;
    }
};

// The syntax for initiating a vector in c++:
// vector<type> v = {val1, val2, val3, ...};

// We can initialize all the elements of the vector to a single value. 
// vector<type> v(n, val);
// first parameter "n": how many elements in this vector
// second parameter "val": all these n elements in the vector will ALL be this val

// Range-Based for Loop in C++:
//  vector<int> v = {1, 2, 3, 4, 5};

//  for (int i : v) {               
//      cout << i << " ";
//  }

// loop time based on the length of s and t, so time complexity = O(n + m)  (n is s length, m is t length)
// counter vector will always be 26, which is constant, so space complexity = O(1)