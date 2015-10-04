import sys
import collections


def distance(x, y):
    return (x[0] - y[0])**2 + (x[1] - y[1])**2

def brute_force(arr):
    min_distance = float('inf')
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and distance(arr[i], arr[j]) < min_distance:
                min_distance = distance(arr[i], arr[j])
                closet_pair = (arr[i], arr[j])
    return (closet_pair, min_distance)

def get_closet_pair(arr):
    if len(arr) <= 3:
        return brute_force(arr)

    mid_point = int(len(arr)/2)
    left_result = get_closet_pair(arr[:mid_point])
    right_result = get_closet_pair(arr[mid_point:])

    lr_md = float('inf')
    min_distance = min(left_result, right_result, key=lambda x: x[1])[1]
    lr_md, lr_cp = float('inf'), (0, 0)
    for p1 in arr[:mid_point]:
        if abs(p1.x - arr[mid_point].x) >= min_distance: continue
        for p2 in arr[mid_point:]:
            if abs(p2.x - arr[mid_point].x) >= min_distance: continue
            if distance(p1, p2) < lr_md:
                lr_md = distance(p1, p2)
                lr_cp = (p1, p2)
    lr_result = (lr_cp, lr_md)

    return min(left_result, right_result, lr_result, key=lambda x: x[1])




if __name__ == "__main__":
    file = open(sys.argv[1])
    line = int(file.readline().rstrip("\n"))
    arr = [() for i in range(line)]
    Point = collections.namedtuple('Point', 'x y')
    for i in range(line):
        x, y = map(float, file.readline().strip("()\n").split(", "))
        arr[i] = Point(x, y)
    p1, p2 = get_closet_pair(sorted(arr, key=lambda p: p.x))
    print(p1, p2)
