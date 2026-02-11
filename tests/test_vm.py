from cantus.vm import CantusVM

def test_add():
    vm = CantusVM()
    result = vm.execute([("PUSH", 2), ("PUSH", 3), ("ADD", 0)])
    assert result[-1] == 5
