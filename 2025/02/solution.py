sum = 0


# part 2
def is_at_least_twice(num: str):
    substr = num[0]

    for i in range(1, len(num) // 2 + 1):
        count = num.count(substr)
        # print(f"{num} has {count} occurences of {substr}")
        if count * len(substr) == len(num):
            # print(f"count * len = {count * len(substr)}")
            return False
        substr += num[i]

    return True


def is_valid(num: str):
    # Part 1
    #   length = len(num)
    #   return num[: length // 2] != num[length // 2 :]
    return is_at_least_twice(num)


with open("input.txt") as file:
    array = file.readline().strip().split(",")

    for val in array:
        start, end = val.split("-")
        start, end = int(start), int(end)

        for i in range(start, end + 1):
            if not is_valid(str(i)):
                sum += i

print(sum)
