import math

def Rectangle(width, length):
    print("Would you like to calculate the area or the perimeter? (Type area or perimeter)")
    user_input_rectangle = input().lower()
    if user_input_rectangle == "area":
        rectangle_area = width * length
        return rectangle_area
    elif user_input_rectangle == "perimeter":
        rectangleperimeter = 2 * (length + width)  # Fixed the formula forperimeter
        return rectangleperimeter
    else:
        return "Invalid input. Please type 'area' or perimeter'."

def Square(side):
    print("Would you like to calculate the area or theperimeter? (Type areaperimeter)")
    user_input_square = input().lower()
    if user_input_square == "area":
        square_area = side ** 2
        return square_area
    elif user_input_square == "perimeter":
        squareperimeter = side * 4
        return squareperimeter
    else:
        return "Invalid input. Please type 'area' or perimeter'."

def Circle(radius):
    print("Are you entering the diameter or the radius? (Type radius/diameter)")
    radius_or_diameter = input().lower()
    if radius_or_diameter == "radius":
        print("calculating using radius")
    elif radius_or_diameter == "diameter":
        print("Calculating using diameter")
        radius = radius / 2
    else:
        return "Invalid input. Please type 'radius' or 'diameter'."
    
    print("Would you like to calculate the area or theperimeter? (Type areaperimeter)")
    user_input_circle = input().lower()
    if user_input_circle == "area":
        circle_area = math.pi * radius ** 2
        return circle_area
    elif user_input_circle == "perimeter":
        circleperimeter = 2 * math.pi * radius
        return circleperimeter
    else:
        return "Invalid input. Please type 'area' or perimeter'."
def Rhombus(D1,D2):
    print("Wo")

def user_input():
    print("Which shape would you like to calculate (Square, Rectangle, Circle)?")
    select_shape = input().lower()
    
    if select_shape == "rectangle":
        rectangle_width = float(input("Enter the width of the rectangle: "))
        rectangle_length = float(input("Enter the length of the rectangle: "))
        rectangle_result = Rectangle(rectangle_width, rectangle_length)
        print(f"Result: {rectangle_result}")
    
    elif select_shape == "square":
        square_side = float(input("Enter the length of the sides of the square: "))
        square_result = Square(square_side)
        print(f"Result: {square_result}")
    
    elif select_shape == "circle":
        circle_radius_or_diameter = float(input("Enter the radius or diameter of the circle: "))
        circle_result = Circle(circle_radius_or_diameter)
        print(f"Result: {circle_result}")
    
    else:
        print("Invalid shape selected. Please type 'Square', 'Rectangle', or 'Circle'.")
    
    continue_calculating = input("Do you want to continue calculating? (Type 'yes'). Else press 'Enter' to exit the program: ").lower()
    if continue_calculating != "yes":
        return False
    return True

while True:
    if not user_input():
        break
