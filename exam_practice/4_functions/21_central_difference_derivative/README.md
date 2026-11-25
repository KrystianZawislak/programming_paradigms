# Exercise 21 — Numerical Derivative (central difference)

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 21 — Numerical Derivative](../../../class_exercises/4_functions/21_numerical_derivative/) by Piotr Pawlik
> Date: 2026-11-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz funkcję derivative, która otrzyma jako argumenty FUNKCJĘ (f), punkt, w którym liczymy pochodną (x) i przyrost (h), a zwróci przybliżoną wartość pochodnej funkcji f w punkcie x. Przybliżoną wartość pochodnej uzyskuje się ze wzoru na iloraz różnicowy centralny:

$$\frac{f(x+h) - f(x-h)}{2h}$$

Niech w funkcji derivative h będzie parametrem z wartością domyślną równą 0.001

W main wypisz wartości funkcji derivative dla:

- cos(x) w punkcie 0
- cos(x) w punkcie π/2
- x^3 w punkcie 2 z przyrostem 0.0001

Funkcja cos oraz liczba π są dostępne w module math (należy zaimportować moduł przez:

```python
import math
```

- wtedy funkcja cos będzie dostępna jako `math.cos`, a π jako `math.pi`)

Funkcję x^3 należy zaimplementować samemu - wystarczy napisać funkcję otrzymującą x a zwracającą `x**3`.

### 🇬🇧 Task description (EN)

Write a function `derivative` that takes as arguments a FUNCTION (f), the point at which we compute the derivative (x) and the increment (h), and returns the approximate value of the derivative of f at the point x. The approximate value of the derivative is obtained from the central difference quotient formula:

$$\frac{f(x+h) - f(x-h)}{2h}$$

In the `derivative` function, let h be a parameter with the default value 0.001.

In `main`, print the values of `derivative` for:

- cos(x) at the point 0
- cos(x) at the point π/2
- x^3 at the point 2 with the increment 0.0001

The `cos` function and the number π are available in the `math` module (import the module with:

```python
import math
```

- then `cos` is available as `math.cos`, and π as `math.pi`).

Implement the function x^3 yourself - it is enough to write a function that takes x and returns `x**3`.

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
