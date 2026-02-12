
OPCODES = {
    "PUSH":1,"POP":2,"DUP":3,"SWAP":4,
    "ADD":5,"SUB":6,"MUL":7,"DIV":8,
    "STORE":9,"LOAD":10,"JMP":11,"JZ":12,
    "PRINT":13,"HALT":14,"POKE":15,"LABEL":0
}

def compile(tokens):
    bytecode=[]
    for op,arg in tokens:
        code=OPCODES.get(op,0)
        bytecode.append(code)
        if isinstance(arg,int):
            bytecode.append(arg)
    return bytecode
