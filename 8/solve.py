WIDTH = 25
HEIGHT = 6
pixels = open('input.txt').read()
num_layers = int(len(pixels) / (WIDTH * HEIGHT))

layers = [[[0 for _ in range(WIDTH)] for _ in range(HEIGHT)] for _ in range(num_layers)]

for x in range(len(pixels)):
    pixel = int(pixels[x])

    layer_index = x // (WIDTH * HEIGHT)
    x_index = (x - (layer_index * WIDTH * HEIGHT)) % WIDTH
    y_index = (x - (layer_index * WIDTH * HEIGHT)) // WIDTH

    layers[layer_index][y_index][x_index] = pixel

min_layer = layers[0]
min_zeros = 999999
for layer in layers:
    zeros = 0
    for row in layer:
        for pixel in row:
            if pixel == 0:
                zeros += 1
    if zeros < min_zeros:
        min_zeros = zeros
        min_layer = layer

print("Part 1: " + str(sum(min_layer, []).count(1) * sum(min_layer, []).count(2)))

stacks = [[[0 for _ in range(num_layers)] for _ in range(WIDTH)] for _ in range(HEIGHT)]

for layer_number in range(len(layers)):
    for x in range(len(layers[layer_number])):
        for y in range(len(layers[layer_number][x])):
            pixel = layers[layer_number][x][y]
            stacks[x][y][layer_number] = pixel


def color(stack):
    for pixel in stack:
        if pixel == 1:
            return 0
        elif pixel == 0:
            return "█"


decoded = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

for x in range(len(stacks)):
    for y in range(len(stacks[x])):
        decoded[x][y] = color(stacks[x][y])

print("Part 2: ")
for x in range(len(decoded)):
    for y in range(len(decoded[x])):
        print(decoded[x][y], end="")
    print("")

