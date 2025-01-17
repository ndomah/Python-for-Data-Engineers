import math

class volume_2:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        
    def sphere(self):
        return (4 / 3) * math.pi * self.radius ** 3
    
    def cone(self):
        return (1 / 3) * math.pi * self.radius ** 2 * self.height
    
    def cylinder(self):
        return math.pi * self.radius ** 2 * self.height
    
# example usage in this module
if __name__ == '__main__':
    radius, height = 6, 7
    v2 = volume_2(radius, height)
    print(f"Sphere Volume: {v2.sphere()}")