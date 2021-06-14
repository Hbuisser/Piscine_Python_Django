def in_it(dict, y):
    x = dict.get(y)
    return x

def transform():
    dict = {}
    d = [
        ('Hendrix', '1942'),
        ('King', '1946'),
        ('Coucou', '1942'),
        ('Santa', '1941')
    ]
    for x, y in d:
        if (in_it(dict, y) == None):
            dict[y] = x
        else:
            dict[y] = " ".join((dict[y], x))
    print('\n'.join("{}: {}".format(k, v) for k, v in dict.items()))

if __name__ == '__main__':
    transform()
