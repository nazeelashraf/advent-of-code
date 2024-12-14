import re
import math

equations = []
buttonPattern = r"Button [AB]: X\+(\d+), Y\+(\d+)"
prizePattern = r"X=(\d+), Y=(\d+)"
unitCorrection = True
with open("input.txt", "r") as file:
    line = file.readline()

    while line:
        matches = re.findall(buttonPattern, line)
        x1, y1 = matches[0]
        line = file.readline()
        matches = re.findall(buttonPattern, line)
        x2, y2 = matches[0]
        line = file.readline()
        matches = re.findall(prizePattern, line)
        xt, yt = matches[0]
        line = file.readline()
        if line:
            line = file.readline()
        rhs1 = int(xt) if not unitCorrection else 10000000000000 + int(xt)
        rhs2 = int(yt) if not unitCorrection else 10000000000000 + int(yt)
        equations.append([(int(x1), int(x2), rhs1), (int(y1), int(y2), rhs2)])

totalTokens = 0
for equation in equations:
    x1, x2, xt = equation[0]
    y1, y2, yt = equation[1]

    lcm = math.lcm(x1, y1)

    xz, yz = lcm // x1, lcm // y1

    bCoeff = x2 * xz - y2 * yz
    rhs = xt * xz - yt * yz

    a = (xt - x2 * rhs // bCoeff) // x1
    b = rhs // bCoeff

    if x1 * a + x2 * b == xt and y1 * a + y2 * b == yt:
        totalTokens += 3 * a + b
    print(f"{x1}a + {x2}b = {xt}")
    print(f"{y1}a + {y2}b = {yt}")
    print(f"LCM: {lcm}")

    print(f"1. {x1 * xz}a + {x2 * xz}b = {xt * xz}")
    print(f"2. {y1 * yz}a + {y2 * yz}b = {yt * yz}")

    print("(1) - (2)")
    print(f"{x2 * xz - y2 * yz}b = {xt * xz - yt * yz}")
    print(f"b = {rhs / bCoeff}")
    print(f"a = {(xt - x2 * rhs / bCoeff) / x1}")
    print("-----------")

print(f"Total tokens: {totalTokens}")
