inputString = ""
with open("input.txt") as file:
    inputString = file.readline().strip()

print(inputString)


def getIDRepresentation(inputList):
    outputList = []

    for index, block in enumerate(inputList):
        value = int(block)
        while value > 0:
            if index % 2 == 0:
                outputList.append(index // 2)
            else:
                outputList.append(".")
            value -= 1

    return outputList


idRepresentation = getIDRepresentation(list(inputString))
left, right = 0, len(idRepresentation) - 1

while left < right:
    while idRepresentation[left] != ".":
        left += 1
    while idRepresentation[right] == ".":
        right -= 1

    idRepresentation[left], idRepresentation[right] = (
        idRepresentation[right],
        idRepresentation[left],
    )
    left += 1
    right -= 1

while left < len(idRepresentation) and idRepresentation[left] != ".":
    left += 1

finalString = "".join([str(val) for val in idRepresentation])
checkSum = 0

for index, digit in enumerate(finalString):
    print(digit)
    if digit == ".":
        break
    checkSum += int(digit) * index
print(finalString.replace(".", ""), len(finalString), checkSum)
