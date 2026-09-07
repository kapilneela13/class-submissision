def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilateral Triangle"
        elif a == b or b == c or a == c:
            return "Isosceles Triangle"
        else:
            return "Scalene Triangle"
    else:
        return "Not a Triangle"

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

print(check_triangle(a, b, c))
