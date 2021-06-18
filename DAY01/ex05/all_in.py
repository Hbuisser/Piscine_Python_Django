import sys

def get_state():
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	return states

def get_capital_cities():
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	return (capital_cities)

def check_state(arg, states, capital_cities):
	for key, value in capital_cities.items():
		if arg == value:
			for x, y in states.items():
				if key == y:
					return (x)
	return (-1)

def check_cities(arg, states, capital_cities):
	x = states.get(arg)
	if x == None:
		return (-1)
	else:
		return (capital_cities[x])

def all_in():
	if len(sys.argv) != 2:
		return
	states = get_state()
	capital_cities = get_capital_cities()
	arg = sys.argv[1]
	lst = arg.split(',')
	for i in lst:
		new_i = " ".join(i.split())
		lst[lst.index(i)] = new_i
	for j in lst:
		if check_cities(j.title(), states, capital_cities) != -1:
			print(check_cities(j.title(), states, capital_cities), "is the capital of", j.title())
		elif check_state(j.title(), states, capital_cities) != -1:
			print(j.title(), "is the capital of", check_state(j.title(), states, capital_cities))
		elif j != "":
			print(j, "is neither a capital city nor a state")

if __name__ == '__main__':
    all_in()
