from cantus.vm import CantusVM

def test_math_logic():
    vm = CantusVM()
    # (2 * 3) + 4 = 10
    program = [("PUSH", 2), ("PUSH", 3), ("MUL", 0), ("PUSH", 4), ("ADD", 0)]
    result = vm.execute(program)
    assert result[-1] == 10

def test_stack_manipulation():
    vm = CantusVM()
    # PUSH 5, DUP -> [5, 5]
    program = [("PUSH", 5), ("DUP", 0)]
    result = vm.execute(program)
    assert result == [5, 5]

def test_jump_logic():
    vm = CantusVM()
    # PUSH 0, IF_ZERO (skips next), PUSH 99, PUSH 1
    # Result should be [0, 1] because 99 was skipped
    program = [("PUSH", 0), ("IF_ZERO", 0), ("PUSH", 99), ("PUSH", 1)]
    result = vm.execute(program)
    assert 99 not in result