#Volumes of the shapes
print("Volumes of 3D Shapes")

#volume of a Cube
print("Volume of a cube: ")
input_a = float(input("Enter the length of side(a): "))
volume = input_a*3
print(f"Volume of the cube is: {volume:.2f}")
print("____________________________")

#volume of a Rectangular Prism
print("Volume of a Rectangular Prism: ")
input_l = float(input("Enter the length of l: "))
input_w = float(input("Enter the width of w: "))
input_h = float(input("Enter the height of h: "))
volume = input_l*input_w*input_h
print(f"Volume of the Rectangular Prism is: {volume:.2f}")
print("____________________________")

#volume of a Cylinder
print("Volume of a Cylinder: ")
input_r = float(input("Enter the radius of the base: "))
input_h = float(input("Enter the height of the cylinder: "))
volume = 3.14*input_r*2*input_h
print(f"Volume of the Cylinder is: {volume:.2f}")
print("____________________________")

#volume of a Cone
print("Volume of a Cone: ")
input_r = float(input("Enter the radius of the cone: "))
input_h = float(input("Enter the height of the cone: "))
volume = (3.14*input_r*2*input_h)/3
print(f"Volume of the Cone is: {volume:.2f}")
print("____________________________")

#volume of a Sphere
print("Volume of a Sphere: ")
input_r = float(input("Enter the radius of the Sphere: "))
volume = (4/3)*3.14*input_r*3
print(f"Volume of the Sphere is: {volume:.2f}")
print("____________________________")
