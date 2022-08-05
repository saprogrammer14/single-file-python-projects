n = int(input("Enter the number: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if (i**2 + j**2) == k**2:
                print(f"{i}, {j}, {k}")
