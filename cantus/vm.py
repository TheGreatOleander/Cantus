class CantusVM:
    def __init__(self):
        self.stack = []
        self.memory = [0] * 256  # 256 Addressable memory slots
        self.pc = 0

    def execute(self, tokens):
        self.stack = []
        self.pc = 0
        
        while self.pc < len(tokens):
            op, arg = tokens[self.pc]
            self.pc += 1
            
            try:
                # --- Arithmetic ---
                if op == "PUSH": self.stack.append(arg)
                elif op == "ADD": self.stack.append(self.stack.pop() + self.stack.pop())
                elif op == "SUB":
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(a - b)
                elif op == "MUL": self.stack.append(self.stack.pop() * self.stack.pop())
                elif op == "DIV":
                    b, a = self.stack.pop(), self.stack.pop()
                    self.stack.append(a // b if b != 0 else 0)

                # --- Memory (The "Sampler" Opcodes) ---
                elif op == "STORE": 
                    val, addr = self.stack.pop(), self.stack.pop()
                    self.memory[addr % 256] = val
                elif op == "LOAD":
                    addr = self.stack.pop()
                    self.stack.append(self.memory[addr % 256])

                # --- Control Flow ---
                elif op == "JUMP":
                    self.pc = self.stack.pop() % len(tokens)
                elif op == "IF_ZERO":
                    if self.stack.pop() == 0: self.pc += 1

                # --- Stack Manipulation ---
                elif op == "DUP": self.stack.append(self.stack[-1])
                elif op == "SWAP" and len(self.stack) >= 2:
                    self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
                elif op == "DROP": self.stack.pop()
                elif op == "OVER": self.stack.append(self.stack[-2])
                elif op == "ROT" and len(self.stack) >= 3:
                    top, mid, bot = self.stack.pop(), self.stack.pop(), self.stack.pop()
                    self.stack.extend([mid, top, bot])

            except (IndexError, ZeroDivisionError):
                continue
        return self.stack