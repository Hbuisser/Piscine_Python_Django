import sys

def capital():  
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    if len(sys.argv) != 2:
        return
    arg = sys.argv[1]
    x = states.get(arg)
    if (x == None):
        print("Unkown state")
        return
    y = capital_cities.get(x)
    print(y)

if __name__ == '__main__':
    capital()
