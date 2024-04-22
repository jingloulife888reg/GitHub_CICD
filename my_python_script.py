def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    # Simple test cases
    print("Testing add function:")
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

    print("Testing subtract function:")
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0

    print("Testing multiply function:")
    assert multiply(2, 3) == 6
    assert multiply(-1, 2) == -2

    print("Testing divide function:")
    assert divide(6, 2) == 3
    assert divide(10, 5) == 2

    print("All tests passed!")
