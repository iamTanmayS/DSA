from math import sqrt

def calc_span(pt_a, pt_b):
    return sqrt(sum((b - a)**2 for a, b in zip(pt_a, pt_b)))

def get_boundary_chain(coords):
    coords = sorted(coords)
    chain = []
    
    for coord in coords:
        while len(chain) > 1 and vector_check(chain[-2], chain[-1], coord) <= 0:
            chain.pop()
        chain.append(coord)
    return chain

def vector_check(origin, p1, p2):
    dx1, dy1 = p1[0] - origin[0], p1[1] - origin[1]
    dx2, dy2 = p2[0] - origin[0], p2[1] - origin[1]
    return dx1 * dy2 - dy1 * dx2

def measure_outline(boundary):
    return sum(calc_span(boundary[i-1], boundary[i]) 
              for i in range(1, len(boundary)))

def process_coordinates(coord_list):
    boundary = get_boundary_chain(coord_list)
    return round(measure_outline(boundary))

if __name__ == "__main__":
    count = int(input())
    coord_list = []
    for _ in range(count):
        x, y = map(int, input().split())
        coord_list.append((x, y))
    
    answer = process_coordinates(coord_list)
    print(answer)