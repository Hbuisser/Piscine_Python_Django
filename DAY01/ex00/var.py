
def my_var():
    i = 42
    print(i, "est de type",  type(i))
    str = "42"
    print(str, "est de type",  type(str))
    str = "quarante-deux"
    print(str, "est de type",  type(str))
    f = 42.0
    print(f, "est de type",  type(f))
    x = True
    print(x, "est de type",  type(x))
    l = [42]
    print(l, "est de type",  type(l))
    d = {42: 42}
    print(d, "est de type",  type(d))
    t = (42,)
    print(t, "est de type",  type(t))
    s = set()
    print(s, "est de type",  type(s))


if __name__ == '__main__':
    my_var()
