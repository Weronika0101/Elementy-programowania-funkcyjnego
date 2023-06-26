from zad1 import acronym,median,pierwiastek,make_alpha_dict,flatten
from zad2 import for_all,exists,atleast,atmost

#print(list(acronym(['Zakład', 'Ubezpieczeń', 'Społecznych'])))
#print(list(acronym([])))
#print(list(acronym(7)))

#print(median([1,1,19,2,3,4,4,5,1]))
#print(median([1,1,4,4]))
#print(median('ch'))
#print(median(7))
#print(median(['s','k']))

#print(pierwiastek(3,0.001))
#print(pierwiastek('a',0.001))
#print(pierwiastek(3,-0.001))

#print(make_alpha_dict('on i ona'))
#print(make_alpha_dict('   '))
#print(make_alpha_dict(7))

#print(flatten([1, [2, 3], [[4, 5], 6]]))
#print(flatten('p'))

#print(for_all(lambda x: x%2==0,[4,7,2,6,8,8,2]))
#print(for_all(lambda x: x%2==0,[4,2,2,6,8,8,2]))
#print(for_all(lambda x: x%2==0,4))

#print(exists(lambda x: x%2==0,[3,5,7,9,9]))
#print(exists(lambda x: x%2==0,[3,5,2,9,9]))

#print(atleast(3, lambda x: x>0,[2,7,9,-8,-2]))
#print(atleast(3, lambda x: x>0,[2,7,0,-8,-2]))

print(atmost(3, lambda x: x>0,[2,7,9,-8,-2]))
print(atmost(3, lambda x: x>0,[2,7,-3,-8,-2]))
print(atmost(3, lambda x: x>0,[2,7,8,8,-2,2]))
print(atmost(3, lambda x: x>0,[0,-2,2]))

