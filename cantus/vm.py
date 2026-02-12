
class CantusVM:
    def __init__(self):
        self.reset()

    def reset(self):
        self.stack = []
        self.memory = [0] * 1024
        self.pc = 0
        self.labels = {}
        self.running = True

    def load_labels(self, tokens):
        for i, (op, arg) in enumerate(tokens):
            if op == "LABEL":
                self.labels[arg] = i

    def execute(self, tokens):
        self.reset()
        self.load_labels(tokens)

        while self.pc < len(tokens) and self.running:
            op, arg = tokens[self.pc]
            self.pc += 1

            if op in (None, "LABEL"):
                continue

            try:
                # Stack
                if op == "PUSH": self.stack.append(arg)
                elif op == "POP": self.stack.pop()
                elif op == "DUP": self.stack.append(self.stack[-1])
                elif op == "SWAP": self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

                # Math
                elif op == "ADD": self.stack.append(self.stack.pop() + self.stack.pop())
                elif op == "SUB":
                    b,a=self.stack.pop(),self.stack.pop()
                    self.stack.append(a-b)
                elif op == "MUL": self.stack.append(self.stack.pop() * self.stack.pop())
                elif op == "DIV":
                    b,a=self.stack.pop(),self.stack.pop()
                    self.stack.append(a//b if b else 0)

                # Memory
                elif op == "STORE":
                    val,addr=self.stack.pop(),self.stack.pop()
                    self.memory[addr%1024]=val
                elif op == "LOAD":
                    addr=self.stack.pop()
                    self.stack.append(self.memory[addr%1024])

                # Control
                elif op == "JMP": self.pc=self.labels.get(arg,self.pc)
                elif op == "JZ":
                    if self.stack.pop()==0:
                        self.pc=self.labels.get(arg,self.pc)
                elif op == "HALT": self.running=False

                # Self-modifying (dangerous)
                elif op == "POKE":
                    val,addr=self.stack.pop(),self.stack.pop()
                    if 0<=addr<len(tokens):
                        tokens[addr]=("PUSH",val)

                # Output
                elif op == "PRINT": print(self.stack[-1])

            except Exception:
                continue

        return self.stack
