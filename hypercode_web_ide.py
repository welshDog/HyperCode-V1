import sys
import os
import io
from contextlib import redirect_stdout
from flask import Flask, request, jsonify, send_file

# Add the organized directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "hypercode_organized_v2"))

from hypercode.core.lexer import Lexer
from hypercode.core.parser import Parser
from hypercode.core.interpreter import Interpreter

app = Flask(__name__)


@app.route("/")
def ide():
    return send_file("ide.html")


@app.route("/run", methods=["POST"])
def run_code():
    data = request.json
    source = data.get("code", "")

    # Capture stdout
    f = io.StringIO()
    with redirect_stdout(f):
        try:
            lexer = Lexer(source)
            tokens = lexer.scan_tokens()

            parser = Parser(tokens)
            program = parser.parse()

            interpreter = Interpreter()
            interpreter.interpret(program)
        except Exception as e:
            print(f"Error: {e}")

    output = f.getvalue()
    return jsonify({"output": output})


if __name__ == "__main__":
    print("Starting HyperCode Web IDE on http://localhost:8000")
    app.run(port=8000, debug=True)
