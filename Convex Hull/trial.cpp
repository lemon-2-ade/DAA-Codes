#include <iostream>
#include <stack>
#include <vector>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

typedef struct {
    int x, y;
} Point;

int orientation (Point p, Point q, Point r) {
    int value = (p.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x);

    if (value == 0) {
        return 0;   // collinear
    } else {
        return (value < 0)? 1 : 2;      // clockwise or anti-clockwise
    }
}

double distance (Point p, Point q) {
    double distanceSq = pow(p.x - q.x, 2) + pow(p.y - q.y, 2);
    return sqrt(distanceSq);
}

void grahamScan (vector<Point> &points) {
    int n = points.size();
    if (n < 3) {
        return;
    }

    Point minPoint = points[0];
    for (const Point& point: points) {
        if (minPoint.y > point.y) {
            minPoint = point;
        } else if (minPoint.y == minPoint.y && minPoint.x > point.x) {
            minPoint = point;
        }
    }   // finding the bottom-most point by y-axis 

    cout << minPoint.x << ", " << minPoint.y << endl;
}

int main (void) {
    vector<Point> points = {
        { 1, 4 },
        { 5, 9 },
        { -2, 1 }
    };

    grahamScan(points);
}