import sys
import unittest
from io import StringIO

from hypercode.core.interpreter import Interpreter
from hypercode.core.lexer import Lexer
from hypercode.core.parser import Parser


def run_code(source: str) -> str:
    """A helper function to run code and capture stdout."""
    old_stdout = sys.stdout
    sys.stdout = new_stdout = StringIO()

    try:
        lexer = Lexer(source)
        tokens = lexer.scan_tokens()
        parser = Parser(tokens)
        statements = parser.parse()
        interpreter = Interpreter()
        interpreter.interpret(statements)
    finally:
        sys.stdout = old_stdout

    return new_stdout.getvalue()


class TestInterpreter(unittest.TestCase):
    def test_if_statement_then(self):
        code = """
        var x = 10;
        if (x > 5) {
            print("then");
        } else {
            print("else");
        }
        """
        output = run_code(code)
        self.assertEqual(output.strip(), "then")

    def test_if_statement_else(self):
        code = """
        var x = 0;
        if (x > 5) {
            print("then");
        } else {
            print("else");
        }
        """
        output = run_code(code)
        self.assertEqual(output.strip(), "else")

    def test_function_call(self):
        code = """
        fun sayHi() {
            print("hi");
        }
        sayHi();
        """
        output = run_code(code)
        self.assertEqual(output.strip(), "hi")

    def test_function_with_parameters(self):
        code = """
        fun sayName(name) {
            print("hi, " + name);
        }
        sayName("HyperCode");
        """
        output = run_code(code)
        self.assertEqual(output.strip(), "hi, HyperCode")

    def test_function_with_return(self):
        code = """
        fun add(a, b) {
            return a + b;
        }
        var result = add(3, 4);
        print(result);
        """
        output = run_code(code)
        self.assertEqual(output.strip(), "7")

    def test_recursive_function_call(self):
        code = """
        fun fib(n) {
            if (n < 2) {
                return n;
            }
            return fib(n - 2) + fib(n - 1);
        }
        var result = fib(10);
        print(result);
        """
        output = run_code(code)
        self.assertEqual(output.strip(), "55")

    def test_scoping(self):
        code = """
        var a = "global";
        {
            var a = "local";
            print(a);
        }
        print(a);
        """
        output = run_code(code)
        self.assertEqual(output.strip(), "local\nglobal")


if __name__ == "__main__":
    unittest.main()
