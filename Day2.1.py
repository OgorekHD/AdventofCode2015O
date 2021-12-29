file = open("(FILE LOCATION)", "r")
TotalCount = 0
print(file)
for line in file:
    B = list(map(int, line.split("x")))
    B.sort()
    X = int(B[0])
    Y = int(B[1])
    Z = int(B[2])
    TotalCount += 2*(X*Z) + 2*(X*Y) + 2*(Y*Z) + X*Y
print(TotalCount)
