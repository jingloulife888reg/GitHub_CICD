import script

def test_script():
    # Simple test cases
    print("Testing add function:")
    assert script.add(2, 3) == 5
    assert script.add(-1, 1) == 0

    print("Testing subtract function:")
    assert script.subtract(5, 3) == 2
    assert script.subtract(0, 0) == 0

    print("Testing multiply function:")
    assert script.multiply(2, 3) == 6
    assert script.multiply(-1, 2) == -2

    print("Testing divide function:")
    assert script.divide(6, 2) == 3
    assert script.divide(10, 5) == 2

    print("All tests passed!")
