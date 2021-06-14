
def numbers():
    f = open("./numbers.txt", "r")
    str = f.read()
    #print(type(str))
    x = str.split(",")
    #print(x)
    for i in x:
        print(i)

if __name__ == '__main__':
    numbers()
