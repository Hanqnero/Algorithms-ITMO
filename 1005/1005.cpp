#include <iostream>
int main() {
	int n, xs[20] = {0};
	std::cin >> n;
	for (int i = 0; i < n; i++) {
		std::cin >> xs[i];
	}

	int min = 100'000*20 + 1;
	
	for (int bitmask = 0; bitmask < (1 << n); bitmask++) {
		int sum = 0;
		for (int i = 0; i < n; i++) {
			sum += bitmask & (1 << i) ? xs[i] : -xs[i];
		}
		sum = std::abs(sum);
		min = std::min(min, sum);
	}
	std::cout << min << '\n';

}
