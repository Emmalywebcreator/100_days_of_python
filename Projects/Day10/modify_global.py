x = 10

def modify_glob(x):
    return x + 3
x = modify_glob(x)
print(x)

i = 50

def foo():
    i = 150
    return i
foo()
print(i)