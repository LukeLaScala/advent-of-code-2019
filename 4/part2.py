from collections import defaultdict

bounds = open('input.txt').readline().split('-')

passwords = []
for x in range(int(bounds[0]), int(bounds[1]), 1):
    password = str(x)

    increasing = True
    for y in range(len(password) - 1):
        if password[y] > password[y + 1]:
            increasing = False

    doubles_map = defaultdict(lambda: 0)
    for y in range(len(password) - 1):
        if password[y] == password[y + 1]:
            doubles_map[password[y]] += 1

    doubles = any(reps == 1 for reps in doubles_map.values())

    if doubles and increasing:
        passwords.append(password)

print(len(passwords))



