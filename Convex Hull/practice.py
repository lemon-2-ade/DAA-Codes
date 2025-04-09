from typing import List, Tuple
import math

def orientation(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]):
    value = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

    if value == 0:
        return 0    # collinear
    else:
        return 1 if value < 0 else 2    #clockwise or anticlockwise

def distance(p: Tuple[int, int], q: Tuple[int, int]):
    distance_sq = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
    return math.sqrt(distance_sq)

def graham_scan(points: List[Tuple[int, int]]):
    min_point = min(points, key=lambda pt: (pt[1], pt[0]))
    points.remove(min_point)

    points.sort(key=lambda pt: (math.atan2(pt[1] - min_point[1], pt[0] - min_point[0]), distance(pt, min_point)))
    sorted_points = [ min_point ] + points

    stack = []
    for pt in sorted_points:
        while len(stack) >= 2 and orientation(stack[-2], stack[-1], pt) != 2:
            stack.pop()
        stack.append(pt)
    
    return sorted(stack, key=lambda pt: (pt[0], pt[1]))

def gift_wrapping(points: List[Tuple[int, int]], n: int):
    hull_points = []
    leftmost_pt = min(points, key=lambda pt: (pt[0], pt[1]))
    p = points.index(leftmost_pt)

    while True:
        hull_points.append(points[p])
        q = (p + 1) % n

        for i in range(n):
            if i == p:
                continue

            if orientation(points[p], points[i], points[q]) == 2:
                q = i
            
        p = q
        if points[p] == leftmost_pt:
            break
    
    return hull_points

if __name__ == '__main__':
    n = int(input("Enter the number of vertices: "))
    points = [tuple(map(int, input().split())) for i in range(n)]

    hull_points = graham_scan(points)
    print(f"Points covering the convex hull: {hull_points}")