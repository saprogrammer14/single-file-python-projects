import cmath

A = complex(input("Enter the value of A: "))
B = complex(input("Enter the value of B: "))
C = complex(input("Enter the value of C: "))

D = B**2 - 4 * A * C
root1 = (-B + cmath.sqrt(D)) / (2 * A)
root2 = (-B - cmath.sqrt(D)) / (2 * A)

print(f"roots are {root1} and {root2}")