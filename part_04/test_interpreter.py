import unittest


class LexerTestCase(unittest.TestCase):
    def makeLexer(self, text):
        from calc import Lexer
        lexer = Lexer(text)
        return lexer

    def test_lexer_integer(self):
        from calc import INTEGER
        lexer = self.makeLexer('234')
        token = lexer.get_next_token()
        self.assertEqual(token.type, INTEGER)
        self.assertEqual(token.value, 234)

    def test_lexer_mul(self):
        from calc import MUL
        lexer = self.makeLexer('*')
        token = lexer.get_next_token()
        self.assertEqual(token.type, MUL)
        self.assertEqual(token.value, '*')

    def test_lexer_div(self):
        from calc import DIV
        lexer = self.makeLexer(' / ')
        token = lexer.get_next_token()
        self.assertEqual(token.type, DIV)
        self.assertEqual(token.value, '/')


class InterpreterTestCase(unittest.TestCase):
    def makeInterpreter(self, text):
        from calc import Lexer, Interpreter
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        return interpreter

    def test_expression1(self):
        interpreter = self.makeInterpreter('7 * 4 / 2')
        result = interpreter.expr()
        self.assertEqual(result, 14)

    def test_expression2(self):
        interpreter = self.makeInterpreter('7 * 4 / 2 * 3')
        result = interpreter.expr()
        self.assertEqual(result, 42)

    def test_expression3(self):
        interpreter = self.makeInterpreter('10 * 4  * 2 * 3 / 8')
        result = interpreter.expr()
        self.assertEqual(result, 30)


if __name__ == '__main__':
    unittest.main()
