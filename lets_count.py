import geometry

figure = input("What figure will you choose? Enter S for square, R for rectangle, T for triangle, C for circle, \n RH for rhombus or TR for trapezium. ")

if figure.lower() == 's':
    dimension_x = int(input("Please enter length of the side this square: "))
    print("The field of this figure is: ", geometry.square(dimension_x))
elif figure.lower() == 'r':
    dimension_x = int(input("Please enter length of the one side this rectangle: "))
    dimension_y = int(input("And the other side has dimension: "))
    print("The field of this figure is: ", geometry.rectangle(dimension_x, dimension_y))
elif figure.lower() == 't':
    dimension_a = int(input("Please enter length of the triangle base: "))
    dimension_h = int(input("And its height: "))
    print("The field of this figure is: ", geometry.triangle(dimension_a, dimension_h))
elif figure.lower() == 'c':
    dimension_r = int(input("Please enter length of the radius: "))
    print("The field of this figure is: ", geometry.circle(dimension_r))
elif figure.lower() == 'rh':
    dimension_e = int(input("Please enter length of the one diagonal this rhombus: "))
    dimension_f = int(input("And the other diagonal has dimension: "))
    print("The field of this figure is: ", geometry.rhombus(dimension_e, dimension_f))
elif figure.lower() == 'tr':
    dimension_a = int(input("Please enter length of the trapezium base: "))
    dimension_b = int(input("And the other base has dimension: "))
    dimension_h = int(input("And its height: "))
    print("The field of this figure is: ", geometry.trapezium(dimension_a, dimension_b, dimension_h))
else:
    print("Something went wrong...")
