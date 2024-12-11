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
checkSum = 0
left, right = 0, len(idRepresentation) - 1

while left < right:
    while idRepresentation[left] != ".":
        checkSum += left * idRepresentation[left]
        left += 1
    while idRepresentation[right] == ".":
        right -= 1

    if right < left:
        break

    idRepresentation[left], idRepresentation[right] = (
        idRepresentation[right],
        idRepresentation[left],
    )
    # finalString = "".join([str(val) for val in idRepresentation])
    # print((left, idRepresentation[left]), (right, idRepresentation[right]))
    checkSum += left * idRepresentation[left]
    left += 1
    right -= 1

print(right, idRepresentation[right])

while left < len(idRepresentation) and idRepresentation[left] != ".":
    checkSum += left * idRepresentation[left]
    left += 1

finalString = "".join([str(val) for val in idRepresentation])
print(finalString.replace(".", ""), idRepresentation, len(finalString), checkSum)
