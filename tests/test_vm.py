
from cantus.vm import CantusVM

def test_math_logic():
    vm = CantusVM()
    program = [("PUSH", 2), ("PUSH", 3), ("MUL", 0), ("PUSH", 4), ("ADD", 0)]
    result = vm.execute(program)
    assert result[-1] == 10
