# Exercise 31 — Matrix with C, Pascal and Matlab Indexing

> Course: Programming Paradigms
> Task author: Piotr Pawlik
> Date: 2026-11-25

## Task

### 🇵🇱 Treść zadania (PL)

Zaimplementuj w języku Python tablicę dwuwymiarową (macierz), do której odczyt będzie można zrealizować jak w języku C, czyli:
`nazwa_tablicy[nr_wiersza][nr_kolumny]`, jak w Pascalu, czyli: `nazwa_tablicy[nr_wiersza, nr_kolumny]` oraz jak w Matlabie, czyli: `nazwa_tablicy(nr_wiersza, nr_kolumny)`. Zapis niech będzie możliwy tylko tak jak w C.
Wykorzystaj w tym celu klasę z metodami `__setitem__`, `__getitem__` i `__call__`
W metodzie `__getitem__` przydatna będzie funkcja isinstance, która ma dwa parametry i sprawdza czy pierwszy argument jest typu podanego jako drugi argument (np. : `isinstance(x, int)`). Wynikiem będzie True lub False.

Dodatkowo proszę zapewnić możliwość wypisania macierzy przez funkcję print poprzez zdefiniowanie metody `__str__` (sposób wypisania jest podany w przykładzie poniżej)

Sama macierz może być reprezentowana w postaci listy list, przy czym pole wewnętrznie reprezentujące macierz  (czyli ta lista list) ma nie być  dostępne spoza klasy. Niech zatem ta lista list nazywa się `__matrix`
Należy zaimplementować 'konstruktor', który stworzy macierz (obiekt tworzonej klasy) na dwa sposoby:
albo otrzyma on jako argument krotkę  zawierającą oba rozmiary macierzy
albo otrzyma wprost listę list wypełnioną wartościami.
Można wykorzystać  isinstance do sprawdzenia czy argument jest typu tuple, a przeciwnym wypadku założyć, że 'konstruktor' otrzymał w argumencie poprawną listę list.
Niech 'konstruktor' posiada także  parametr, z wrtością domyślną równą 0, wykorzystywany do wypełniania macierzy, kiedy macierz jest tworzona przez podanie jej rozmiarów.

Przykładowy kod tworzący macierz (przyjąwszy, że klasa nazywa się macierz):

```python
m1 = macierz(
[ [1, 0, 2],
  [-1, 3, 1] ]
)
print(m1)
```

Wynikiem wypisania m1 powinno być:

```
| 1   0   2 |
|-1   3   1 |
```

W main-ie sprawdz działanie zaimplementowanej klasy przez stworzenie trzech macierzy:
pierwszej:

```
| 1   0   2 |
|-1   3   1 |
```

poprzez podanie jej listy list oraz drugiej:

```
| 1   1   1 |
| 1   1   1 |
```

i trzeciej:

```
| 0   0   0 |
| 0   0   0 |
```

przez podanie rozmiarów macierzy i wartości wypełniających.

Do trzeciej macierzy wpisz wynik sumawania pierwszej i drugiej. W obliczeniach użyj pętli for z range. Dostęp do elementów pierwszej macierzy zrealizuj jak w Pascalu a drugiej jak w Matlabie.

Wypisz trzecią macierz (print-em).

### 🇬🇧 Task description (EN)

Implement in Python a two-dimensional array (a matrix) that can be read like in C, i.e.:
`array_name[row_no][column_no]`, like in Pascal, i.e.: `array_name[row_no, column_no]`, and like in Matlab, i.e.: `array_name(row_no, column_no)`. Writing should be possible only like in C.
Use a class with the methods `__setitem__`, `__getitem__` and `__call__` for this.
In the `__getitem__` method the `isinstance` function will be useful: it has two parameters and checks whether the first argument is of the type given as the second argument (e.g.: `isinstance(x, int)`). The result is True or False.

Additionally, make it possible to print the matrix with the `print` function by defining the `__str__` method (the printing format is given in the example below).

The matrix itself can be represented as a list of lists, but the field that internally represents the matrix (i.e. this list of lists) must not be accessible from outside the class. So let this list of lists be called `__matrix`.
Implement a 'constructor' that creates a matrix (an object of the class) in two ways:
either it receives as an argument a tuple containing both sizes of the matrix,
or it directly receives a list of lists filled with values.
You can use `isinstance` to check whether the argument is a tuple, and otherwise assume that the 'constructor' received a valid list of lists as its argument.
Let the 'constructor' also have a parameter with the default value 0, used to fill the matrix when it is created by giving its sizes.

Example code creating a matrix (assuming the class is called `macierz`, Polish for "matrix"):

```python
m1 = macierz(
[ [1, 0, 2],
  [-1, 3, 1] ]
)
print(m1)
```

Printing m1 should give:

```
| 1   0   2 |
|-1   3   1 |
```

In `main`, test the implemented class by creating three matrices:
the first one:

```
| 1   0   2 |
|-1   3   1 |
```

by giving its list of lists, and the second one:

```
| 1   1   1 |
| 1   1   1 |
```

and the third one:

```
| 0   0   0 |
| 0   0   0 |
```

by giving the sizes of the matrix and the fill value.

Write the sum of the first and the second matrix into the third one. Use a `for` loop with `range` in the computation. Access the elements of the first matrix like in Pascal and of the second one like in Matlab.

Print the third matrix (with `print`).

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - `Matrix` class with the private list of lists `__matrix`; the constructor takes either a `(rows, cols)` tuple plus a fill value (default 0) or a ready list of lists; `__getitem__` returns a whole row for an `int` key (so `m[i][j]` reads and writes like in C) and one element for a tuple key (Pascal); `__call__(row, col)` reads like in Matlab; `__setitem__` always raises `TypeError`, because a C-style write never reaches it; `__str__` prints the rows between `|` characters. `main` adds the first two matrices into the third one and prints all three. |

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
| 1 0 2 |
|-1 3 1 |

| 1 1 1 |
| 1 1 1 |

| 2 1 3 |
| 0 4 2 |

```
