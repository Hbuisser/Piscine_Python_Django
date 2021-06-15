
class Intern:
    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        self.name = name
    def __str__(self):
        return self.name
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
    def work(self):
        raise Exception("I'am just an intern, I can't do that...")
    def make_coffee(self):
        return self.Coffee

if __name__ == '__main__':
    m = Intern("Mark")
    n = Intern()
    print(m.__str__())
    print(n.__str__())
    m_order = m.make_coffee()
    print(m_order.__str__(m_order))
    n_order = n.make_coffee()
    print(n_order.__str__(n_order))
    try:
        n.work()
    except Exception as error:
        print(error)