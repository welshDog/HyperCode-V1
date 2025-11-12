import sys
from .repl import run_repl, run

def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                source = f.read()
            run(source)
        except FileNotFoundError:
            print(f"Error: File not found at '{filepath}'")
            sys.exit(1)
    else:
        run_repl()

if __name__ == "__main__":
    main()