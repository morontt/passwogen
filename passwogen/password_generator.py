__author__ = 'morontt'

import hashlib
import re


class PasswordGenerator:

    def __init__(self, salt, domain):
        self.salt = salt
        self.domain = domain
        self.symbols = []

        self.init_symbols()
        self.symbols_len = len(self.symbols)

    def init_symbols(self):
        for i in xrange(ord('0'), ord('9') + 1):
            self.symbols.append(chr(i))

        for i in xrange(ord('a'), ord('z') + 1):
            self.symbols.append(chr(i))

        for i in xrange(ord('A'), ord('Z') + 1):
            self.symbols.append(chr(i))

        for s in ['!', '@', '#', '$', '%', '&', '*', '?', '+', '_']:
            self.symbols.append(s)

    def generate(self):
        sha = hashlib.sha1(hashlib.sha1(self.salt).hexdigest())
        sha.update(self.domain)

        hash_password = sha.hexdigest()
        password = self.convert_hash(hash_password)

        while True:
            if self.check_strength(password):
                break
            hash_password = hashlib.sha1(hash_password).hexdigest()
            password = self.convert_hash(hash_password)

        return password

    def convert_hash(self, hashstring):

        integer_hash = int(hashstring, 16)
        password = ''
        for i in range(10):
            modulo = integer_hash % self.symbols_len
            password += self.symbols[modulo]
            integer_hash = (integer_hash - modulo) / self.symbols_len

        return password

    def check_strength(self, password):
        strength = 0

        if re.search(r'([0-9])', password):
            strength += 1

        if re.search(r'([a-z])', password):
            strength += 1

        if re.search(r'([A-Z])', password):
            strength += 1

        if re.search(r'([!,@,#,$,%,&,*,?,+,_])', password):
            strength += 1

        return True if strength == 4 else False