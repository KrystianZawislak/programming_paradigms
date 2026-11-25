# Exercise 2 — Difference and Quotient (return value vs. pointer)

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 2 — Sum and Product (return value vs. pointer)](../../../class_exercises/1_unstructured_programming/02_sum_and_product_pointer/) by Piotr Pawlik
> Date: 2026-11-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz w C funkcję wyliczającą różnicę i iloraz (całkowity) dwóch liczb całkowitych. Przy czym różnica ma być zwracana przez return a iloraz przez adres (C).

Czyli funkcja ma mieć 3 parametry - dwie liczby całkowite oraz wskaźnik/referencję do liczby całkowitej.

W main zdefiniuj tylko jedną zmienną, tą do której funkcja wpisze iloraz.
Następnie jednym printf-em wypisz iloraz i różnicę dowolnych dwóch liczb (w tej kolejności, różnicę wypisujemy bezpośrednio - jako wynik działania funkcji).

Wynik zapewne będzie w porządku - ale proszę sprawdzić co się stanie gdy zamienimy kolejność (najpierw różnica potem iloraz)? Potrafisz wytłumaczyć co się stało?

### 🇬🇧 Task description (EN)

Write a C function that computes the difference and the (integer) quotient of two integers. The difference should be returned with `return` and the quotient through an address (C).

So the function should have 3 parameters - two integers and a pointer/reference to an integer.

In `main`, define only one variable - the one into which the function will write the quotient.
Then, with a single `printf`, print the quotient and the difference of any two numbers (in this order; the difference is printed directly - as the result of the function call).

The result will probably be fine - but check what happens when we swap the order (first the difference, then the quotient)? Can you explain what happened?

## Files

| File | Description |
| ---- | ----------- |
| `main.c` | Solution - not written yet. |

## How to run

macOS / Linux:

```bash
cc main.c -o ex2
./ex2
```

Windows (MinGW):

```powershell
gcc main.c -o ex2.exe
.\ex2.exe
```
