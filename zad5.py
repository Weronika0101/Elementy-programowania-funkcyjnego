from zad4 import make_generator,fib
from functools import cache,lru_cache

def make_generator_mem(f):
    @cache
    def f_cached(n):
        return f(n)
    return make_generator(f_cached)


fib_generator = make_generator_mem(fib)
print("Ciąg Fibonacciego zad5")
for i in range(10):
    print(next(fib_generator))


geo_generator = make_generator_mem(lambda n: 2 ** n)
print("Ciąg geometryczny zad5")
for i in range(10):
    print(next(geo_generator))