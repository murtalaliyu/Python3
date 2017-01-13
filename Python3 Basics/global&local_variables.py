x = 6   #t x is not a global variable

def example():
    global x    # x is now a global variable
    print(x)
    x += 5
    print(x)
    
example()


def ex():
    globx = x
    print(globx)
    globx += 5
    print(globx)

    return globx

x = ex()
print(x)
