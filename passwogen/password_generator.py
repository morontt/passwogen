__author__ = 'morontt'


class PasswordGenerator:

    def __init__(self, salt, domain):
        self.salt = salt
        self.domain = domain
        self.symbols = []

        self.init_symbols()

    def init_symbols(self):
        for i in xrange(ord('0'), ord('9') + 1):
            self.symbols.append(chr(i))

        for i in xrange(ord('a'), ord('z') + 1):
            self.symbols.append(chr(i))

        for i in xrange(ord('A'), ord('Z') + 1):
            self.symbols.append(chr(i))

        for s in ['!', '%', '&', '@', '#', '$', '^', '*', '?', '_', '~']:
            self.symbols.append(s)

    def generate(self):
        password = ''
        for s in self.symbols:
            password += s

        return password