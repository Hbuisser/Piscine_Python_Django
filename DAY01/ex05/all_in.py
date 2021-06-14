import sys

def capital(arg, states, capital_cities):
    x = states.get(arg)
    y = capital_cities.get(x)
    if (y != None):
        print(y)

def state(arg, states, capital_cities):
    for x, y in capital_cities.items():
        if (arg == y):
            for k, v in states.items():
                if (x == v):
                    print(k)

def all_in(arg, states, capital_cities):
    if len(sys.argv) != 2:
        return;
    list = arg.split(',')
    #check deux virgule d'affile
    for i in list:
        new_i = " ".join(i.split())
        new_i = new_i.capitalize()
        list[list.index(i)] = new_i
    print(list)
    # for y in list:
    #     capital(y, states, capital_cities)
    for k in list:
        state(k, states, capital_cities)


if __name__ == '__main__':
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersay" : "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR" : "Salem",
        "AL" : "Montgomery",
        "NJ" : "Trenton",
        "CO" : "Denver"
    }
    all_in(sys.argv[1], states, capital_cities)
