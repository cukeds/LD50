import math

def distance(p1x, p1y, p2x, p2y):
    return math.hypot(p1x - p2x, p1y - p2y)

def dotProduct(vec1, vec2):
    return vec1.x * vec2.x + vec1.y * vec2.y