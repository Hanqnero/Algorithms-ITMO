#include <iostream>
#include <vector>
#include <string>

using namespace std;

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


int main() {
    string bwt;
    int n;
    cin >> n >> bwt;
    cout << inverseBWT(--n, bwt) << endl;
    return 0;
}
