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
                #print("param 1 value " + str(param1_value))
                #print("relative base: " + str(self.relative_base))
                #print(self.ip)

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
machine.run([1])
print("Part 1: ", machine.outputs[-1])
machine = Machine(opcodes)
machine.run([2])

print("Part 2: ", machine.outputs[-1])

