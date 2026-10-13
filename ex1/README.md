# Exercise 1 — Unstructured Christmas Trees (`goto`)

> Course: Programming Paradigms
> Date: 2026-10-13

## Task

### 🇵🇱 Treść zadania (PL)

Napisz w języku C program rysujący "choinki" jak poniżej:

```
     *
    ***
   *****
  *******
 *********
***********
```

Liczba poziomów powinna być pobierana z klawiatury. Choinka o parzystej liczbie poziomów powinna zostać "wyrysowana" gwiazdkami, a o nieparzystej - hashami (#).

Po wyrysowaniu choinki program ma ponownie pobrać liczbę poziomów i wyrysować nową choinkę. Rysowanie choinek ma być powtarzane wielokrotnie aż do wyrysowania choinki o wysokości 7.

**UWAGA:** Program należy napisać NIESTRUKTURALNIE - to znaczy nie wolno używać "struktur sterujących" - pętli, else, sekwencji (czyli nie można użyć wyrażeń przecinkowych ani nawiasów { oraz } poza rozpoczynającym i kończącym maina - innymi słowy w programie może wystąpić tylko jedna para nawiasów {}).
Za to można (a nawet trzeba) używać goto.

### 🇬🇧 Task description (EN)

Write a C program that draws "Christmas trees" like the one below:

```
     *
    ***
   *****
  *******
 *********
***********
```

The number of levels should be read from the keyboard. A tree with an even number of levels should be drawn with asterisks (`*`), and a tree with an odd number of levels with hashes (`#`).

After drawing a tree, the program should read the number of levels again and draw a new tree. Drawing trees should be repeated until a tree of height 7 has been drawn.

**NOTE:** The program must be written in an UNSTRUCTURED way - that is, you may not use "control structures": loops, `else`, or sequences (i.e. no comma expressions and no `{` / `}` braces other than the ones opening and closing `main` - in other words, only one pair of `{}` may appear in the program).
Instead, you may (and in fact must) use `goto`.

## Files

| File     | Description |
| -------- | ----------- |
| `main.c` | Solution written with `goto` only. |

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

Windows (Visual Studio Developer Command Prompt):

```bat
cl main.c
main.exe
```

Example input/output:

```
3
  #
 ###
#####
4
   *
  ***
 *****
*******
7
      #
     ###
    #####
   #######
  #########
 ###########
#############
```
