#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;


string inverseBWT(int n, string s) {

	string L = s;
	string F = s;
	sort(F.begin(), F.end());
	
	string chars = "";
	vector<int> used_idx{};
	vector<pair<char, char>> used_pairs{};

	int current = n-1;

	while (chars.length() < s.length()-1) {


		chars += F[current];
		used_idx.push_back(current);
		used_pairs.push_back(
			pair<char, char>{L[current], F[current]});
		
		int next = -1;
		int nextBeforePairCheck = 111; 
		for (int i = 0; i < s.length(); i++) {
			bool skip = false;

			if (L[i] != F[current]) continue;

			for (auto j: used_idx) {
				if (i == j) {
					skip = true;
					break;
				}
			}
			if (skip) continue;

			nextBeforePairCheck = i;

			for (auto p: used_pairs) {
				if (pair<char, char>{L[i], F[i]} == p) {
					skip = true;
					break;
				}
			}
			if (skip) continue;

			next = i;
			break;
		}

		if (next == -1) next = nextBeforePairCheck;

		current = next;
	}
	chars += F[current];
	return chars;
}

int main() {
	int n; string s;
	cin >> n >> s;
	cout << inverseBWT(n , s) << endl;
}
