INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'


class Token:

    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"


class Interpreter:

    def __init__(self, expression):
        self.expression = expression.strip()
        self.pos = 0
        self.current_token: Token | None = None

    def is_expression_ended(self):
        return self.pos == len(self.expression)

    def get_next_token(self):

        if self.pos == len(self.expression):
            return Token(EOF, None)

        while self.expression[self.pos].isspace():
            self.pos += 1

        if self.expression[self.pos] == '+':
            self.pos += 1
            return Token(PLUS, '+')

        if self.expression[self.pos] == '-':
            self.pos += 1
            return Token(MINUS, '-')

        digits = []
        while self.expression[self.pos].isdigit():
            digits.append(self.expression[self.pos])
            self.pos += 1
            if self.pos == len(self.expression):
                break
        return Token(INTEGER, int(''.join(digits)))

    def eat(self, expected_type: str | tuple):
        self.current_token = self.get_next_token()
        if isinstance(expected_type, str):
            if self.current_token.type != expected_type:
                raise Exception('Parsing error')
        if isinstance(expected_type, tuple):
            if self.current_token.type not in expected_type:
                raise Exception('Parsing error')

    def parse(self):

        self.eat(INTEGER)
        result = self.current_token.value

        while not self.is_expression_ended():
            self.eat((PLUS, MINUS))
            op = self.current_token

            self.eat(INTEGER)
            right = self.current_token.value

            if op.type == PLUS:
                result = result + right
            elif op.type == MINUS:
                result = result - right

        return result


i = Interpreter('1+2 ')
result = i.parse()
print(result)
