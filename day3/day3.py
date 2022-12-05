def prioritySum(c): #Given a rucksack, return the value of the lowercase or the upper case order value
    if c.islower():
        return ord(c) - ord("a") + 1
    else:
        return ord(c) - ord("A") + 27

with open("input.txt") as contents: #Generic split read asnd split so we can look at inputs at single lines
    lines = contents.read().split()

acc = 0
for line in lines:
    lower = set(line[:len(line)//2]) #The first half of the letters, all lowercase
    upper = set(line[len(line)//2:]) #The back half of the letters, all uper case
    c = next(iter(lower.intersection(upper)))
    acc += prioritySum(c)



print("Day 3 Part 1 = " + str(acc))

i = 0
accumulator = 0
while i < len(lines):
    group = lines[i: i + 3]
    commonItem = next(iter(set(group[0]).intersection(set(group[1])).intersection(set(group[2]))))
    accumulator += prioritySum(commonItem)
    i += 3

print("Day 3 Part 2 = ", accumulator)