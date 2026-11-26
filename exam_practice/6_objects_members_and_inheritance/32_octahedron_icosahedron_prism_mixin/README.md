# Exercise 32 — Octahedron, Icosahedron and Prism (mixin, multiple inheritance)

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 32 — Solids from Regular Shapes (mixin, multiple inheritance)](../../../class_exercises/6_objects_members_and_inheritance/32_solids_from_shapes_mixin/) by Piotr Pawlik
> Date: 2026-11-26

## Task

### 🇵🇱 Treść zadania (PL)

Skopiuj klasy figur z ćwiczenia 30 z zajęć (Kształt, Koło, Trójkąt, Prostokąt, Kwadrat, Trójkąt równoboczny) i uzupełnij figury foremne o atrybut liczba_boków (ustawiany w konstruktorze).

Wykorzystując uzupełnione klasy stworzymy klasy brył stworzonych z figur foremnych: ośmiościan, dwudziestościan i graniastosłup trójkątny foremny (wszystkie krawędzie równe - dwie podstawy to trójkąty równoboczne, a ściany boczne to kwadraty). Będą one dziedziczyć po klasie Bryła, opisanej poniżej. W konstruktorze każdej z tych klas utwórz listę ścian - figur tworzących ściany tych brył. Parametrem konstruktora (oprócz nazwy) niech będzie bok ściany (figury są foremne, więc wszystkie będą miały taką samą długość swoich boków).

Stwórz nadrzędną klasę dla tych trzech klas (o nazwie Bryła) dziedziczącą od klasy Kształt - dzięki temu bryły odziedziczą pole nazwa. Klasa dziedzicząca po Kształt musi mieć metodę pole. W wypadku brył polem jest suma pól wszystkich ścian. Dlatego klasa Bryła powinna przechowywać listę ścian przekazanych jej przez konstruktory klas pochodnych i korzystając z tej listy wyliczać pole. Aby to było możliwe niech klasa Bryła posiada metodę abstrakcyjną ściany, która w bryłach pochodnych będzie zwracała listę utworzonych w nich ścian.

Będziemy do brył chcieli dodać metodę podającą ich liczbę wierzchołków. Ośmiościan (8 trójkątów) i dwudziestościan (20 trójkątów) są bryłami platońskimi, więc liczbę wierzchołków można wyliczyć na podstawie liczby ścian i liczby boków ściany wg wzoru:

liczba_wierzchołków = 2 - liczba_ścian + liczba_ścian * liczba_boków_ściany / 2

Nie twórz dla nich dodatkowej nadklasy dziedziczącej z Bryła - zamiast tego utwórz mixin, czyli prostą klasę Platon bez konstruktora, która zawiera tylko metodę wierzchołki zwracającą liczbę wierzchołków korzystając z powyższego wzoru. Ośmiościan i dwudziestościan mają dziedziczyć po dwóch klasach (Bryła i Platon).

Graniastosłup nie jest bryłą platońską (ma ściany różnego rodzaju), więc musi mieć własną metodę wierzchołki, która po prostu zwróci wartość 6.

W main należy stworzyć listę zawierającą ośmiościan o boku 2, dwudziestościan o boku 1 i graniastosłup o boku 3, a następnie w pętli wypisać nazwy brył oraz ich pola i liczbę wierzchołków.

### 🇬🇧 Task description (EN)

Copy the shape classes from class exercise 30 (Shape, Circle, Triangle, Rectangle, Square, Equilateral triangle) and extend the regular shapes with a `number_of_sides` attribute (set in the constructor).

Using the extended classes, we will create classes of solids built from regular shapes: an octahedron, an icosahedron and a regular triangular prism (all edges equal - the two bases are equilateral triangles and the side faces are squares). They will inherit from the Solid class described below. In the constructor of each of these classes, create a list of faces - the shapes that form the faces of the solid. The constructor parameter (besides the name) should be the side of a face (the shapes are regular, so all of them will have the same side length).

Create a parent class for these three classes (called Solid) that inherits from the Shape class - thanks to this, the solids will inherit the name field. A class inheriting from Shape must have an `area` method. For solids, the area is the sum of the areas of all faces. That is why the Solid class should store the list of faces passed to it by the constructors of the derived classes and use this list to compute the area. To make this possible, let the Solid class have an abstract method `faces`, which in the derived solids will return the list of faces created in them.

We will want to add a method to the solids that gives their number of vertices. The octahedron (8 triangles) and the icosahedron (20 triangles) are Platonic solids, so their number of vertices can be computed from the number of faces and the number of sides of a face with the formula:

number_of_vertices = 2 - number_of_faces + number_of_faces * number_of_sides_of_a_face / 2

Do not create an extra parent class for them inheriting from Solid - instead, create a mixin, i.e. a simple Plato class without a constructor, which contains only the `vertices` method returning the number of vertices using the formula above. The octahedron and the icosahedron should inherit from two classes (Solid and Plato).

The prism is not a Platonic solid (it has faces of different kinds), so it must have its own `vertices` method, which simply returns the value 6.

In `main`, create a list containing an octahedron with side 2, an icosahedron with side 1 and a prism with side 3, and then in a loop print the names of the solids, their areas and their numbers of vertices.

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
