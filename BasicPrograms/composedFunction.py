def add(x:int)->int:
    return x+2
def multiply(x:int)->int:
    return x*2

def composed(X:int)->int:
    return add(multiply(X))

print(composed(4))
