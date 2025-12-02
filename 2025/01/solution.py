dial_value = 10050
num_zeros = 0
last_hundredth = 100


def get_num(line: str):
    num = int(line[1:])
    if line[0] == "R":
        return num
    return -num


with open("input.txt") as file:
    line = file.readline().strip()
    while line:
        print(f"current dial value: {dial_value}, input: {line}", end="")

        new_num = dial_value + get_num(line)
        next_hundredth = abs(new_num) // 100

        num_zeros += abs(next_hundredth - last_hundredth)

        dial_value = new_num
        last_hundredth = next_hundredth

        print(f" = {dial_value} (zeros: {num_zeros})")

        line = file.readline().strip()

print(f"number of zeros: {num_zeros}")
