# Exercise 30 — Solids (abstract class, inheritance)

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 30 — Geometric Shapes (abstract class, inheritance)](../../../class_exercises/6_objects_members_and_inheritance/30_shapes_abstract_class/) by Piotr Pawlik
> Date: 2026-11-25

## Task

### 🇵🇱 Treść zadania (PL)

Napisz zestaw klas opisujących bryły geometryczne. Klasy powinny pochodzić od klasy nadrzędnej Bryła. Klasa Bryła ma być klasą abstrakcyjną i zawierać prywatny atrybut z nazwą bryły, dostępny poprzez getter (należy wykorzystać @property). Atrybut ten należy w `__init__` ustawić na nazwę "Bryła". Atrybut może być zmieniony za pomocą settera, ale setter nie ma zastępować starej nazwy nową lecz doklejać nową do starej (ze spacją pomiędzy nimi). Ponadto klasa Bryła ma zawierać abstrakcyjną metodę objętość.

Następnie należy stworzyć klasy pochodne od klasy Bryła:

- Kula(nazwa, promień)
- Prostopadłościan(nazwa, bok_a, bok_b, bok_c)
- Walec(nazwa, promień, wysokość)

Każda z brył ma umieć wyliczyć swoją objętość za pomocą metody objętość, a w `__init__` dokładać do atrybutu nazwa nazwę swojej klasy (poprzez setter).

W kolejnym kroku należy dla Prostopadłościanu i Walca utworzyć ich klasy pochodne opisujące ich wersje "foremne" (czyli sześcian oraz walec równoboczny - walec, którego wysokość jest równa średnicy podstawy). Mają one zawierać jedynie odpowiednie konstruktory (żadnych innych metod ani atrybutów).

W main należy stworzyć bryły:

Kulę o promieniu 2, prostopadłościan o bokach 2, 3 i 4, walec o promieniu 1 i wysokości 5, a następnie sześcian o boku 3 i walec równoboczny o promieniu 2.

Niech te ostatnie dwie bryły uzupełnią swoje nazwy o napisy "Sześcian" i "W. równoboczny"

Na koniec należy wszystkie utworzone obiekty umieścić w liście i w pętli wypisać z listy nazwy brył oraz ich objętości.

### 🇬🇧 Task description (EN)

Write a set of classes describing geometric solids. The classes should derive from the parent class Solid. The Solid class should be an abstract class and contain a private attribute with the name of the solid, accessible through a getter (use `@property`). In `__init__`, this attribute should be set to the name "Solid". The attribute can be changed with a setter, but the setter should not replace the old name with the new one - it should append the new one to the old one (with a space between them). Moreover, the Solid class should contain an abstract method `volume`.

Then create classes derived from Solid:

- Sphere(name, radius)
- Cuboid(name, side_a, side_b, side_c)
- Cylinder(name, radius, height)

Each solid should be able to compute its volume with the `volume` method, and in `__init__` append the name of its class to the name attribute (through the setter).

In the next step, create derived classes of Cuboid and Cylinder describing their "regular" versions (i.e. a cube and an equilateral cylinder - a cylinder whose height equals the diameter of its base). They should contain only the appropriate constructors (no other methods or attributes).

In `main`, create the solids:

a sphere with radius 2, a cuboid with sides 2, 3 and 4, a cylinder with radius 1 and height 5, and then a cube with side 3 and an equilateral cylinder with radius 2.

Let the last two solids extend their names with the strings "Cube" and "Equilateral cylinder".

Finally, put all the created objects in a list and in a loop print the names of the solids and their volumes from the list.

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
