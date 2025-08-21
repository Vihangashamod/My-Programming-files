print("Volumes of 3D Shapes")
print("____________________________")

# Volume of a Cube
print("Volume of a Cube: ")
a = float(input("Enter the length of side (a): "))
volume = a ** 3
print(f"Volume of the cubic is: ", volume)
print("____________________________")

# Volume of a Rectangular Prism
print("Volume of a Rectangular Prism: ")
l = float(input("Enter the length (l): "))
w = float(input("Enter the width (w): "))
h = float(input("Enter the height (h): "))
volume = l * w * h
print(f"Volume of the Rectangular Prism is: {volume:.2f}")
print("____________________________")

# Volume of a Cylinder
print("Volume of a Cylinder: ")
r = float(input("Enter the radius of the base: "))
h = float(input("Enter the height of the cylinder: "))
volume = 3.14 * (r ** 2) * h
print(f"Volume of the Cylinder is: {volume:.2f}")
print("____________________________")

# Volume of a Cone
print("Volume of a Cone: ")
r = float(input("Enter the radius of the cone: "))
h = float(input("Enter the height of the cone: "))
volume = (1/3) * 3.14 * (r ** 2) * h
print(f"Volume of the Cone is: {volume:.2f}")
print("____________________________")

# Volume of a Sphere
print("Volume of a Sphere: ")
r = float(input("Enter the radius of the Sphere: "))
volume = (4/3) * 3.14 * (r ** 3)
print(f"Volume of the Sphere is: {volume:.2f}")
print("____________________________")

