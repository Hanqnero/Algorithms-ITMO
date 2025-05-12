#include <iostream>
#include <vector>
#include <string>
#include <cassert>

using namespace std;

// Fixed implementation of inverseBWT
string inverseBWT(int n, string s) {
    int len = s.size();
    vector<int> count(256, 0);
    
    // Count character frequencies
    for (char c : s) count[c]++;
    
    // Compute starting positions of each character in sorted order
    int sum = 0;
    for (int i = 0; i < 256; i++) {
        int temp = count[i];
        count[i] = sum;
        sum += temp;
    }
    
    // Create the sorted first column and T array (which maps positions)
    vector<int> T(len);
    vector<int> count_copy = count;
    
    for (int i = 0; i < len; i++) {
        T[count_copy[s[i]]] = i;
        count_copy[s[i]]++;
    }
    
    // Reconstruct the original string
    string result(len, ' ');
    int pos = n;
    
    for (int i = 0; i < len; i++) {
        pos = T[pos];
        result[i] = s[pos];
    }
    
    return result;
}

void debugTest(int idx, string bwt, string expected) {
    string result = inverseBWT(idx, bwt);
    cout << "BWT: " << bwt << endl;
    cout << "Expected: " << expected << endl;
    cout << "Actual: " << result << endl;
    cout << "Match: " << (result == expected ? "YES" : "NO") << endl;
    cout << "--------------------" << endl;
}

void runTests() {
    // Debug test case with the correct BWT string for "abracadabra"
    cout << "Debug Test Case 2:" << endl;
    debugTest(2, "rdarcaaaabb", "abracadabra");
    
    // Try other variations for completeness
    cout << "Test with alternative BWT strings:" << endl;
    debugTest(2, "rdaracaaabb", "abracadabra");
    debugTest(2, "rdacraaaabb", "abracadabra");
    
    // Add more tests if needed
}

int main() {
    runTests();
    return 0;
}