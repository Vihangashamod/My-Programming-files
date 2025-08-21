#area of 2D shapes
print("Areas of 2D Shapes")
print("____________________________")

#area of a square
print("Area of a Square: ")
input_base = float(input("Enter the length of a side(base): "))
area = input_base ** 2
print(f"The area of the square is: {area:.2f}")
print("____________________________")

#area of a rectangle
print("Area of a Rectangle: ")
input_base = float(input("Enter the length of the base: "))
input_height = float(input("Enter the height: "))
area = input_base*input_height
print(f"The area of the rectangle is: {area:.2f}")
print("____________________________")

#area of a Triangle
print("Area of a Triangle: ")
input_base = float(input("Enter the length of the base: "))
input_height = float(input("Enter the height: "))
area = (input_base*input_height)/2
print(f"The area of the rectanle is: {area:.2f}")
print("____________________________")

#area of a Trapezium
print("area of a Trapezium: ")
input_b = float(input("Enter the length of the base(b): "))
input_height = float(input("Enter the height: "))
input_a = float(input("Enter the length of the top(a): "))
area = ((input_a+input_b)*input_height)/2
print(f"The area of the trapezium is: {area:.2f}")
print("____________________________")

#area of a Parallelogram
print("Area of a Parallelogram: ")
input_base = float(input("Enter the length of the base: "))
input_height = float(input("Enter the perpendicular Height: "))
area = input_base*input_height
print(f"The area of the parallelogram is: {area:.2f}")
print("____________________________")

#area of a Rhombus
print("Area of a Rhombus: ")
input_length = float(input("Enter the lenght: "))
input_height = float(input("Enter the height: "))
area = (input_length*input_height)/2
print(f"The area of the rhombus is: {area:.2f}")
print("____________________________")

#area of a Kite
print("Area of a kite: ")
input_length = float(input("Enter the length of the kite: "))
input_height = float(input("Enter the height of the Kite: "))
area = (input_length*input_height)/2
print(f"The area of the kite is: {area:.2f}")
print("____________________________")
