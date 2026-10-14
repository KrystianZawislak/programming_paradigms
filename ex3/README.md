# Exercise 3 — Christmas Trees in Python

> Course: Programming Paradigms
> Date: 2026-10-14

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program w Pythonie rysujący "choinkę" jak poniżej.

```
     *
    ***
   *****
  *******
 *********
***********
```

Liczba poziomów powinna być pobierana z klawiatury. Choinka o parzystej liczbie poziomów powinna zostać "wyrysowana" gwiazdkami, a o nieparzystej - hashami (#).

Po wyrysowaniu choinki program ma ponownie pobrać liczbę poziomów i wyrysować nową choinkę. Rysowanie choinek ma być powtarzane wielokrotnie (w pętli while) aż do wyrysowania choinki o wysokości 7 (choinka o tej wysokości też ma zostać wyrysowana).
Rysowanie pojedynczej choinki powinno być zawarte w jednej pętli for (z użyciem range oraz 'mnożenia liczby przez napis').

### 🇬🇧 Task description (EN)

Write a Python program that draws a "Christmas tree" like the one below.

```
     *
    ***
   *****
  *******
 *********
***********
```

The number of levels should be read from the keyboard. A tree with an even number of levels should be drawn with asterisks (`*`), and a tree with an odd number of levels with hashes (`#`).

After drawing a tree, the program should read the number of levels again and draw a new tree. Drawing trees should be repeated (in a `while` loop) until a tree of height 7 has been drawn (the tree of that height must be drawn too).
Drawing a single tree should be contained in one `for` loop (using `range` and "multiplying a number by a string").

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - `while` loop reading heights, one `for` loop with `range` and string multiplication per tree. |

## How to run

macOS / Linux:

```bash
python3 main.py
```

Windows:

```powershell
py main.py
```

Example input/output:

```
Conifer Height: 3
  #
 ###
#####
Conifer Height: 4
   *
  ***
 *****
*******
Conifer Height: 7
      #
     ###
    #####
   #######
  #########
 ###########
#############
```
