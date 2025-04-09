from typing import List, Tuple
import math

def distance_sq(p1: Tuple[int, int], p2: Tuple[int, int]):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def orientation(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]):
    value = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

    if value == 0:
        return 0    # collinear
    else:
        return 1 if value < 0 else 2    # clockwise or anti-clockwise

def graham_scan(points: List[Tuple[int, int]]):
    min_point = min(points, key=lambda p: (p[1], p[0]))
    points.remove(min_point)

    points.sort(key=lambda p: (math.atan2(p[1] - min_point[1], p[0] - min_point[0]), distance_sq(min_point, p)))
    sorted_points = [ min_point ] + points

    stack = []
    for point in sorted_points:
        while len(stack) >= 2 and orientation(stack[-2], stack[-1], point) != 2:
            stack.pop()
        stack.append(point)
    
    return stack

if __name__ == '__main__':

    n = int(input("Enter the number of points: "))
    print("Enter the points:-")
    points = [tuple(map(int, input().split())) for i in range(n)]

    hull_points = graham_scan(points)
    print(f"\nNumber of hull points: {len(hull_points)}")
    print(f"Points in the hull: {hull_points}")