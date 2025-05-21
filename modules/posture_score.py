import math

def calculate_angle(a, b, c):
    """คำนวณมุม b ระหว่างจุด a-b-c (in degrees)"""
    ba = (a[0]-b[0], a[1]-b[1])
    bc = (c[0]-b[0], c[1]-b[1])
    cos_angle = (ba[0]*bc[0] + ba[1]*bc[1]) / (
        math.hypot(*ba) * math.hypot(*bc))
    angle = math.degrees(math.acos(max(min(cos_angle, 1), -1)))
    return angle
