from collections import defaultdict
import math

freq = defaultdict(int)

with open("input.txt", "r") as file:
    line = file.readline().strip()

    stones = line.split(" ")

    for stone in stones:
        freq[int(stone)] += 1


def transform(stone, frequency):
    freq[stone] -= frequency
    if stone == 0:
        freq[1] += frequency
        return

    length = math.floor(math.log10(stone) + 1)
    if length % 2 == 0:
        halfLength = length // 2
        part1 = stone // (10**halfLength)
        part2 = stone % (10**halfLength)
        freq[part1] += frequency
        freq[part2] += frequency
        return

    freq[stone * 2024] += frequency


def blink(stones):
    localizedFreq = list(stones.items())
    for stone, frequency in localizedFreq:
        transform(stone, frequency)


for i in range(75):
    blink(freq)

count = 0
for value in freq.values():
    count += value

print(count)
