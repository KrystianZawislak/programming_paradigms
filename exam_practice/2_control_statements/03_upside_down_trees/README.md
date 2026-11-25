# Exercise 3 — Upside-Down Trees in Python

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 3 — Christmas Trees in Python](../../../class_exercises/2_control_statements/03_christmas_trees/) by Piotr Pawlik
> Date: 2026-11-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program w Pythonie rysujący "odwróconą choinkę" jak poniżej.

```
*********
 *******
  *****
   ***
    *
```

Liczba poziomów powinna być pobierana z klawiatury. Choinka, której liczba poziomów jest podzielna przez 3, powinna zostać "wyrysowana" znakami @, a pozostałe - plusami (+).

Po wyrysowaniu choinki program ma ponownie pobrać liczbę poziomów i wyrysować nową choinkę. Rysowanie choinek ma być powtarzane wielokrotnie (w pętli while) aż do wyrysowania choinki o wysokości 5 (choinka o tej wysokości też ma zostać wyrysowana).
Rysowanie pojedynczej choinki powinno być zawarte w jednej pętli for (z użyciem range oraz 'mnożenia liczby przez napis').

### 🇬🇧 Task description (EN)

Write a Python program that draws an "upside-down Christmas tree" like the one below.

```
*********
 *******
  *****
   ***
    *
```

The number of levels should be read from the keyboard. A tree whose number of levels is divisible by 3 should be "drawn" with @ characters, and the others - with pluses (+).

After drawing a tree, the program should read the number of levels again and draw a new tree. Drawing trees should be repeated many times (in a `while` loop) until a tree of height 5 is drawn (the tree of this height should be drawn too).
Drawing a single tree should be done in one `for` loop (using `range` and 'multiplying a number by a string').

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
