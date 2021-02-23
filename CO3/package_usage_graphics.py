from CO3.graphics.graphics3D import cuboid
from CO3.graphics.circle import *
import CO3.graphics.rectangle

l =20
b =30
h =35

# regular import
print("Area of Rectangle : "+str(CO3.graphics.rectangle.getPerimeter(l,b)))

# shortened import
print("Area of Cuboid : "+str(cuboid.getArea(l,b,h)))

# using *
print("Area of Circle : "+str(getArea(70)))

