

def acronym(lst):
    try:
        return map(lambda x: x[0] ,lst)
    except TypeError:
        print("Nie podano listy znaków jako parametr")


def median(lst):
    try:       
        try:
            dl = len(lst)
        except TypeError:
            print("Nie podano listy liczb jako parametr")
        lst.sort()
        if(all([isinstance(elem,int) for elem in lst])):
            if dl%2 != 0: 
                return lst[dl//2]      
            return (lst[dl//2-1]+lst[dl//2+1])/2
        else:
            print("Podana lista zawiera wartości niebędące int")
    except AttributeError:
        print("Parametr musi być listą liczb")


def pierwiastek(liczba,e):
    if e>0 and e<1 :
        a = 1
        b = liczba
        try:
            def newton(a,b):
                if abs(a-b)<e:          
                    return ((a+b)/2)
                else:                                    
                    return newton((a+b)/2,liczba/a)    
            return newton(a,b)
        except TypeError:
            print("Nie podano liczby jako parametr!")
    else:
        print("Podano ujemny epsilon")


def make_alpha_dict(chars):
    dictionary = {}
    try:
        words= chars.rsplit(' ')
        chars_list = [x for x in chars if x!=' ']
        if chars_list != []:
            def iterate(i):
                char = chars_list[i]
                dictionary[char] = [word for word in words if (char in word)]
                if i+1==len(chars_list):
                    return dict(sorted(dictionary.items(), key=lambda x: x[0]))
                else:
                    return iterate(i+1)
            return iterate(0)
        else:
            print("Podany łańcuch nie zawiera słów!")
    except AttributeError:
        print("Podany parametr nie jest ciągiem znaków!")


def flatten(lst):
    if isinstance(lst,list): 
        if len(lst) == 0:  
            return []
        else:
            return flatten(lst[0]) + flatten(lst[1:])  # spłaszcz pierwszy element i resztę listy
    else:  # jeśli element jest skalar
        return [lst]  # zwróć listę jednoelementową zawierającą skalar


