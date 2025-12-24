import sys

from .repl import run, run_repl


def main():
    # Handle --version flag
    if len(sys.argv) > 1 and sys.argv[1] == "--version":
        print("HyperCode v0.2.0 - Think Spatially")
        return

    # Handle --help flag
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("HyperCode v0.2.0 - Spatial Programming Language")
        print()
        print("Usage:")
        print("  hypercode <file.hc>     Run a HyperCode program")
        print("  hypercode               Start interactive REPL")
        print("  hypercode --version     Show version")
        print("  hypercode --help        Show this help")
        print()
        print("Built for neurodivergent developers")
        print("Learn more: https://github.com/welshDog/hypercode")
        return

    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                source = f.read()
            run(source)
        except FileNotFoundError:
            print(f"Error: File not found at '{filepath}'")
            sys.exit(1)
    else:
        run_repl()


if __name__ == "__main__":
    main()
