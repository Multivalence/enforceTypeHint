# Enforce Type Hints
Decorator that enforces Type hints on functions (Python)

# Example Usage
main.py
```py
from enforceTH import enforceType

#All type hints are required (Including return)
@enforceType() # returnValue is set to True by default
def doubler(x : int, y: int) -> int:
	value = x + y
	return value

print(doubler("Hello",3)) # Fails
print(doubler(3,3)) # Successful

#All type hints except return are required
@enforceType(returnValue=False)
def foo(x : float, y : float):
	value = x + y
	return value

print(foo("Hello",3)) # Fails
print(foo(3.0,3.2)) # Successful

```

**Note**
In order for the decorator to check the return value, it calls the function. There is currently no way to avoid doing this. If you don't want your function to be called by the decorator, set returnValue equal to False.

