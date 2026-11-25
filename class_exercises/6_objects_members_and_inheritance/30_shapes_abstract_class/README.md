# Exercise 30 — Geometric Shapes (abstract class, inheritance)

> Course: Programming Paradigms
> Task author: Piotr Pawlik
> Date: 2026-11-25

## Task

### 🇵🇱 Treść zadania (PL)

Napisz zestaw klas opisujących figury geometryczne. Klasy powinny pochodzić od klasy nadrzędnej Kształt. Klasa Kształt ma być klasą abstrakcyjną i zawierać prywatny atrybut z nazwą figury , dostępny poprzez getter (należy wykorzystać @property). Atrybut ten należy w `__init__` ustawić na nazwę "Kształt".  Atrybut może być zmieniony za pomocą settera, ale setter nie ma zastępować starej nazwy nową lecz doklejać nową do starej (ze spacją pomiędzy nimi). Ponadto klasa Kształt ma zawierać abstrakcyjną metodę pole.

Następnie należy stworzyć klasy pochodne od klasy Kształt:

- Koło(nazwa, promień)
- Trójkąt(nazwa, bok_a, bok_b, bok_c)
- Prostokąt(nazwa, bok_a, bok_b)

Każda z figur ma umieć wyliczyć swoje pole za pomocą metody pole, a w `__init__` dokładać do atrybutu nazwa nazwę swojej klasy (poprzez setter).

W kolejnym kroku należy dla Prostokąta i Trójkata utworzyć ich klasy pochodne opisujące ich wersje foremne (czyli kwadrat i trójkąt równoboczny). Mają one zawierać jedynie odpowiednie konstruktory (żadnych innych metod ani atrybutów).

W main należy stworzyć  figury:

Koło o promieniu 3, prostokąt o bokach 1 i 2, trójkąt o bokach 3, 4, 5 a następnie kwadrat o boku 6 i trójkąt foremny o boku 3.

Niech te ostatnie dwie figury uzupełnią swoje nazwy o napisy "Kwadrat" i "Tr. foremny"

Na koniec lależy wszystkie utworzone obiekty umieścić w liście w pętli wypisać z listy nazwy figur oraz ich pola.

### 🇬🇧 Task description (EN)

Write a set of classes describing geometric shapes. The classes should derive from the parent class Shape. The Shape class should be an abstract class and contain a private attribute with the name of the shape, accessible through a getter (use `@property`). In `__init__`, this attribute should be set to the name "Shape". The attribute can be changed with a setter, but the setter should not replace the old name with the new one - it should append the new one to the old one (with a space between them). Moreover, the Shape class should contain an abstract method `area`.

Then create classes derived from Shape:

- Circle(name, radius)
- Triangle(name, side_a, side_b, side_c)
- Rectangle(name, side_a, side_b)

Each shape should be able to compute its area with the `area` method, and in `__init__` append the name of its class to the name attribute (through the setter).

In the next step, create derived classes of Rectangle and Triangle describing their regular versions (i.e. a square and an equilateral triangle). They should contain only the appropriate constructors (no other methods or attributes).

In `main`, create the shapes:

a circle with radius 3, a rectangle with sides 1 and 2, a triangle with sides 3, 4, 5, and then a square with side 6 and a regular triangle with side 3.

Let the last two shapes extend their names with the strings "Square" and "Regular triangle".

Finally, put all the created objects in a list and in a loop print the names of the shapes and their areas from the list.

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - abstract `Shape(ABC)` with the private `__shape` name (set to "Shape" in `__init__`), a `shape` property whose setter appends the new name after a space, and the abstract method `area`; `Circle`, `Triangle` (Heron's formula) and `Rectangle` call `super().__init__()` and append their class name through the setter; `EquilateralTriangle` and `Square` only call the parent constructor with equal sides; `main` appends "Square" and "Equilateral" to the last two names and prints all names and areas in a loop. |

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
Shape Circle 28.274333882308138
Shape Rectangle 2
Shape Triangle 6.0
Shape Rectangle Square 36
Shape Triangle Equilateral 3.897114317029974
```
