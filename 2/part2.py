

def run(noun, verb):
    codes = [int(x) for x in open('2.txt').readline().split(',')]
    codes[1] = noun
    codes[2] = verb

    index = 0

    while codes[index] != 99:
        if codes[index] == 1:
            summation = codes[codes[index + 1]] + codes[codes[index + 2]]
            codes[codes[index + 3]] = summation

        elif codes[index] == 2:
            product = codes[codes[index + 1]] * codes[codes[index + 2]]
            codes[codes[index + 3]] = product

        index += 4

    return codes[0]

expected = 19690720

for noun in range(0, 99):
    for verb in range(0, 99):
        if run(noun, verb) == expected:
            print(100 * noun + verb)
            exit()

print("No results found")
