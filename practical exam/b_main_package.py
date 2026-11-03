# Method 1: Import package
import shapekit

print(shapekit.VERSION)


# Method 2: Import specific function from package
from shapekit import circle_area

print(circle_area(5))


# Method 3: Full path import
import shapekit.perimeter

print(shapekit.perimeter.rect_perimeter(4, 6))


# Method 4: Import module using alias
import shapekit.perimeter as p

print(p.circle_perimeter(2))


# Method 5: Import functions from sub-package
from shapekit.solids.volume import cube_volume, cylinder_volume

print(cube_volume(3), cylinder_volume(2, 5))