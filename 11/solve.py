from collections import defaultdict


class Machine:

    def __init__(self, opcodes):
        self.outputs = []
        self.inputs = []
        self.ip = 0
        self.halted = False
        self.tape = defaultdict(lambda: 0)
        self.relative_base = 0

        for index, opcode in enumerate(opcodes):
            self.tape[index] = opcode

    def reset(self):
        self.ip = 0
        self.halted = False
        self.outputs = []
        self.inputs = []

    def parameter_mode(self, instruction):
        instruction = list(str(instruction))
        paramter_modes = ([0] * (5 - len(instruction))) + instruction
        try:
            if int(paramter_modes[2]) == 0:
                param1_value = self.tape[self.ip + 1]
            elif int(paramter_modes[2]) == 1:
                param1_value = self.ip + 1
            else:
                param1_value = self.tape[self.ip + 1] + self.relative_base

        except:
            print("except")
            param1_value = None
        try:
            if int(paramter_modes[1]) == 0:
                param2_value = self.tape[self.ip + 2]
            elif int(paramter_modes[1]) == 1:
                param2_value = self.ip + 2
            else:
                param2_value = self.tape[self.ip + 2] + self.relative_base
        except:
            print("except")
            param2_value = None
        try:
            if int(paramter_modes[0]) == 0:
                param3_value = self.tape[self.ip + 3]
            elif int(paramter_modes[0]) == 1:
                param3_value = self.ip + 3
            else:
                param3_value = self.tape[self.ip + 3] + self.relative_base
        except:
            print("except")
            param3_value = None

        return param1_value, param2_value, param3_value

    def run(self, inputs):
        self.inputs += inputs
        instruction = self.tape[self.ip]
        opcode = int(str(instruction)[-2:])
        while opcode != 99:
            param1, param2, param3 = self.parameter_mode(instruction)

            if opcode == 1:
                self.tape[param3] = self.tape[param1] + self.tape[param2]
                self.ip += 4

            if opcode == 2:
                self.tape[param3] = self.tape[param1] * self.tape[param2]
                self.ip += 4

            if opcode == 3:
                if len(self.inputs) == 0:
                    return

                self.tape[param1] = int(self.inputs.pop(0))
                self.ip += 2

            if opcode == 4:
                self.outputs.append(self.tape[param1])
                self.ip += 2

            if opcode == 5:
                if self.tape[param1] != 0:
                    self.ip = self.tape[param2]
                else:
                    self.ip += 3

            if opcode == 6:
                if self.tape[param1] == 0:
                    self.ip = self.tape[param2]
                else:
                    self.ip += 3

            if opcode == 7:
                if self.tape[param1] < self.tape[param2]:
                    self.tape[param3] = 1
                else:
                    self.tape[param3] = 0
                self.ip += 4

            if opcode == 8:
                if self.tape[param1] == self.tape[param2]:
                    self.tape[param3] = 1
                else:
                    self.tape[param3] = 0
                self.ip += 4

            if opcode == 9:
                self.relative_base += self.tape[param1]
                self.ip += 2

            instruction = self.tape[self.ip]
            opcode = int(str(instruction)[-2:])

        self.halted = True
        return

opcodes = open("input.txt").read().split(",")
opcodes = list(map(int, opcodes))

machine = Machine(opcodes)

WHITE = 1
BLACK = 0

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, 1)
DOWN = (0, -1)


grid = defaultdict(lambda: BLACK)

current = (0, 0)
direction = UP

machine.run([grid[current]])
while not machine.halted:
    color = machine.outputs[-2]
    turn = machine.outputs[-1]

    grid[current] = color

    if turn == 0:
        if direction == UP:
            direction = LEFT
        elif direction == LEFT:
            direction = DOWN
        elif direction == DOWN:
            direction = RIGHT
        elif direction == RIGHT:
            direction = UP

    elif turn == 1:
        if direction == UP:
            direction = RIGHT
        elif direction == RIGHT:
            direction = DOWN
        elif direction == DOWN:
            direction = LEFT
        elif direction == LEFT:
            direction = UP

    current = (current[0] + direction[0], current[1] + direction[1])

    machine.run([grid[current]])

print("Part 1: ", len(grid.values()))

machine = Machine(opcodes)

WHITE = 1
BLACK = 0

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, 1)
DOWN = (0, -1)


grid = defaultdict(lambda: BLACK)

current = (0, 0)
direction = UP

grid[current] = WHITE

machine.run([grid[current]])
while not machine.halted:
    color = machine.outputs[-2]
    turn = machine.outputs[-1]

    grid[current] = color

    if turn == 0:
        if direction == UP:
            direction = LEFT
        elif direction == LEFT:
            direction = DOWN
        elif direction == DOWN:
            direction = RIGHT
        elif direction == RIGHT:
            direction = UP

    elif turn == 1:
        if direction == UP:
            direction = RIGHT
        elif direction == RIGHT:
            direction = DOWN
        elif direction == DOWN:
            direction = LEFT
        elif direction == LEFT:
            direction = UP

    current = (current[0] + direction[0], current[1] + direction[1])

    machine.run([grid[current]])

max_x = max([item[0][0] for item in grid.items()])
max_y = min([item[0][1] for item in grid.items()])

pixels = [[0 for x in range(max_x + 1)] for y in range(abs(max_y) + 1)]

for point, value in grid.items():
    pixels[point[1] + abs(max_y)][point[0]] = value

for x in range(len(pixels) - 1, -1, -1):
    for y in range(len(pixels[x])):
        if pixels[x][y] == WHITE:
            print("█", end="")
        else:
            print(" ", end="")

    print()


