import sys, os, re

def render(arg):
    f = open("settings.py", "r")
    data = f.readlines()
    f.close()
    t = open(arg, "r")
    text = t.read()
    t.close()
    dico = {}
    for i in data:
        i = i.split(" = ")
        v = i[1].rstrip('\n')
        v = v[1:-1]
        dico[i[0]] = v
    for key, value in dico.items():
        key = "{" + key + "}"
        text = re.sub(key, value, text)
    file = open("result.html", "w")
    file.write(text)
    file.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Enter one and only one argument")
        sys.exit(1)
    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print("File not found")
        sys.exit(1)
    if not os.path.isfile(filepath):
        print("Path is not a file")
    elif not filepath.endswith('.template'):
        print("Wrong file extension")
        sys.exit(1)
    render(sys.argv[1])
