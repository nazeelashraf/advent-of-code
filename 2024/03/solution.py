import re

total = 0
withDo = True
pattern = r"mul\((\d{1,3},\d{1,3})\)"
doPattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"


def findMulSum(line):
    matches = re.findall(pattern, line)
    mulSum = 0
    for match in matches:
        numbers = match.split(",")
        mulSum += int(numbers[0]) * int(numbers[1])

    return mulSum


with open("input.txt", "r") as file:
    line = file.readline()

    if not withDo:
        while line:
            total += findMulSum(line)
            line = file.readline()
    else:
        i = 1
        isEnabled = True
        while line:
            matches = re.findall(doPattern, line)
            for match in matches:
                if isEnabled and match[0] == "m":
                    total += findMulSum(match)
                if match == "don't()":
                    isEnabled = False
                if match == "do()":
                    isEnabled = True
            line = file.readline()
            i += 1


print(f"Result: {total}")
