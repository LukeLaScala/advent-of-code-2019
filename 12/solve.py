class Moon:

    def __init__(self, x, y, z, id):
        self.x = x
        self.y = y
        self.z = z
        self.velocity = [0, 0, 0]
        self.id = id

    def pos(self):
        return self.x, self.y, self.z

    def apply_gravity(self, others):
        for other in others:
            if other.id != self.id:
                self.velocity[0] += -1 if self.x > other.x else 1 if other.x > self.x else 0
                self.velocity[1] += -1 if self.y > other.y else 1 if other.y > self.y else 0
                self.velocity[2] += -1 if self.z > other.z else 1 if other.z > self.z else 0

    def apply_velocity(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.z += self.velocity[2]

    def energy(self):
        return sum([abs(value) for value in (self.x, self.y, self.z)]) * sum([abs(value) for value in self.velocity])

    def __repr__(self):
        return "POS: " + str(self.pos()) + ", VEL: " + str(self.velocity)

moons = []
positions = []

for counter, line in enumerate(open('input.txt').readlines()):
    split = line.split('=')
    x = split[1][0:split[1].index(',')]
    y = split[2][0:split[2].index(',')]
    z = split[3][0:split[3].index('>')]
    moons.append(Moon(int(x), int(y), int(z), counter))

for x in range(1000000):
    for moon in moons:
        moon.apply_gravity(moons)
    for moon in moons:
        moon.apply_velocity()
    if sum([moon.energy() for moon in moons]) in positions:
        print("HIT")
    positions.append(sum([moon.energy() for moon in moons]))

    print(x) if x % 1000 == 0 else None
print("Part 1: ", sum([moon.energy() for moon in moons]))
