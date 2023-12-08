class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance_between_points(a, b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5


