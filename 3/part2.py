from collections import defaultdict

wire1_dir = open('input.txt').readlines()[0].split(',')
wire2_dir = open('input.txt').readlines()[1].split(',')

grid = defaultdict(lambda: [0, 0])


current = [0, 0]
counter = 0
for direction in wire1_dir:
    if direction[0] == "R":
        for x in range(int(direction[1:])):
            current[0] += 1
            counter += 1
            grid[(current[0], current[1])][0] = 1
            grid[(current[0], current[1])][1] = counter
    elif direction[0] == "L":
        for x in range(int(direction[1:])):
            current[0] -= 1
            counter += 1
            grid[(current[0], current[1])][0] = 1
            grid[(current[0], current[1])][1] = counter
    elif direction[0] == "D":
        for x in range(int(direction[1:])):
            current[1] -= 1
            counter += 1
            grid[(current[0], current[1])][0] = 1
            grid[(current[0], current[1])][1] = counter
    elif direction[0] == "U":
        for x in range(int(direction[1:])):
            current[1] += 1
            counter += 1
            grid[(current[0], current[1])][0] = 1
            grid[(current[0], current[1])][1] = counter


current = [0, 0]

counter = 0
for direction in wire2_dir:
    if direction[0] == "R":
        for x in range(int(direction[1:])):
            current[0] += 1
            counter += 1
            if grid[(current[0], current[1])][0] == 1:
                grid[(current[0], current[1])][1] += counter
                grid[(current[0], current[1])][0] = 2

    elif direction[0] == "L":
        for x in range(int(direction[1:])):
            current[0] -= 1
            counter += 1
            if grid[(current[0], current[1])][0] == 1:
                grid[(current[0], current[1])][1] += counter
                grid[(current[0], current[1])][0] = 2
    elif direction[0] == "D":
        for x in range(int(direction[1:])):
            current[1] -= 1
            counter += 1
            if grid[(current[0], current[1])][0] == 1:
                grid[(current[0], current[1])][1] += counter
                grid[(current[0], current[1])][0] = 2
    elif direction[0] == "U":
        for x in range(int(direction[1:])):
            current[1] += 1
            counter += 1
            if grid[(current[0], current[1])][0] == 1:
                grid[(current[0], current[1])][1] += counter
                grid[(current[0], current[1])][0] = 2

steps = []

for key in grid:
    if grid[key][0] >= 2:
        steps.append(grid[key][1])

print(min(steps))