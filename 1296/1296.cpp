#include <algorithm>
#include <iostream>
#include <vector>

int kadane(std::vector<int> arr) {
	int current_sum = 0; int best_sum = 0;
	for (int x : arr) {
		current_sum = std::max(x, current_sum + x);
		best_sum = std::max(current_sum, best_sum);
	}
	return best_sum;
}

int main() {
	int x, n; std::cin >> n;
	std::vector<int> arr;
	while (n--) {
		std::cin >> x;
		arr.push_back(x);
	}

	std::cout << kadane(arr) << "\n";
}
