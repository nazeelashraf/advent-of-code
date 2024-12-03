safe = 0
enableProblemDampener = True


def isValidLevels(levels):
    diffList = []
    positive, zero, negative = 0, 0, 0
    for i in range(1, len(levels)):
        difference = levels[i] - levels[i - 1]
        if not (1 <= abs(difference) <= 3):
            return False
        if difference > 0:
            positive += 1
        elif difference < 0:
            negative += 1
        else:
            zero += 1
        diffList.append(difference)

    if zero >= 1:
        return False

    if positive and negative == 0:
        return True

    if negative and positive == 0:
        return True

    return False


with open("input.txt", "r") as file:
    line = file.readline()

    while line:
        levels = line.strip().split()
        values = [int(level) for level in levels]

        isAnyTrue = isValidLevels(values)

        if enableProblemDampener:
            for i in range(len(values) - 1):
                isAnyTrue = isAnyTrue or isValidLevels(values[:i] + values[i + 1 :])

            isAnyTrue = isAnyTrue or isValidLevels(values[:-1])

        if isAnyTrue:
            safe += 1
        line = file.readline()

print(f"Safe levels: {safe}")
