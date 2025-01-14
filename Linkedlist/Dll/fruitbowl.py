import math

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def construct_lower_hull(points):
    points.sort()
    hull = []
    for pt in points:
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], pt) <= 0:
            hull.pop()
        hull.append(pt)
    return hull

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def calculate_perimeter(hull):
    perimeter = 0
    for i in range(1, len(hull)):
        perimeter += calculate_distance(hull[i - 1], hull[i])
    return perimeter

def solve_optimized(points):
    lower_hull = construct_lower_hull(points)
    return round(calculate_perimeter(lower_hull))




N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

result = solve_optimized(points)
print(result)