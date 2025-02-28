#include <iostream>
#include <ostream>
#include <string>

const int pairs[12][2] = {{0, 1}, {1, 2}, {2, 3}, {0, 3}, {4, 5}, {5, 6},
                        {6, 7}, {4, 7}, {0, 4}, {1, 5}, {2, 6}, {3, 7}};
const std::string letters("ABCDEFGH");

int main() {
  int xs[8] = {0};
  for (int i = 0; i < 8; i++)
    std::cin >> xs[i];

  int red_sum = xs[0] + xs[2] + xs[5] + xs[7];
  int black_sum = xs[1] + xs[3] + xs[4] + xs[6];

  if (red_sum != black_sum) {
    std::cout << "IMPOSSIBLE" << std::endl;
    return 0;
  }

  for (int i = 0; i < 12; i++) {
    
    int a = pairs[i][0];
    int b = pairs[i][1];

//    std::cout << "looking at pair " << letters[a] << letters[b] << std::endl;

    int n = std::min(xs[a], xs[b]);
    if (n == 0)
      continue;
 //   std::cout << "Found adjacent at " << letters[a] << letters[b] << "of mag " << n << std::endl;
    xs[a] -= n;
    xs[b] -= n;
    red_sum -= n;
    black_sum -= n;
    while (n--)
      std::cout << letters[a] << letters[b] << "-\n";
  }

  // Blacks
  for (int i = 0; i < xs[6]; i++) {
    std::cout << "BC+\nCG-\n";
  }
  for (int i = 0; i < xs[4]; i++) {
    std::cout << "AB+\nAE-\n";
  }
  for (int i = 0; i < xs[3]; i++) {
    std::cout << "AB+\nAD-\n";
  }

  // Reds
  for (int i = 0; i < xs[7]; i++) {
    std::cout << "AE+\nEH-\n";
  }
  for (int i = 0; i < xs[5]; i++) {
    std::cout << "AE+\nEF-\n";
  }
  for (int i = 0; i < xs[2]; i++) {
    std::cout << "AB+\nBC-\n";
  }


  for (int i = 0; i < red_sum; i++) {
    std::cout << "AB-\n";
  }

  std::cout << std::flush;
  return 0;
}
