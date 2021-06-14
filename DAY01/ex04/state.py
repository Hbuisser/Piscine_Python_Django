import sys

def state(arg):
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
    if len(sys.argv) != 2:
        return;
    for x, y in capital_cities.items():
        if (arg == y):
            for k, v in states.items():
                if (x == v):
                    print(k)
                    return;
    print("Unkown state")

if __name__ == '__main__':
    state(sys.argv[1])
