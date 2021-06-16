

class Text(str):
    def __str__(self):
        return super().__str__().replace('\n', '\n<br />\n')

class Elem:
    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag # h1, h2, p, etc
        self.attr = attr
        self.content = content
        self.tag_type = tag_type # balise simple (juste au debut) ou double

    def __str__(self):
        attribut = ""
        if self.content == None:
            self.content = ""
        if type(self.content) == Elem:
            self.content = str(Elem())
            self.content = "\n  " + self.content + "\n"
        if len(self.attr) != 0:
            for key, value in attr.items():
                attribut = attribut + " " + key + "="  + value
            attribut = attribut[1:]
        if self.tag_type == 'double':
            result = "<" + self.tag + attribut + ">" + self.content + "</" + self.tag + ">" ##
        elif self.tag_type == 'simple':
            result = "<" + self.tag + attribut + ">"
            if (self.tag == "img"):
                result = result[:-1] + "/>"
        print(result)
        return result

    def __make_attr(self):
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += [...]
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))
