# Exercise 1 — Upside-Down Trees (`goto`)

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 1](../../class_exercises/ex1/) (Unstructured Christmas Trees (`goto`)) by Piotr Pawlik
> Date: 2026-11-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz w języku C program rysujący "odwrócone choinki" jak poniżej:

```
*********
 *******
  *****
   ***
    *
```

Liczba poziomów powinna być pobierana z klawiatury. Choinka, której liczba poziomów jest podzielna przez 3, powinna zostać "wyrysowana" znakami @, a pozostałe - plusami (+).

Po wyrysowaniu choinki program ma ponownie pobrać liczbę poziomów i wyrysować nową choinkę. Rysowanie choinek ma być powtarzane wielokrotnie aż do wyrysowania choinki o wysokości 5.

**UWAGA:** Program należy napisać NIESTRUKTURALNIE - to znaczy nie wolno używać "struktur sterujących" - pętli, else, sekwencji (czyli nie można użyć wyrażeń przecinkowych ani nawiasów { oraz } poza rozpoczynającym i kończącym maina - innymi słowy w programie może wystąpić tylko jedna para nawiasów {}).
Za to można (a nawet trzeba) używać goto.

### 🇬🇧 Task description (EN)

Write a C program that draws "upside-down Christmas trees" like the one below:

```
*********
 *******
  *****
   ***
    *
```

The number of levels should be read from the keyboard. A tree whose number of levels is divisible by 3 should be "drawn" with @ characters, and the others - with pluses (+).

After drawing a tree, the program should read the number of levels again and draw a new tree. Drawing trees should be repeated many times until a tree of height 5 is drawn.

**NOTE:** The program must be written in an UNSTRUCTURED way - i.e. you must not use "control structures" - loops, else, sequences (so you cannot use comma expressions or the { and } brackets other than those opening and closing `main` - in other words, only one pair of {} brackets may appear in the program).
Instead, you can (and even have to) use goto.

## Files

| File | Description |
| ---- | ----------- |
| `main.c` | Solution - not written yet. |

## How to run

macOS / Linux:

```bash
cc main.c -o ex1
./ex1
```

Windows (MinGW):

```powershell
gcc main.c -o ex1.exe
.\ex1.exe
```
