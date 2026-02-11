class CantusVM:
    def __init__(self):
        self.stack = []
        self.memory = [0] * 256

    def execute(self, tokens):
        for op, arg in tokens:
            if op == "PUSH":
                self.stack.append(arg)
            elif op == "ADD":
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
        return self.stack
