from collections import defaultdict

rules = defaultdict(set)
updates = []

with open("input.txt") as file:
    line = file.readline()

    while line.strip():
        page1, page2 = line.strip().split("|")
        rules[page1].add(page2)
        line = file.readline()

    line = file.readline()
    while line:
        updates.append(line.strip().split(","))
        line = file.readline()


def isValidPage(page1, page2):
    return page2 in rules[page1]


def isValidUpdate(update):
    visited = set()

    visited.add(update[0])

    for i in range(1, len(update)):
        newPage = update[i]
        for page in visited:
            if not isValidPage(page, newPage):
                return False
        visited.add(newPage)
    return True


def correctUpdate(update):
    correctedUpdate = update.copy()

    for i in range(1, len(update)):
        newPage = update[i]

        for j in range(i):
            page = correctedUpdate[j]
            if page == newPage:
                continue

            isValid = isValidPage(page, newPage)

            if not isValid:
                index = correctedUpdate.index(page)
                correctedUpdate[index], correctedUpdate[i] = (
                    correctedUpdate[i],
                    correctedUpdate[index],
                )
                newPage = page
    return correctedUpdate


def getValidPageCount(updates):
    count = 0
    correctedCount = 0
    for update in updates:
        if isValidUpdate(update):
            count += int(update[len(update) // 2])
            continue

        correctedUpdate = correctUpdate(update)
        correctedCount += int(correctedUpdate[len(correctedUpdate) // 2])

    return count, correctedCount


print(f"Correctly-ordered update sum: {getValidPageCount(updates)}")
