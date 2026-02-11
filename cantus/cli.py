from cantus.vm import CantusVM
from cantus.tokenizer import tokenize

def main():
    vm = CantusVM()
    tokens = tokenize(None)
    print("STACK:", vm.execute(tokens))

if __name__ == "__main__":
    main()
