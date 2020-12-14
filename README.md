# Enforce Type Hints
Decorator that enforces Type hints on functions (Python)

# Example Usage
main.py
```py
from enforceTH import enforceType


@enforceType
def doubler(x : int, y: int) -> int:
	value = x + y

print(doubler("Hello",3)) # Fails
print(doubler(3,3)) # Successful
```

