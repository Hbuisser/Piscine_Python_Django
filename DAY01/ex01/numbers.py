
def numbers():
    f = open("./numbers.txt", "r")
    s = f.read()
    f.close()
    s = s.split(",")
    for i in s:
        if "\n" in i:
            i = i[:-1]
        print(i)

if __name__ == '__main__':
    numbers()
