# Exercise 32 — Solids from Regular Shapes (mixin, multiple inheritance)

> Course: Programming Paradigms
> Task author: Piotr Pawlik
> Date: 2026-11-26

## Task

### 🇵🇱 Treść zadania (PL)

Skopiuj klasy z poprzedniego ćwiczenia i uzupełnij figury foremne o atrybut liczba_boków (ustawiany w konstruktorze)

Wykorzystując uzupełnione klasy stworzymy klasy brył stworzonych z figur foremnych: czworościan, sześcian i 'piramida'. Będą one dziedziczyć po klasie Bryła, opisanej poniżej. W konstruktorze każdej z tych klas utwórz listę ścian - figur tworzących ściany tych brył. Parametrem konstruktora (oprócz nazwy) niech będzie bok ściany (figury są foremne, więc wszystkie będą miały taką samą długość swoich boków).

Stwórz nadrzędną klasę dla tych trzech klas (o nazwie Bryła) dziedziczącą od klasie Kształt - dzięki temu bryły odziedziczą pole nazwa. Klasa dziedzicząca po Kształt musi mieć metodę pole. W wypadku brył polem jest suma pól wszystkich ścian. Dlatego klasa Bryła powinna przechowywać listę ścian przekazanych jej przez konstruktory klas pochodnych i korzystając z tej listy wyliczać pole. Aby to było możliwe niech klasa Bryła posiada metodę abstrakcyjną ściany która w bryłach pochodnych będzie zwracała listę utworzonych w nich ścian.

Będziemy do brył chcieli dodać metodę podającą ich liczbę wierzchołków. Dla brył platońskich (my mamy tu tylko dwie: czworościan i sześcian) istnieje wzór pozwalający na wyliczenie liczby wierzchołków na podstawie liczby ścian i liczby krawędzi wg wzoru:

liczba_wierzchołków = 2 - liczba_ścian + liczba_ścian * liczba_boków_ściany / 2

Moglibyśmy stworzyć nadklasę dla czworościanu i sześcianu dziedziczącą z Bryła, ale to dodaje kolejny poziom w  hierarchii klas. Jeżeli chcielibyśmy tego uniknąć możemy stworzyć mixin czyli prostą klasę (nawet bez konstruktora) zawierającą tylko jedną lub kilka metod 'wstrzykiwanych' do innej klasy. W naszym wypadku 'wstrzykniemy' metodę wierzchołki (którą tu zdefiniujemy), a czworościan i sześcian będą dziedziczyły po dwóch klasach (Bryła i Platon - patrz poniżej). 

Natomiast piramida musi mieć własną metodę wierzchołki, która po prostu zwróci wartość 5.

Tak więc utwórz klasę Platon bez konstruktora, która zawiera tylko metodę wierzchołki zwracającą liczbę wierzchołków korzystając  z powyżej podanego wzoru.

W main należy stworzyć listę figur zawierającą przykładowe obiekty każdej z brył i w pętli wypisać nazwy brył oraz ich pola i liczbę wierzchołków.

### 🇬🇧 Task description (EN)

Copy the classes from the previous exercise (exercise 30) and extend the regular shapes with a `number_of_sides` attribute (set in the constructor).

Using the extended classes, we will create classes of solids built from regular shapes: a tetrahedron, a cube and a 'pyramid'. They will inherit from the Solid class described below. In the constructor of each of these classes, create a list of faces - the shapes that form the faces of the solid. The constructor parameter (besides the name) should be the side of a face (the shapes are regular, so all of them will have the same side length).

Create a parent class for these three classes (called Solid) that inherits from the Shape class - thanks to this, the solids will inherit the name field. A class inheriting from Shape must have an `area` method. For solids, the area is the sum of the areas of all faces. That is why the Solid class should store the list of faces passed to it by the constructors of the derived classes and use this list to compute the area. To make this possible, let the Solid class have an abstract method `faces`, which in the derived solids will return the list of faces created in them.

We will want to add a method to the solids that gives their number of vertices. For Platonic solids (we only have two here: the tetrahedron and the cube) there is a formula that computes the number of vertices from the number of faces and the number of edges:

number_of_vertices = 2 - number_of_faces + number_of_faces * number_of_sides_of_a_face / 2

We could create a parent class for the tetrahedron and the cube inheriting from Solid, but that adds another level to the class hierarchy. If we wanted to avoid this, we can create a mixin, i.e. a simple class (even without a constructor) containing only one or a few methods 'injected' into another class. In our case we will 'inject' the `vertices` method (which we will define here), and the tetrahedron and the cube will inherit from two classes (Solid and Plato - see below).

The pyramid, on the other hand, must have its own `vertices` method, which simply returns the value 5.

So create a Plato class without a constructor, which contains only the `vertices` method returning the number of vertices using the formula given above.

In `main`, create a list of shapes containing example objects of each of the solids, and in a loop print the names of the solids, their areas and their numbers of vertices.

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - the classes from exercise 30, with `EquilateralTriangle` and `Square` setting `sides` (3 and 4) in their constructors; abstract `GeometricSolid(Shape)` stores the list of faces it gets from the derived constructors, sums their areas in `area` and declares the abstract method `walls`; the `Plato` mixin (no constructor) has only `vertices`, computed from the formula using `walls()` and the number of sides of the first face; `Tetrahedron` (4 equilateral triangles) and `Cube` (6 squares) inherit from `GeometricSolid` and `Plato`, `Pyramid` (1 square + 4 equilateral triangles) inherits only from `GeometricSolid` and has its own `vertices` returning 5; `main` prints the name, area and number of vertices of each solid in a loop. |

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
Shape Tetrahedron 27.712812921102035 4
Shape Cube 54 8
Shape Pyramid 2.7320508075688767 5
```
