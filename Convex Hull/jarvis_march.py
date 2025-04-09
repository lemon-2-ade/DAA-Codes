from typing import List, Tuple

def orientation(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]):
    value = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

    if value == 0:
        return 0    # collinear
    else:
        return 1 if value < 0 else 2    # clockwise or anti-clockwise
    
def gift_wrapping(points: List[Tuple[int, int]], n: int):

    if n < 3:
        return []
    
    hull_points = []
    min_point = min(points, key=lambda p: (p[1], p[0]))
    p = points.index(min_point)

    while True:
        hull_points.append(points[p])
        q = (p + 1) % n

        for i in range(n):
            if i == p:
                continue
            
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q
        if p == points.index(min_point):
            break
    
    return hull_points

if __name__ == '__main__':

    n = int(input("Enter the number of vertices: "))
    points = [tuple(map(int, input().split())) for i in range(n)]

    hull_points = gift_wrapping(points, n)
    print(f"Number of hull points: {len(hull_points)}")
    print(f"Points in the hull: {hull_points}")
