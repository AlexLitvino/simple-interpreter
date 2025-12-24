INTEGER, ADD, SUB, MLP, DIV, EOF = 'INTEGER', 'ADD', 'SUB', 'MLP', 'DIV', 'EOF'

class Token:

    def __init__(self, type, value):
        self.type = type
        self.value = value


class Lexer:

    def __init__(self, text):
        self.text: str = text
        self.pos = 0
        self.current_symbol: str = self.text[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos == len(self.text):
            self.current_symbol = None
        else:
            self.current_symbol = self.text[self.pos]

    def skip_spaces(self):
        while self.current_symbol is not None and self.current_symbol.isspace():
            self.advance()

    def integer(self):
        integer_str = ''
        while self.current_symbol is not None and self.current_symbol.isdigit():
            integer_str += self.current_symbol
            self.advance()
        return int(integer_str)

    def error(self):
        raise Exception('Invalid symbol')

    def get_next_token(self):

        while self.current_symbol is not None:

            if self.current_symbol.isspace():
                self.skip_spaces()
                continue

            if self.current_symbol.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_symbol == '+':
                self.advance()
                return Token(ADD, '+')

            if self.current_symbol == '-':
                self.advance()
                return Token(SUB, '-')

            if self.current_symbol == '*':
                self.advance()
                return Token(MLP, '*')

            if self.current_symbol == '/':
                self.advance()
                return Token(DIV, '/')

            self.error()

        return Token(EOF, None)


class Interpreter:

    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Parsing error')

    def eat(self, expected_type):
        if self.current_token.type != expected_type:
            self.error()
        else:
            self.current_token = self.lexer.get_next_token()

    def factor(self):
        result = self.current_token
        self.eat(INTEGER)
        return result.value

    def term(self):
        result = self.factor()
        while self.current_token.type in (MLP, DIV):
            if self.current_token.type == MLP:
                self.eat(MLP)
                result *= self.factor()
            elif self.current_token.type == DIV:
                self.eat(DIV)
                result //= self.factor()
        return result

    def expr(self):
        result = self.term()
        while self.current_token.type in (ADD, SUB):
            if self.current_token.type == ADD:
                self.eat(ADD)
                result += self.term()
            elif self.current_token.type == SUB:
                self.eat(SUB)
                result -= self.term()
        return result


lexer = Lexer('1+2*3 +4 - 5 * 1')
interpreter = Interpreter(lexer)
result = interpreter.expr()
print(result)