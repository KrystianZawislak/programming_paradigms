# Exercise 6 — Multiplication Table 12x12

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 6 — Multiplication Table](../../../class_exercises/2_control_statements/06_multiplication_table/) by Piotr Pawlik
> Date: 2026-11-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program wypisujący tabliczkę mnożenia 12x12 w postaci jak poniżej:

```
    |   1   2   3   4   5   6   7   8   9  10  11  12
-----------------------------------------------------
  1 |   1   2   3   4   5   6   7   8   9  10  11  12
  2 |   2   4   6   8  10  12  14  16  18  20  22  24
  3 |   3   6   9  12  15  18  21  24  27  30  33  36
itd.
```

Liczby powinny być w kolumnach z wyrównaniem do prawej. W wersji uproszczonej można pominąć "ozdobniki" (linie oraz numery kolumn i wierszy). Do wyrównania użyj formatowania wydruku f-napisami (np. `{x:4}` wypisuje x na 4 pozycjach).

**UWAGA:** Aby wypisywać liczby kilkoma printami w jednym wierszu należy ustawić dodatkowy parametr funkcji print - `end`:

Na przykład:

```python
print(5, end="")
print(6, end="")
```

wypisze:

```
56
```

### 🇬🇧 Task description (EN)

Write a program that prints a 12x12 multiplication table in the form below:

```
    |   1   2   3   4   5   6   7   8   9  10  11  12
-----------------------------------------------------
  1 |   1   2   3   4   5   6   7   8   9  10  11  12
  2 |   2   4   6   8  10  12  14  16  18  20  22  24
  3 |   3   6   9  12  15  18  21  24  27  30  33  36
etc.
```

The numbers should be in right-aligned columns. In the simplified version you can skip the "decorations" (lines and column/row numbers). For the alignment use output formatting with f-strings (e.g. `{x:4}` prints x on 4 positions).

**NOTE:** To print numbers with several `print` calls in one line, set the additional parameter of `print` - `end`:

For example:

```python
print(5, end="")
print(6, end="")
```

prints:

```
56
```

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
