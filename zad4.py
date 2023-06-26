from zad6 import log


def make_generator(f):
    #n = 1
    def generator():
        n=1
        while True:
            yield f(n)
            n += 1
    return generator()

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib_generator = make_generator(fib)
#print("Ciąg Fibonacciego")
#for i in range(10):
#        print(next(fib_generator))

geo_generator = make_generator(lambda n: 2 ** n)
#print("Ciąg geometryczny")
#for i in range(10):
#    print(next(geo_generator))

