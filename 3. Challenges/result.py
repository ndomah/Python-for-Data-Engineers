from volume1 import volume_1
from volume2 import volume_2

# input for volume1
length, breadth, height = 3, 4, 5
v1 = volume_1(length, breadth, height)
print(f"Cuboid Volume from volume1: {v1.cuboid()}")

# input for volume2
radius, height = 6, 7
v2 = volume_2(radius, height)
print(f"Sphere Volume from volume2: {v2.sphere()}")