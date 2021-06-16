

class Text(str):
    def __str__(self):
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')

class Elem:
    class ValidationError(Exception):
        def __init__(self):
            self.message = "This content is not a Text or an Elem."
        def __str__(self):
            return self.message
    
    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag # h1, h2, p, etc
        self.attr = attr
        self.content = []
        self.tag_type = tag_type # balise simple (juste au debut) ou double
        if content:
            self.add_content(content)
        elif content != None:
            if not isinstance(content, Text):
                raise Elem.ValidationError

    def __str__(self):
        attr = self.__make_attr()
        if self.tag_type == 'double':
            result = "<" + self.tag + attr + ">"
            result += self.__make_content()
            result += "</" + self.tag + ">"
        elif self.tag_type == 'simple':
            result = "<" + self.tag + attr + ">"
        return result
        # attribut = ""
        # if self.content == None:
        #     self.content = ""
        # if type(self.content) == Elem:
        #     # if (type(self.content) == Elem):
        #     #     str(Elem)
        #     self.content = str(Elem())
        #     self.content = "\n  " + self.content + "\n"
        # if type(self.content) == list:
        #     s = "\n"
        #     for index, obj in enumerate(self.content):
        #         if index < len(self.content):
        #             s = s + "  " + str(obj) + "\n"
        #     self.content = s
        # if len(self.attr) != 0:
        #     for key, value in attr.items():
        #         attribut = attribut + " " + key + "="  + value
        #     attribut = attribut[1:]
        # if self.tag_type == 'double':
        #     result = "<" + self.tag + attribut + ">" + self.content + "</" + self.tag + ">"
        # elif self.tag_type == 'simple':
        #     result = "<" + self.tag + attribut + ">"
        #     if (self.tag == "img"):
        #         result = result[:-1] + "/>"
        # print("------------------------")
        # print(result)
        # print("------------------------")
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
            result += "  " + str(elem).replace('\n', '\n  ') + "\n"
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
