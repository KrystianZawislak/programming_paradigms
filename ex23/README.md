# Exercise 23 — Bisection Method

> Course: Programming Paradigms
> Date: 2026-11-06

## Task

### 🇵🇱 Treść zadania (PL)

Napisz funkcję wyznaczającą miejsce zerowe dowolnej funkcji f(x) w zadanym przedziale, metodą bisekcji. Funkcja powinna otrzymywać 4 parametry: funkcję f, oraz x1, x2 jako początek i koniec przedziału w którym należy szukać miejsca zerowego a także eps - dokładność obliczeń

Za pomocą napisanej funkcji należy wyznaczyć miejsce zerowe:

- sinusa w przedziale (-1.5 , 1) oraz
- wielomianu (funkcja do samodzielnego napisania):

  $$y = x^3 - 2x^2 + 4x - 1$$

  w przedziale (-10, 10) - z dokładnością 0.001

### 🇬🇧 Task description (EN)

Write a function that finds the root of any function f(x) in a given interval, using the bisection method. The function should take 4 parameters: the function f, x1 and x2 as the start and the end of the interval in which the root should be searched for, and eps - the accuracy of the computation.

Using the function, find the root of:

- sine in the interval (-1.5 , 1) and
- the polynomial (a function to be written yourself):

  $$y = x^3 - 2x^2 + 4x - 1$$

  in the interval (-10, 10) - with the accuracy 0.001

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - `finding_zeros_using_the_bisection_method(function, x1, x2, eps)` halves the interval while it is wider than `eps`, keeping the half in which the function changes sign; `polynomial` implements x³ - 2x² + 4x - 1. |

## How to run

macOS / Linux:

```bash
python3 main.py
```

Windows:

```powershell
py main.py
```

Example output:

```
-0.0003662109375
0.2850341796875
```

Exact roots for comparison: sin(x) = 0 at x = 0, the polynomial at x ≈ 0.28477.
