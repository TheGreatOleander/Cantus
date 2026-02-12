
from cantus.vm import CantusVM
from cantus.dsl import parse_cantus

def test_add():
    vm = CantusVM()
    tokens = parse_cantus("PUSH 2\nPUSH 3\nADD")
    result = vm.execute(tokens)
    assert result[-1] == 5
