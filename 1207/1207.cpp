#include <iostream>

struct point
{
    long long x, y, id;
} points[10'001];

int main()
{
    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        std::cin >> points[i].x >> points[i].y;
        points[i].id = i + 1;
        if (points[0].y > points[i].y) {
            std::swap(points[0], points[i]);
        }
    }

    for (int i = 1; i < n; i++) {
        points[i].x -= points[0].x, points[i].y -= points[0].y;
    }

    qsort(points+1, n-1, sizeof(struct point), [](const void* a, const void* b){
        auto x = *(const point*) a, y = *(const point*) b;
        if (y.y == 0 && x.y == 0) return (int) (x.x - y.x > 0);
        if (x.x*y.y > x.y*y.x) return -1;
        return 1;
    });

    std::cout << points[0].id << " " << points[n/2].id << "\n";
    std::cout << std::flush;
    return 0;
}