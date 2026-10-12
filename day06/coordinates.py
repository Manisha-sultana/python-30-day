points = [(3, 4), (1, 2), (5, 1), (0, 2)]

closest = min(points, key=lambda point: point[0]**2 + point[1]**2)

print("Closest point:", closest)