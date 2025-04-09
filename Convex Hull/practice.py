from typing import List, Tuple
import math

def orientation(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]):
    value = (q[0])

if __name__ == '__main__':
    n = int(input("Enter the number of vertices: "))
    points = [tuple(map(int, input().split())) for i in range(n)]

    hull_points = graham_scan(points)
    print(f"Points covering the convex hull: {hull_points}")