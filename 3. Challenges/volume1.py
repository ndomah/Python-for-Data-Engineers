class volume_1:
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height
        
    def cube(self):
        if self.length == self.breadth == self.height:
            return self.length ** 3
        else:
            raise ValueError("All sides must be equal to calculate the volume of a cube.")
        
    def cuboid(self):
        return self.length * self.breadth * self.height
    
# example usage in this module
if __name__ == '__main__':
    length, breadth, height = 3, 4, 5
    v1 = volume_1(length, breadth, height)
    print(f"Cuboid volume: {v1.cuboid()}")