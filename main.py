def decorator(function):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = function(*args, **kwargs)
        return result
    wrapper.count = 0
    return wrapper

@decorator
def myFunction(a, b, c):
    print(a+b+c)

myFunction(1, 2, 3)
myFunction(4, 5, 6)
myFunction(7, 8 ,9)

print(f"\nfunction count - {myFunction.count}")
