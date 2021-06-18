def in_it(dict, y):
    x = dict.get(y)
    return x

def transform():
    dict = {}
    d = [
        ('Hendrix' , '1942'),
        ('Allman' , '1946'),
        ('King' , '1925'),
        ('Clapton' , '1945'),
        ('Johnson' , '1911'),
        ('Berry' , '1926'),
        ('Vaughan' , '1954'),
        ('Cooder' , '1947'),
        ('Page' , '1944'),
        ('Richards' , '1943'),
        ('Hammett' , '1962'),
        ('Cobain' , '1967'),
        ('Garcia' , '1942'),
        ('Beck' , '1944'),
        ('Santana' , '1947'),
        ('Ramone' , '1948'),
        ('White' , '1975'),
        ('Frusciante', '1970'),
        ('Thompson' , '1949'),
        ('Burton' , '1939')
    ]
    for x, y in d:
        if (in_it(dict, y) == None):
            dict[y] = x
        else:
            dict[y] = " ".join((dict[y], x))
    print('\n'.join("{}: {}".format(k, v) for k, v in dict.items()))

if __name__ == '__main__':
    transform()
