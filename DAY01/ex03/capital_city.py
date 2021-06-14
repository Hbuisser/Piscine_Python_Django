import sys

def capital(arg):
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
    x = states.get(arg)
    if (x == None):
        print("Unkown state")
        return;
    y = capital_cities.get(x)
    print(y)

if __name__ == '__main__':
    capital(sys.argv[1])
