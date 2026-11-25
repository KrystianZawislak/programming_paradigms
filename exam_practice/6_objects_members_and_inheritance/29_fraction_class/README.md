# Exercise 29 — Fraction Class (operator overloading)

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 29 — Fraction Class (operator overloading)](../../../class_exercises/6_objects_members_and_inheritance/29_fraction_class/) by Piotr Pawlik
> Date: 2026-11-25

## Task

### 🇵🇱 Treść zadania (PL)

Napisz klasę reprezentującą ułamki zwykłe niewłaściwe. Obiekt tej klasy ma być tworzony poprzez podanie licznika i mianownika. Klasa ma obsługiwać operacje: dodawanie, odejmowanie, mnożenie i dzielenie ułamków zwykłych. Operacje powinny wykorzystywać standardowe operatory tych działań (+, -, *, /) (podpowiedź: zdefiniuj dla tej klasy odpowiednie metody specjalne). Po operacjach ułamki powinny zostać skrócone.
Do realizacji np. dodawania przyda się metoda licząca najmniejszą wspólną wielokrotność (NWW). NWW można wyliczyć obliczając wcześniej największy wspólny dzielnik dwóch liczb (NWD). Ta metoda również przyda się przy skracaniu ułamków. Obie metody zaimplementuj jako prywatne.
Zdefiniuj także odpowiednią metodę specjalną, aby można wypisywać print-em ułamek zwykły w postaci licznik/mianownik. Np. ułamek u o liczniku 5 i mianowniku 8 powinien w wyniku wywołania print(u) wyświetlić:

```
5/8
```

Sprawdź, czy wszystko działa i następnie uzupełnij klasę tak, aby można było utworzyć obiekt ułamek zarówno przez podanie licznika i mianownika (poprzez `__init__`) jak i przez metodę klasową (o nazwie fromdecimal) otrzymującą ułamek dziesiętny i zwracającą ułamek zwykły - czyli obiekt naszej klasy.
Uzupełnij też klasę o mechanizm pozwalający wypisać ile w danym momencie istnieje obiektów tej klasy (utwórz prywatny - w sensie nieosiągalny spoza klasy - atrybut klasy dostępny przez statyczną metodę o nazwie count) - ten atrybut ma być zwiększany przy konstrukcji obiektu i zmniejszany przy destrukcji).

W main stwórz ułamek u1 o wartości 10/4 oraz ułamek u2 odpowiadający dziesiętnemu 0.375, wypisz je i wykonaj na nich wszystkie 4 operacje arytmetyczne (+, -, *, /) wypisując wyniki.

Wypisz aktualną liczbę obiektów klasy. Wykonaj u2=u1 i ponownie wypisz aktualną liczbę obiektów klasy. Potrafisz powiedzieć dlaczego teraz jest o jeden mniej i który obiekt został usunięty?

### 🇬🇧 Task description (EN)

Write a class representing improper common fractions. An object of this class should be created by giving the numerator and the denominator. The class should support the operations: addition, subtraction, multiplication and division of common fractions. The operations should use the standard operators of these operations (+, -, *, /) (hint: define the appropriate special methods for this class). After the operations the fractions should be reduced.
To implement e.g. addition, a method computing the least common multiple (LCM) will be useful. The LCM can be computed by first computing the greatest common divisor of two numbers (GCD). This method will also be useful for reducing fractions. Implement both methods as private.
Also define the appropriate special method so that a common fraction can be printed with `print` in the form numerator/denominator. E.g. a fraction u with the numerator 5 and the denominator 8 should display, as a result of calling `print(u)`:

```
5/8
```

Check that everything works and then extend the class so that a fraction object can be created both by giving the numerator and the denominator (through `__init__`) and by a class method (named `fromdecimal`) that takes a decimal fraction and returns a common fraction - i.e. an object of our class.
Also extend the class with a mechanism that allows printing how many objects of this class exist at a given moment (create a private - in the sense of unreachable from outside the class - class attribute accessible through a static method named `count`) - this attribute should be increased when an object is constructed and decreased when it is destroyed.

In `main`, create a fraction u1 with the value 10/4 and a fraction u2 corresponding to the decimal 0.375, print them and perform all 4 arithmetic operations (+, -, *, /) on them, printing the results.

Print the current number of objects of the class. Execute `u2=u1` and print the current number of objects of the class again. Can you say why there is one fewer now, and which object was destroyed?

## Files

| File | Description |
| ---- | ----------- |
| `main.py` | Solution - not written yet. |

## How to run

macOS / Linux:

```bash
python3 main.py
```

Windows:

```powershell
py main.py
```
