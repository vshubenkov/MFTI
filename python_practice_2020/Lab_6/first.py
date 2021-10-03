
x = 10

def printer(a):
    x = 20
    print(a)
    print(x)
    a = 40
    print(a)
    print(__name__)

printer(x)
print(x)
print(__name__)