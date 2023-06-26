from collections.abc import Iterable
    
    
def for_all(pred,iterable):
    if isinstance(iterable,Iterable):
        it = iter(iterable)
        try:
            element = next(it)
        except StopIteration:
            return True
        else:
            return pred(element) and for_all(pred,it)
    else:
        print("Parametr nie jest typem iterable!")


def exists(pred,iterable):
    if isinstance(iterable,Iterable):
        it = iter(iterable)
        try:
            element = next(it)
        except StopIteration:
            return False
        else:
            return pred(element) or exists(pred,it)
    else:
        print("Parametr nie jest typem iterable!")

def atleast(n,pred,iterable):
    if isinstance(iterable,Iterable):
        it = iter(iterable)
        try:
            element = next(it)
        except StopIteration:
            return False
        else:
            return pred(element) and (n==1 or atleast(n-1,pred,it)) or atleast(n,pred,it)
    else:
        print("Parametr nie jest typem iterable!")


def atmost(n, pred, iterable):
    if not isinstance(iterable, Iterable):
        print("Parametr nie jest typem iterable!")
        return False

    try:
        it=iter(iterable)
        element = next(it)
        #print(element)
    except StopIteration:
        return True and n >= 0

    if pred(element):
        return n > 0 and atmost(n - 1, pred, it)
    else:
        return atmost(n, pred, it)