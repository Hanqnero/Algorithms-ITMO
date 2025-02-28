#include <iostream>

long m = 3;
int N;
int grid[512][512] = {};
int HX, HY = 0;

inline void input(int* n, int* hx, int *hy) {
	std::cin >> *n >> *hx >> *hy;
}

inline void place(int x, int y) {
	grid[y][x] = m++/3;
}

inline void place0(int x, int y) {
	if (x == HX && y == HY)
		grid[y][x] = 0;
}


void generate(int n, int x, int y, int hx, int hy);
void generate(int n, int x, int y, int hx, int hy) {


	std::string prefix;
	for (int i = 0; i < N-n; i++) {
		prefix += "  ";
	}

	// hx and hy ALWAYS are inside current square
	// they are relative to x, y
	// (x, y) is the top-left cell of given square.
	
	// x x
	// x x
	if (n == 1) {
		// std::cout << '\n';
		if (hx == 0) {
			if (hy == 0) {
				// 0 x
				// x x
				place0(x, y);
				place(x+1, y);
				place(x, y+1);
				place(x+1, y+1);

			} else {
				// x x
				// 0 x
				place(x, y);
				place(x+1, y);
				place0(x, y+1);
				place(x+1, y+1);
			}
		} else {
			if (hy == 0) {
				// x 0
				// x x
				place(x, y);
				place0(x+1, y);
				place(x, y+1);
				place(x+1, y+1);
				
			} else {
				// x x
				// x 0
				place(x, y);
				place(x+1, y);
				place(x, y+1);
				place0(x+1, y+1);
			}
		}  
		return;
	}

	int side = (1 << n);

	if (hx < side/2) {
		if (hy < side/2) {
			// x x x x
			// x 0 # x
			// x # # x
			// x x x x

			place(x+side/2,  y+side/2);
			place(x+side/2,  y+side/2-1);
			place(x+side/2-1,y+side/2);

			generate(n-1,        x,        y,       hx,       hy);
			generate(n-1, x+side/2,        y,        0, side/2-1);
			generate(n-1,        x, y+side/2, side/2-1,        0);
			generate(n-1, x+side/2, y+side/2,        0,        0);

		} else {
			// x x x x
			// x # # x
			// x 0 # x
			// x x x x

			place(x+side/2,  y+side/2);
			place(x+side/2,  y+side/2-1);
			place(x+side/2-1,y+side/2-1);

			generate(n-1, x       , y       , side/2-1, side/2-1);
			generate(n-1, x+side/2, y       ,        0, side/2-1);
			generate(n-1, x       , y+side/2,       hx,hy-side/2);
			generate(n-1, x+side/2, y+side/2,        0,        0);

		}
	} else {
		if (hy < side/2) {
			// x x x x
			// x # 0 x
			// x # # x
			// x x x x

			place(x+side/2,  y+side/2);
			place(x+side/2-1,y+side/2);
			place(x+side/2-1,y+side/2-1);

			generate(n-1, x       , y       ,   side/2-1, side/2-1);
			generate(n-1, x+side/2, y       ,  hx-side/2,       hy);
			generate(n-1, x       , y+side/2,   side/2-1,        0);
			generate(n-1, x+side/2, y+side/2,          0,        0);

		} else {
			// x x x x
			// x # # x
			// x # 0 x
			// x x x x

			place(x+side/2-1,y+side/2-1);
			place(x+side/2-1,y+side/2);
			place(x+side/2,  y+side/2-1);

			generate(n-1, x       , y       ,   side/2-1,   side/2-1);
			generate(n-1, x+side/2, y       ,          0,   side/2-1);
			generate(n-1, x       , y+side/2,   side/2-1,          0);
			generate(n-1, x+side/2, y+side/2,  hx-side/2,  hy-side/2);
		}
	}
	return;
}

int main() {
	int n, hx, hy;
	input(&n, &hx, &hy);
	N = n;

	HX = --hx, HY = --hy;
	
	generate(n, 0, 0, hx, hy);

	for (int x = 0; x < (1 << N); x++) {
		for (int y = 0; y < (1 << N); y++) {
			std::cout << grid[y][x] << " ";
		}
		std::cout << "\n";
	}
}

