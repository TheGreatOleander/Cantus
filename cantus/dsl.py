
def parse(source):
    tokens=[]
    for line in source.splitlines():
        line=line.strip()
        if not line or line.startswith("#"): continue
        parts=line.split()
        op=parts[0].upper()
        arg=parts[1] if len(parts)>1 else None

        if op=="PUSH": tokens.append(("PUSH",int(arg)))
        elif op in {"ADD","SUB","MUL","DIV","POP","DUP","SWAP","STORE","LOAD","PRINT","HALT"}:
            tokens.append((op,0))
        elif op in {"LABEL","JMP","JZ"}:
            tokens.append((op,arg))
        elif op=="POKE":
            tokens.append(("POKE",0))
        else:
            raise ValueError(f"Unknown opcode {op}")
    return tokens
