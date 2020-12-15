# Enforce Type Hints
Decorator that enforces Type hints on functions (Python)

# Example Usage
Regular Functions
```py
from enforceTH import enforceType

@enforceType
def doubler(x : int, y: int) -> int:
	value = x + y
	return value

print(doubler("Hello",3)) # Fails
print(doubler(3,3)) # Successful

```

Classes (self requires the "object" annotation)
```py
from enforceTH import enforceType

class Person:

	@enforceType
	def __init__(self : object, name : str, age : int, job : str) -> None:
		self.name = name
		self.age = age
		self.job = job
	

	def giveName(self):
		return self.name
	
	def giveAge(self):
		return self.age
	
	def giveJob(self):
		return self.job


x = Test("John Doe",18,"Software Developer")
print(x.giveName())
```



