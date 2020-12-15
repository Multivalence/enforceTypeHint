# Enforce Type Hints
Decorator that enforces Type hints on functions (Python)

# Example Usage
main.py
```py
from enforceTH import enforceType

@enforceType
def doubler(x : int, y: int) -> int:
	value = x + y
	return value

print(doubler("Hello",3)) # Fails
print(doubler(3,3)) # Successful

```
**Note** that decorator currently does not work within classes but will in the future.


