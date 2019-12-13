import math

grid = []
for line in [line.strip() for line in open('input.txt').readlines()]:
    grid.append(line)


def reduce(point):
    x = point[0]
    y = point[1]

    neg_x = False
    if x < 0:
        x *= -1
        neg_x = True

    neg_y = False
    if y < 0:
        y *= -1
        neg_y = True

    upper_bound = max((len(grid), len(grid[0])))
    for divisor in range(2, upper_bound):
        if (x >= divisor or y >= divisor) and x % divisor == 0 and y % divisor == 0:
            reduced = reduce((int(x / divisor), int(y / divisor)))
            if neg_x:
                reduced = (reduced[0] * -1, reduced[1])
            if neg_y:
                reduced = (reduced[0], reduced[1] * -1)

            return reduced


    return point


def visible(p1):
    blocked = [p1]

    for asteroid in asteroids:

        vector = (asteroid[0] - p1[0], asteroid[1] - p1[1])
        vector = reduce(vector)

        scalar = 1
        target = (vector[0] * scalar + asteroid[0], vector[1] * scalar + asteroid[1])
        while vector != (0, 0) and 0 <= target[0] < len(grid) and 0 <= target[1] < len(grid[vector[0]]):
            if target not in blocked:
                blocked.append(target)

            scalar += 1
            target = (vector[0] * scalar + asteroid[0], vector[1] * scalar + asteroid[1])

    return [asteroid for asteroid in asteroids if asteroid not in blocked]


def get_angle(point):
    x = point[0] - station[0]
    y = point[1] - station[1]

    if x >= 0 and y < 0:
        return math.atan(abs(x) / abs(y))

    if x >= 0 and y > 0:
        offset = math.pi / 2

        if x == 0:
            return math.pi

        return math.atan(abs(y) / abs(x)) + offset

    if y >= 0 and x < 0:
        offset = math.pi

        if y == 0:
            return 3 * math.pi / 2

        return math.atan(abs(x) / abs(y)) + offset

    if x < 0 and y < 0:
        offset = 3 * math.pi / 2
        return math.atan(abs(y) / abs(x)) + offset

    return 0

asteroids = []

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] == "#":
            asteroids.append((y, x))


max_visible = 0
best_asteroid = None
station = None
for asteroid in asteroids:
    num_visible = len(visible(asteroid))
    if num_visible > max_visible:
        max_visible = num_visible
        station = asteroid

print("Part 1: ", max_visible)

visible_asteroids = sorted(visible(station), key=get_angle)

print("Part 2: ", visible_asteroids[199][0] * 100 + visible_asteroids[199][1])


