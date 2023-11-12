name = input("What is your name? ")
def solve_cubic(a,b,c,d):
    x = (((-b**3)/(27*a**3)+((b*c)/(6*a**2))-(d/(2*a)))+((((((-b**3)/(27*a**3))+((b*c)/(6*a**2))-(d/(2*a)))**2)+((c/(3*a))-(b**2)/(9*a**2))**3)**(1/2)))**(1/3)+(((-b**3)/(27*a**3)+((b*c)/(6*a**2))-(d/(2*a)))+((((((-b**3)/(27*a**3))+((b*c)/(6*a**2))-(d/(2*a)))**2)+((c/(3*a))-(b**2)/(9*a**2))**3)**(1/2)))**(1/3)-b/3*a
    return str(x.real)
print("I can solve the Cubic Eequation ax^3-bx^2+cx-d=0")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))
equation=f"Hello {name.capitalize()} i can solve {a} x^3- {b} x^2+ {c} x- {d} =0"
equation=equation.replace("1 x","x")
equation=equation.replace("- -","-")
print(equation)
result = solve_cubic(a,b,c,d)
print("the result of is",solve_cubic(a,b,c,d))










































