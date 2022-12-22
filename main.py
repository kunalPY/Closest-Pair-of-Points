import math


def distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def closest_pair_recursive(points, left, right):
    """Recursive function for finding the closest pair of points."""
    # Base case: there are 2 or 3 points
    if right - left <= 3:
        return closest_pair_brute_force(points, left, right)

    # Divide the points into two halves
    middle = (left + right) // 2
    left_pair = closest_pair_recursive(points, left, middle)
    right_pair = closest_pair_recursive(points, middle, right)

    # Find the pair with the minimum distance
    pair = min(left_pair, right_pair, key=lambda pair: distance(pair[0], pair[1]))

    # Find the points that are within a distance of pair[1][0] - pair[0][0] of the middle line
    middle_line = (points[middle][0] + points[middle + 1][0]) / 2
    middle_points = [point for point in points[left:right] if abs(point[0] - middle_line) < distance(pair[0], pair[1])]

    # Sort the middle points by their y-coordinates
    middle_points.sort(key=lambda point: point[1])

    # Check for points within a distance of pair[1][1] - pair[0][1]
    for i in range(len(middle_points)):
        for j in range(i + 1, min(i + 8, len(middle_points))):
            candidate = (middle_points[i], middle_points[j])
            pair = min(pair, candidate, key=lambda pair: distance(pair[0], pair[1]))

    return pair


def closest_pair_brute_force(points, left, right):
    """Find the closest pair of points using a brute-force approach."""
    min_distance = float('inf')
    min_pair = None
    for i in range(left, right):
        for j in range(i + 1, right):
            pair = (points[i], points[j])
            distance = math.sqrt((pair[0][0] - pair[1][0]) ** 2 + (pair[0][1] - pair[1][1]) ** 2)
            if distance < min_distance:
                min_distance = distance
                min_pair = pair
    return min_pair


# Exemplify
points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
pair = closest_pair_recursive(points, 0, len(points))
print(pair)
