__author__ = 'morontt'


class PasswordGenerator:

    def __init__(self, salt, domain):
        self.salt = salt
        self.domain = domain