wire1_dir = open('input.txt').readlines()[0].split(',')
wire2_dir = open('input.txt').readlines()[1].split(',')

wire1 = []
wire2 = []


current = [0, 0]
for direction in wire1_dir:
    if direction[0] == "R":
        for x in range(int(direction[1:])):
            current[0] += 1
            wire1.append((current[0], current[1]))
    elif direction[0] == "L":
        for x in range(int(direction[1:])):
            current[0] -= 1
            wire1.append((current[0], current[1]))
    elif direction[0] == "D":
        for x in range(int(direction[1:])):
            current[1] -= 1
            wire1.append((current[0], current[1]))
    elif direction[0] == "U":
        for x in range(int(direction[1:])):
            current[1] += 1
            wire1.append((current[0], current[1]))

wire1x = set()
wire1y = set()

for coord in wire1:
    wire1x.add(coord[0])
    wire1y.add(coord[1])

print(wire1x)
print(wire1y)

crosses = []
current = [0, 0]
counter = 0
for direction in wire2_dir:
    print(counter)
    counter += 1
    if direction[0] == "R":
        for x in range(int(direction[1:])):
            current[0] += 1
            if current[0] in wire1x and (current[0], current[1]) in wire1:
                crosses.append((current[0], current[1]))
    elif direction[0] == "L":
        for x in range(int(direction[1:])):
            current[0] -= 1
            if current[0] in wire1x and (current[0], current[1]) in wire1:
                crosses.append((current[0], current[1]))
    elif direction[0] == "D":
        for x in range(int(direction[1:])):
            current[1] -= 1
            if current[1] in wire1y and (current[0], current[1]) in wire1:
                crosses.append((current[0], current[1]))
    elif direction[0] == "U":
        for x in range(int(direction[1:])):
            current[1] += 1
            if current[1] in wire1y and (current[0], current[1]) in wire1:
                crosses.append((current[0], current[1]))

print(crosses)
print(min([abs(cross[0]) + abs(cross[1]) for cross in crosses]))