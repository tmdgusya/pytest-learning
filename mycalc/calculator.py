
class Calculator:

    def add(self, a, b):
        if not isinstance(a, (int, float)) or (not isinstance(b, (int, float))):
            raise TypeError('The arguments must be a number.')
        return a + b

    def sub(self, a, b):
        if not isinstance(a, (int, float)) or (not isinstance(b, (int, float))):
            raise TypeError('The arguments must be a number.')
        return a - b

    def div(self, a, b):
        if not isinstance(a, (int, float)) or (not isinstance(b, (int, float))):
            raise TypeError('The arguments must be a number.')
        return a / b