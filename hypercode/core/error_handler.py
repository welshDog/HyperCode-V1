from .tokens import Token, TokenType

def report_parse_error(token: Token, message: str) -> None:
    if token.type == TokenType.EOF:
        report(token.line, " at end", message)
    else:
        report(token.line, f" at '{token.lexeme}'", message)

def report(line: int, where: str, message: str) -> None:
    print(f"[line {line}] Error{where}: {message}")
