import math

def calculate2(Pr, y, b):
    tan_y = math.tan(y)
    tan_b = math.tan(b)
    cos_b = math.cos(b)
    
    if tan_y == tan_b:
        return None
    
    return (Pr * tan_y) / (cos_b * (tan_y - tan_b))

def calculate1(Pr, Pm):
    if Pr + Pm == 0:
        return None
    return (Pr * Pm) / (Pr + Pm)


print(calculate2(5.5, y=34, b=5))

