# Exercise 6 — Multiplication Table

> Course: Programming Paradigms
> Date: 2026-10-14

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program wypisujący tabliczkę mnożenia 10x10 w postaci jak poniżej:

```
   |  1  2  3  4  5  6  7  8  9 10
---------------------------------
 1 |  1  2  3  4  5  6  7  8  9 10
 2 |  2  4  6  8 10 12 14 16 18 20
 3 |  3  6  9 12 15 18 21 24 27 30
itd.
```

Liczby powinny być w kolumnach z wyrównaniem do prawej. W wersji uproszczonej można pominąć "ozdobniki" (linie oraz numery kolumn i wierszy). Jak osiągnąć takie wyrównanie jest napisane poniżej w opisie formatowania wydruku.

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

#### Formatowania wydruku w Pythonie

Załóżmy, że chcemy wypisać liczbę 1-cyfrową na 9-ciu pozycjach (czyli dołożyć jej z przodu 8 spacji). Można to osiągnąć przez formatowanie wydruku.

W pythonie istnieje kilka sposobów na formatowanie wydruku (czyli np. tego jak wypisywane są liczby na ekran). Obecnie od Pythona 3.6 wprowadzone zostały f-napisy (f-strings). W tym podejściu przed napisem przekazywanym do funkcji print dodaje się literę f, natomiast zmienne, które do tej pory umieszczaliśmy po przecinkach są wstawiane do tego napisu otoczone nawiasami {} (czyli zamiast `print("Promień koła wynosi", r, "cm")` piszemy `print(f"Promień koła wynosi  {r} cm")`).

Taka notacja pozwala dołożyć informację o formatowaniu. Zadanie wypisania zmiennej x (przechowującej np. wartość 5) na 9-ciu pozycjach wyglądałoby tak:

```python
print(f"Liczba na dziewięciu pozycjach: {x:9}")
```

co wypisze:

```
Liczba na dziewięciu pozycjach:         5
```

Inne przykłady:

```python
print(f"Liczba na trzech pozycjach uzupełniona zerami {x:03}")
```

wypisze:

```
Liczba na trzech pozycjach uzupełniona zerami: 005
```

```python
print(f"Liczba z dwoma miejscami po przecinku: {x:.2f}")
```

wypisze:

```
Liczba z dwoma miejscami po przecinku: 5.00
```

#### CIEKAWOSTKI HISTORYCZNE

Alternatywny, 'stary', zapis powyższych przykładów:

```python
print("Liczba na dziewięciu pozycjach: {:9d}".format(x))
print("Liczba na trzech pozycjach uzupełniona zerami {:03d}".format(x))
print("Liczba z dwoma miejscami po przecinku: {:.2f}".format(x))
```

Alternatywny, 'jeszcze starszy', zapis powyższych przykładów:

```python
print("Liczba na dziewięciu pozycjach: %9d" % x)
print("Liczba na trzech pozycjach uzupełniona zerami %03d" % x)
print("Liczba z dwoma miejscami po przecinku: %.2f" % x)
```

### 🇬🇧 Task description (EN)

Write a program that prints a 10x10 multiplication table in the following form:

```
   |  1  2  3  4  5  6  7  8  9 10
---------------------------------
 1 |  1  2  3  4  5  6  7  8  9 10
 2 |  2  4  6  8 10 12 14 16 18 20
 3 |  3  6  9 12 15 18 21 24 27 30
etc.
```

The numbers should be in columns, right-aligned. In the simplified version you may skip the "decorations" (the lines and the column/row numbers). How to achieve this alignment is described below, in the section on output formatting.

**NOTE:** To print numbers with several `print` calls on one line, set the additional `end` parameter of the `print` function:

For example:

```python
print(5, end="")
print(6, end="")
```

prints:

```
56
```

#### Output formatting in Python

Suppose we want to print a 1-digit number on 9 positions (i.e. prepend 8 spaces to it). This can be done with output formatting.

Python has several ways of formatting output (e.g. how numbers are printed to the screen). Since Python 3.6 there are f-strings. In this approach the letter `f` is put before the string passed to `print`, and the variables which we used to put after commas are inserted into that string, surrounded by `{}` braces (i.e. instead of `print("The radius of the circle is", r, "cm")` we write `print(f"The radius of the circle is {r} cm")`).

This notation lets you add formatting information. Printing the variable `x` (holding e.g. the value 5) on 9 positions would look like this:

```python
print(f"Number on nine positions: {x:9}")
```

which prints:

```
Number on nine positions:         5
```

Other examples:

```python
print(f"Number on three positions padded with zeros {x:03}")
```

prints:

```
Number on three positions padded with zeros: 005
```

```python
print(f"Number with two decimal places: {x:.2f}")
```

prints:

```
Number with two decimal places: 5.00
```

#### HISTORICAL TRIVIA

An alternative, 'old' way of writing the examples above:

```python
print("Number on nine positions: {:9d}".format(x))
print("Number on three positions padded with zeros {:03d}".format(x))
print("Number with two decimal places: {:.2f}".format(x))
```

An alternative, 'even older' way of writing the examples above:

```python
print("Number on nine positions: %9d" % x)
print("Number on three positions padded with zeros %03d" % x)
print("Number with two decimal places: %.2f" % x)
```

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - full version with header row, separator line and row numbers; numbers right-aligned with f-string width. |

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
    |   1   2   3   4   5   6   7   8   9  10
---------------------------------------------
  1 |   1   2   3   4   5   6   7   8   9  10
  2 |   2   4   6   8  10  12  14  16  18  20
  3 |   3   6   9  12  15  18  21  24  27  30
  4 |   4   8  12  16  20  24  28  32  36  40
  5 |   5  10  15  20  25  30  35  40  45  50
  6 |   6  12  18  24  30  36  42  48  54  60
  7 |   7  14  21  28  35  42  49  56  63  70
  8 |   8  16  24  32  40  48  56  64  72  80
  9 |   9  18  27  36  45  54  63  72  81  90
 10 |  10  20  30  40  50  60  70  80  90 100
```
