def fuel(mass):
	if mass <= 0:
		return 0
	
	return mass + fuel(int(mass / 3) - 2)

print(sum([fuel(int(int(mass) / 3 - 2)) for mass in open('1.txt')]))