from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="html", attr=attr, content=content, tag_type='double')
        
class Head(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="head", attr=attr, content=content, tag_type='double')

class Body(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="body", attr=attr, content=content, tag_type='double')

class Title(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="title", attr=attr, content=content, tag_type='double')

class Meta(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="meta", attr=attr, content=content, tag_type='simple')

class Img(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="img", attr=attr, content=content, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="table", attr=attr, content=content, tag_type='double')

class Td(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="td", attr=attr, content=content, tag_type='double')

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="tr", attr=attr, content=content, tag_type='double')

class Th(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="th", attr=attr, content=content, tag_type='double')

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="ul", attr=attr, content=content, tag_type='double')

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="ol", attr=attr, content=content, tag_type='double')

class Li(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="li", attr=attr, content=content, tag_type='double')

class H1(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="h1", attr=attr, content=content, tag_type='double')

class H2(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="h2", attr=attr, content=content, tag_type='double')

class P(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="p", attr=attr, content=content, tag_type='double')

class Div(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="div", attr=attr, content=content, tag_type='double')

class Span(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="span", attr=attr, content=content, tag_type='double')

class Hr(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="hr", attr=attr, content=content, tag_type='simple')

class Br(Elem):
    def __init__(self, content=None, attr={}):
        Elem.__init__(self, tag="br", attr=attr, content=content, tag_type='simple')

def test():
    assert((str(Html())) == """<html></html>""")
    assert((str(Html(attr={'lang': 'en'}))) == """<html lang="en"></html>""")
    print("Html Test : OK.")
    assert((str(Div())) == """<div></div>""")
    assert((str(Div(attr={'lang': 'en'}))) == """<div lang="en"></div>""")
    print("Div Test : OK.")
    assert((str(Br())) == """<br>""")
    assert((str(Br(attr={'lang': 'en'}))) == """<br lang="en">""")
    print("Br Test : OK.")

if __name__ == '__main__':
    try:
        test()
        print('Tests succeeded!')
    except AssertionError as e:
        print(e)
    print("Html display : ")
    html = Elem('html', content = [Elem('head', content = Elem('title', content = Text('\"Hello ground!\"'))),
        Elem('body', content = [Elem('h1', content = Text("\"Oh no, no again!\"")),
            Elem('img', {'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type = 'simple')])])
    print(html)
