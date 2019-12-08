from itertools import permutations


class Machine:

    def __init__(self, opcodes):
        self.opcodes = opcodes
        self.reset_opcodes = [op for op in opcodes]
        self.outputs = []
        self.inputs = []
        self.ip = 0
        self.halted = False

    def reset(self):
        self.opcodes = self.reset_opcodes
        self.ip = 0
        self.halted = False
        self.outputs = []
        self.inputs = []

    def parameter_mode(self, instruction):
        instruction = list(str(instruction))
        paramter_modes = ([0] * (5 - len(instruction))) + instruction
        try:
            param1_value = self.opcodes[self.ip + 1] if int(paramter_modes[2]) == 0 else (self.ip + 1)
        except:
            param1_value = None
        try:
            param2_value = (self.opcodes[self.ip + 2] if int(paramter_modes[1]) == 0 else (self.ip + 2))
        except:
            param2_value = None
        try:
            param3_value = (self.opcodes[self.ip + 3] if int(paramter_modes[0]) == 0 else (self.ip + 3))
        except:
            param3_value = None

        return param1_value, param2_value, param3_value

    def run(self, inputs):
        self.inputs += inputs
        instruction = self.opcodes[self.ip]
        opcode = int(str(instruction)[-2:])
        while opcode != 99:
            param1, param2, param3 = self.parameter_mode(instruction)

            if opcode == 1:
                self.opcodes[param3] = self.opcodes[param1] + self.opcodes[param2]
                self.ip += 4

            if opcode == 2:
                self.opcodes[param3] = self.opcodes[param1] * self.opcodes[param2]
                self.ip += 4

            if opcode == 3:
                self.opcodes[param1] = int(self.inputs.pop(0))
                self.ip += 2

            if opcode == 4:
                self.outputs.append(self.opcodes[param1])
                self.ip += 2
                return

            if opcode == 5:
                if self.opcodes[param1] != 0:
                    self.ip = self.opcodes[param2]
                else:
                    self.ip += 3

            if opcode == 6:
                if self.opcodes[param1] == 0:
                    self.ip = self.opcodes[param2]
                else:
                    self.ip += 3

            if opcode == 7:
                if self.opcodes[param1] < self.opcodes[param2]:
                    self.opcodes[param3] = 1
                else:
                    self.opcodes[param3] = 0
                self.ip += 4

            if opcode == 8:
                if self.opcodes[param1] == self.opcodes[param2]:
                    self.opcodes[param3] = 1
                else:
                    self.opcodes[param3] = 0
                self.ip += 4

            instruction = self.opcodes[self.ip]
            opcode = int(str(instruction)[-2:])

        self.halted = True
        return


opcodes = open("input.txt").read().split(",")
opcodes = list(map(int, opcodes))

signals = []

a = Machine([x for x in opcodes])
b = Machine([x for x in opcodes])
c = Machine([x for x in opcodes])
d = Machine([x for x in opcodes])
e = Machine([x for x in opcodes])

machines = [a, b, c, d, e]

# Part 1
for perm in permutations(range(5)):
    a.inputs += [perm[0], 0]
    a.run([])
    b.inputs += [perm[1], a.outputs[-1]]
    b.run([])
    c.inputs += [perm[2], b.outputs[-1]]
    c.run([])
    d.inputs += [perm[3], c.outputs[-1]]
    d.run([])
    e.inputs += [perm[4], d.outputs[-1]]
    e.run([])
    signals.append((e.outputs[-1]))

    [machine.reset() for machine in machines]

print("Part 1: " + str(max(signals)))


signals = []

a = Machine([x for x in opcodes])
b = Machine([x for x in opcodes])
c = Machine([x for x in opcodes])
d = Machine([x for x in opcodes])
e = Machine([x for x in opcodes])

for perm in permutations(range(9, 4, -1)):
    a.inputs.append(perm[0])
    b.inputs.append(perm[1])
    c.inputs.append(perm[2])
    d.inputs.append(perm[3])
    e.inputs.append(perm[4])

    a.inputs.append(0)

    while not e.halted:
        a.run([])

        b.inputs.append(a.outputs[-1])
        b.run([])

        c.inputs.append(b.outputs[-1])
        c.run([])

        d.inputs.append(c.outputs[-1])
        d.run([])

        e.inputs.append(d.outputs[-1])
        e.run([])

        a.inputs.append(e.outputs[-1])

    signals.append(e.outputs[-1])

    a = Machine([x for x in opcodes])
    b = Machine([x for x in opcodes])
    c = Machine([x for x in opcodes])
    d = Machine([x for x in opcodes])
    e = Machine([x for x in opcodes])

print("Part 2: " + str(max(signals)))