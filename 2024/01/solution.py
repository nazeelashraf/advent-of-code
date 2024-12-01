import heapq
from collections import defaultdict

list1 = []
list2 = []
freq = defaultdict(int)

totalDistance = 0
similarityScore = 0

with open("input.txt", "r") as file:
    content = file.read()
    lines = content.strip().split("\n")

for line in lines:
    num1, num2 = line.split()
    num1, num2 = int(num1), int(num2)

    freq[num2] += 1

    heapq.heappush(list1, num1)
    heapq.heappush(list2, num2)

while list1 and list2:
    num1, num2 = heapq.heappop(list1), heapq.heappop(list2)
    totalDistance += abs(num1 - num2)
    similarityScore += num1 * freq[num1]

print(f"Total Distance: {totalDistance}")
print(f"Similarity Score: {similarityScore}")
