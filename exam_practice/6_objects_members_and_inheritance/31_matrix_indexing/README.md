# Exercise 31 — Matrix with C, Pascal and Matlab Indexing

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 31 — Matrix with C, Pascal and Matlab Indexing](../../../class_exercises/6_objects_members_and_inheritance/31_matrix_indexing/) by Piotr Pawlik
> Date: 2026-11-25

## Task

### 🇵🇱 Treść zadania (PL)

Zaimplementuj w języku Python tablicę dwuwymiarową (macierz), do której odczyt będzie można zrealizować jak w języku C, czyli:
`nazwa_tablicy[nr_wiersza][nr_kolumny]`, jak w Pascalu, czyli: `nazwa_tablicy[nr_wiersza, nr_kolumny]` oraz jak w Matlabie, czyli: `nazwa_tablicy(nr_wiersza, nr_kolumny)`. Zapis niech będzie możliwy tylko tak jak w C.
Wykorzystaj w tym celu klasę z metodami `__setitem__`, `__getitem__` i `__call__`
W metodzie `__getitem__` przydatna będzie funkcja isinstance, która ma dwa parametry i sprawdza czy pierwszy argument jest typu podanego jako drugi argument (np. : `isinstance(x, int)`). Wynikiem będzie True lub False.

Dodatkowo proszę zapewnić możliwość wypisania macierzy przez funkcję print poprzez zdefiniowanie metody `__str__` (sposób wypisania jest podany w przykładzie poniżej)

Sama macierz może być reprezentowana w postaci listy list, przy czym pole wewnętrznie reprezentujące macierz (czyli ta lista list) ma nie być dostępne spoza klasy. Niech zatem ta lista list nazywa się `__matrix`
Należy zaimplementować 'konstruktor', który stworzy macierz (obiekt tworzonej klasy) na dwa sposoby:
albo otrzyma on jako argument krotkę zawierającą oba rozmiary macierzy
albo otrzyma wprost listę list wypełnioną wartościami.
Można wykorzystać isinstance do sprawdzenia czy argument jest typu tuple, a przeciwnym wypadku założyć, że 'konstruktor' otrzymał w argumencie poprawną listę list.
Niech 'konstruktor' posiada także parametr, z wartością domyślną równą 0, wykorzystywany do wypełniania macierzy, kiedy macierz jest tworzona przez podanie jej rozmiarów.

Przykładowy kod tworzący macierz (przyjąwszy, że klasa nazywa się macierz):

```python
m1 = macierz(
[ [2, -1],
  [0,  4],
  [3,  1] ]
)
print(m1)
```

Wynikiem wypisania m1 powinno być:

```
| 2  -1 |
| 0   4 |
| 3   1 |
```

W main-ie sprawdź działanie zaimplementowanej klasy przez stworzenie trzech macierzy:
pierwszej:

```
| 2  -1 |
| 0   4 |
| 3   1 |
```

poprzez podanie jej listy list oraz drugiej:

```
| 2   2 |
| 2   2 |
| 2   2 |
```

i trzeciej:

```
| 0   0 |
| 0   0 |
| 0   0 |
```

przez podanie rozmiarów macierzy i wartości wypełniających.

Do trzeciej macierzy wpisz wynik odejmowania drugiej macierzy od pierwszej (pierwsza - druga). W obliczeniach użyj pętli for z range. Dostęp do elementów pierwszej macierzy zrealizuj jak w Matlabie a drugiej jak w Pascalu.

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
[ [2, -1],
  [0,  4],
  [3,  1] ]
)
print(m1)
```

Printing m1 should give:

```
| 2  -1 |
| 0   4 |
| 3   1 |
```

In `main`, test the implemented class by creating three matrices:
the first one:

```
| 2  -1 |
| 0   4 |
| 3   1 |
```

by giving its list of lists, and the second one:

```
| 2   2 |
| 2   2 |
| 2   2 |
```

and the third one:

```
| 0   0 |
| 0   0 |
| 0   0 |
```

by giving the sizes of the matrix and the fill value.

Write the result of subtracting the second matrix from the first one (first - second) into the third one. Use a `for` loop with `range` in the computation. Access the elements of the first matrix like in Matlab and of the second one like in Pascal.

Print the third matrix (with `print`).

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
