import sys
import os
from cantus.vm import CantusVM
from cantus.tokenizer import tokenize

def main():
    print("● CANTUS | Executable Music Engine v0.1")
    print("---------------------------------------")
    
    audio_file = sys.argv[1] if len(sys.argv) > 1 else None
    
    try:
        tokens = tokenize(audio_file)
        print(f"ASM: {tokens}")
        
        vm = CantusVM()
        result = vm.execute(tokens)
        
        print(f"RESULT: {result}")
        print("---------------------------------------")
        print("Execution Successful.")
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")

if __name__ == "__main__":
    main()