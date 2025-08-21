# Areas of 2D Shapes
print("Areas of 2D Shapes")
print("____________________________")
print("Available shapes:")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Trapezium")
print("5. Parallelogram")
print("6. Rhombus")
print("7. Kite")
print("____________________________")

choice = input("Enter the number of the shape you want to calculate the area for: ")

if choice == "1":
    print("Area of a Square: ")
    input_base = float(input("Enter the length of a side(base): "))
    area = input_base ** 2
    print(f"The area of the square is: {area:.2f}")

elif choice == "2":
    print("Area of a Rectangle: ")
    input_base = float(input("Enter the length of the base: "))
    input_height = float(input("Enter the height: "))
    area = input_base * input_height
    print(f"The area of the rectangle is: {area:.2f}")

elif choice == "3":
    print("Area of a Triangle: ")
    input_base = float(input("Enter the length of the base: "))
    input_height = float(input("Enter the height: "))
    area = (input_base * input_height) / 2
    print(f"The area of the triangle is: {area:.2f}")

elif choice == "4":
    print("Area of a Trapezium: ")
    input_b = float(input("Enter the length of the base(b): "))
    input_height = float(input("Enter the height: "))
    input_a = float(input("Enter the length of the top(a): "))
    area = ((input_a + input_b) * input_height) / 2
    print(f"The area of the trapezium is: {area:.2f}")

elif choice == "5":
    print("Area of a Parallelogram: ")
    input_base = float(input("Enter the length of the base: "))
    input_height = float(input("Enter the perpendicular Height: "))
    area = input_base * input_height
    print(f"The area of the parallelogram is: {area:.2f}")

elif choice == "6":
    print("Area of a Rhombus: ")
    input_length = float(input("Enter the length: "))
    input_height = float(input("Enter the height: "))
    area = (input_length * input_height) / 2
    print(f"The area of the rhombus is: {area:.2f}")

elif choice == "7":
    print("Area of a Kite: ")
    input_length = float(input("Enter the length of the kite: "))
    input_height = float(input("Enter the height of the Kite: "))
    area = (input_length * input_height) / 2
    print(f"The area of the kite is: {area:.2f}")

else:
    print("Invalid choice. Please select a valid shape")