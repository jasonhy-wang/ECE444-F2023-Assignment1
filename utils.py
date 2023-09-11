class Utils:
    def reversed(self, n):
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        return int(str(n)[::-1])

    def formatter(self, n):
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        #slice off the first two character to remote prefix
        binary = bin(n)[2:]
        octal = oct(n)[1:]
        return binary, octal
