import functools


def enforceType(func):
	@functools.wraps(func)
	def wrapper(*args):
			wrapper.has_been_called = True
			x = func.__annotations__
			t = [x[i] for i in x if i != 'return']

			if len(args) != len(t):
				raise TypeError("Missing required positional arguments and/or annotations.")

			for i in range(len(t)):
				if not isinstance(args[i],t[i]):
					raise ValueError(f"Invalid literal for {t[i]}: {args[i]}")
			
			try:
				ReturnValue = x['return']
			
			except KeyError:
				raise TypeError("Missing required return value annotation.")
			
			RV = func(*args)

			if not isinstance(RV, ReturnValue):
				raise TypeError(f"Expected function to return {ReturnValue}. Got {type(RV)} instead.")

			return RV
	wrapper.has_been_called = False
	return wrapper
