# Exercise 21 — Numerical Derivative

> Course: Programming Paradigms
> Date: 2026-11-04

## Task

### 🇵🇱 Treść zadania (PL)

Napisz funkcję derivative, która otrzyma jako argumenty FUNKCJĘ (f), punkt, w którym liczymy pochodną (x) i przyrost (h), a zwróci przybliżoną wartość pochodnej funkcji f w punkcie x. Przybliżoną wartość pochodnej uzyskuje się ze wzoru na iloraz różnicowy:

$$\frac{f(x+h) - f(x)}{h}$$

Niech w funkcji derivative h będzie parametrem z wartością domyślną równą 0.0001

W main wypisz wartości funkcji derivative dla:

- sin(x) w punkcie 1
- sin(x) w punkcie 0
- x^2 w punkcie 1 z przyrostem 0.00001

Funkcja sin jest dostępna w module math (należy zaimportować moduł przez:

```python
import math
```

- wtedy funkcja sin będzie dostępna jako `math.sin`

Funkcję kwadratową x^2 należy zaimplementować samemu - wystarczy napisać funkcję otrzymującą x a zwracającą `x**2`.

### 🇬🇧 Task description (EN)

Write a function `derivative` that takes as arguments a FUNCTION (f), the point at which we compute the derivative (x) and the increment (h), and returns the approximate value of the derivative of f at the point x. The approximate value of the derivative is obtained from the difference quotient formula:

$$\frac{f(x+h) - f(x)}{h}$$

In the `derivative` function, let h be a parameter with the default value 0.0001.

In `main`, print the values of `derivative` for:

- sin(x) at the point 1
- sin(x) at the point 0
- x^2 at the point 1 with the increment 0.00001

The `sin` function is available in the `math` module (import the module with:

```python
import math
```

- then `sin` is available as `math.sin`).

Implement the quadratic function x^2 yourself - it is enough to write a function that takes x and returns `x**2`.

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - `derivative(function, critical_point, increase=0.0001)` returns the difference quotient; `quadratic_function` returns `number**2`. |

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
0.5402602314186211
0.9999999983333334
2.00001000001393
```

Exact values for comparison: cos(1) ≈ 0.5403, cos(0) = 1, (x²)' at 1 = 2.
