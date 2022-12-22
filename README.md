# Closest Pair of Points
This is a Python implementation of a divide-and-conquer algorithm for finding the closest pair of points in a set of points. The algorithm has a time complexity of O(n log n), which makes it efficient for large sets of points. The problem of finding the closest pair of points is to find the two points in a set of points that have the minimum distance between them. This problem has numerous applications, such as in geographical information systems, computer graphics, and pattern recognition.

## Usage
To use the algorithm, you can call the closest_pair_recursive function with the entire set of points as the argument:

```python
points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
pair = closest_pair_recursive(points, 0, len(points))
print(pair)```

## Dependencies
This code requires the math module, which is a built-in Python module.
