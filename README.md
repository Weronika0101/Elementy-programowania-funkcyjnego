# Elementy-programowania-funkcyjnego

Napisanie skryptów miało za zadanie: 
- Zapoznanie z elementami programowania funkcyjnego w Python
- Zapoznanie z tworzeniem iteratorów i generatorów
- Zapoznanie z tworzeniem dekoratorów

  W ramach programu wykonano następujące funkcje:
- Funkcja acronym, która przyjmuje na wejściu listę ciągów znaków zwraca akronim
zbudowany z tych ciągów znaków.
- Funkcja median, która przyjmuje na wejściu listę liczb i zwraca ich medianę
- Funkcja obliczająca pierwiastek kwadratowy metodą Netwona
- Funkcja make_alpha_dict, która przyjmuje na wejściu ciąg znaków, a zwraca na
wyjściu słownik, w którym kluczami są znaki występujące alfabetyczne
występujące ciągu, a wartościami listy słów zawierających te znaki
- Funkcja flatten spłaszczająca listy
- forall(pred, iterable) - funkcja która zwraca True, jeśli każdy element iterable
spełnia predykat pred, w przeciwnym przypadku False
- exists(pred, iterable) – funkcja która zwraca True, jeśli co najmniej jeden
element iterable spełnia predykat pred, w przeciwnym przypadku False
- atleast(n, pred, iterable) – funkcja zwracająca True, jeśli co najmniej n
elementów iterable spełnia predykat pred, w przeciwnym przypadku False
- atmost(n, pred, iterable) – funkcja zwracająca True, jeśli co najwyżej n
elementów iterable spełnia predykat pred, w przeciwnym przypadku False

Skonstruowano też klasę PasswordGenerator, która obsługuje protokół iteratora.
Iterator zwraca kolejne losowo generowane hasła( parametry: długość hasła, zestaw znaków, z których losowo będą tworzone hasła, maksymalnq liczba haseł do wygenerowania).

Wykorzystując domknięcia, skonstruowano funkcję make_generator zwracającą generator.
Make_generator przyjmuje jako parametr jednoargumentową funkcję f i
zwraca generator. Generator leniwie oblicza wartości funkcji f dla kolejnych
argumentów, rozpoczynając od 1. 

Dokładniejszy opis działania wszystkich funkcji i klas wraz z wywołaniami znajduje się w pliku przyklady-dzialania.pdf
