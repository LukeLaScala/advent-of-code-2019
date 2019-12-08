import sys

sys.setrecursionlimit(20000)
class Node:
    parent = None
    children = []
    value = None
    depth = 0

    def __init__(self, value, parent=None, depth=0):
        self.children = []
        self.value = value
        self.parent = parent
        self.depth = depth

    def __repr__(self):
        return "<{}>".format(self.value)


def update_depths(node):
    node.depth = node.parent.depth + 1

    if len(node.children) == 0:
        return

    for child in node.children:
        update_depths(child)

nodes = []

orbits = [orbit.strip() for orbit in open('input.txt').readlines()]

for orbit in orbits:
    orbitee_value = orbit.split(')')[0]
    orbiter_value = orbit.split(')')[1]

    orbitee = None
    orbiter = None

    for node in nodes:
        if node.value == orbitee_value:
            orbitee = node

    if orbitee is None:
        orbitee = Node(orbitee_value)
        nodes.append(orbitee)

    for node in nodes:
        if node.value == orbiter_value:
            orbiter = node
            orbiter.parent = orbitee
            orbitee.children.append(orbiter)
            update_depths(orbiter)

    if orbiter is None:
        orbiter = Node(orbiter_value, parent=orbitee)
        orbitee.children.append(orbiter)
        update_depths(orbiter)
        nodes.append(orbiter)

print("Part 1: " + str(sum([node.depth for node in nodes])))

visited = []


def search(node, counter):
    if node.value == "SAN":
        return counter

    if node.value in visited:
        return

    visited.append(node.value)

    for n in [node.parent] + node.children:
        if node.depth != 0:
            num = search(n, counter + 1)
            if num:
                return num


for node in nodes:
    if node.value == "YOU":
        you = node
        print("Part 2: " + str(search(you, 0) - 2))