
from cantus.vm import CantusVM
from cantus.dsl import parse_cantus

def start_repl():
    print("● CANTUS REPL v1.0")
    print("Type instructions. 'exit' to quit.")

    vm = CantusVM()

    while True:
        try:
            line = input(">>> ")
            if line.lower() in {"exit","quit"}:
                break
            tokens = parse_cantus(line)
            result = vm.execute(tokens)
            print("STACK:", result)
        except Exception as e:
            print("Error:", e)
