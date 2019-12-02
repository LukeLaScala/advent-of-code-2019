codes = [int(x) for x in open('2.txt').readline().split(',')]

index = 0

while codes[index] != 99:
    if codes[index] == 1:
        summation = codes[codes[index + 1]] + codes[codes[index + 2]]
        codes[codes[index + 3]] = summation

    elif codes[index] == 2:
        product = codes[codes[index + 1]] * codes[codes[index + 2]]
        codes[codes[index + 3]] = product

    index += 4

print(str(codes[0]))
