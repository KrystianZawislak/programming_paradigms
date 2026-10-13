# Exercise 2 — Sum and Product (return value vs. pointer)

> Course: Programming Paradigms
> Date: 2026-10-13

## Task

### 🇵🇱 Treść zadania (PL)

Napisz w C funkcję wyliczającą sumę i iloczyn dwóch liczb całkowitych. Przy czym suma ma być zwracana przez return a iloczyn przez adres (C).

Czyli funkcja ma mieć 3 parametry - dwie liczby całkowite oraz wskaźnik/referencję do liczby całkowitej.

W main zdefiniuj tylko jedną zmienną, tą do której do której funkcja wpisze iloczyn.
Następnie jednym printf-em wypisz iloczyn i sumę dowolnych dwóch liczb (w tej kolejności, sumę wypisujemy bezpośrednio - jako wynik działania funkcji).

Wynik zapewne będzie w porządku - ale proszę sprawdzić co się stanie gdy zamienimy kolejność (najpierw suma potem iloczyn)? Potrafisz wytłumaczyć co się stało?

### 🇬🇧 Task description (EN)

Write a C function that computes the sum and the product of two integers. The sum should be returned with `return`, and the product through an address (C).

In other words, the function should take 3 parameters - two integers and a pointer/reference to an integer.

In `main`, define only one variable - the one the function will write the product into.
Then, using a single `printf`, print the product and the sum of any two numbers (in that order; the sum is printed directly - as the function's return value).

The result will probably be fine - but check what happens when you swap the order (sum first, then product). Can you explain what happened?

## Files

| File     | Description |
| -------- | ----------- |
| `main.c` | Solution - one `printf`, product first, then sum. The swapped version (sum first, then product) is commented out below it. |

## How to run

macOS / Linux:

```bash
cc main.c -o main && ./main
```

Windows (MinGW):

```powershell
gcc main.c -o main.exe; .\main.exe
```

To check the swapped order, comment out the first `printf`, uncomment the second one and compile again.

Example output (Apple clang 17, arm64, no optimization):

```
product = -101924776, sum = 7    # product first
sum = 7, product = 12            # swapped
```

The output depends on the compiler and optimization level (with `-O2` both versions print `12`).
