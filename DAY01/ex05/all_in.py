import sys

def check_state(arg, states, capital_cities):
	for key, value in capital_cities.items():
		if arg == value:
			for x, y in states.items():
				if key == y:
					return (x)
		else:
			return (-1)
def check_cities(arg, states, capital_cities):
	x = states.get(arg)
	if x == None:
		return (-1)
	else:
		return (capital_cities[x])

def all_in(arg, states, capital_cities):
    if len(sys.argv) != 2:
        return;
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
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey" : "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR" : "Salem",
        "AL" : "Montgomery",
        "NJ" : "Trenton",
        "CO" : "Denver"
    }
    all_in(sys.argv[1], states, capital_cities)
