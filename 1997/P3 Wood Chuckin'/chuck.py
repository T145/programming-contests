with open('chuck.in') as f:
	for line in f:
		name, kilos = line.split()
		print('{0} the woodchuck can chuck {1} kilograms of wood.'.format(name, int(kilos) * 5))
