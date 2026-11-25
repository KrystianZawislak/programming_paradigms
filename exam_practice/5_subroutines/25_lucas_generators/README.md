# Exercise 25 — Lucas Sequence Generators

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 25 — Fibonacci Generators](../../../class_exercises/5_subroutines/25_fibonacci_generators/) by Piotr Pawlik
> Date: 2026-11-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz dwa generatory zwracające kolejne wartości ciągu Lucasa (ciąg Lucasa, tak jak ciąg Fibonacciego, ma tę właściwość, że kolejny jego element jest sumą dwóch poprzednich - ale wartość pierwszego wyrazu wynosi 2, a drugiego 1. Trzeci wyraz ma wtedy wartość 3, czwarty 4, piąty 7, szósty 11 itd).

Pierwszy generator niech otrzymuje jako argument ile wyrazów ma wygenerować. Drugi niech będzie generatorem nieskończonym (z pętlą while True).

W main najpierw wypisz wartości 10 pierwszych wyrazów ciągu Lucasa z użyciem pierwszego generatora.

Następnie wypisz te same 10 wyrazów używając drugiego generatora, a potem w następnej pętli wypisz te z 10 następnych wyrazów, które są podzielne przez 3 oraz w kolejnej pętli parzyste spośród następnych 10-ciu (czyli od pierwszego do dziesiątego - wszystkie, od jedenastego do dwudziestego podzielne przez 3 a od dwudziestego pierwszego do trzydziestego parzyste).

### 🇬🇧 Task description (EN)

Write two generators returning consecutive values of the Lucas sequence (the Lucas sequence, like the Fibonacci sequence, has the property that each next element is the sum of the two previous ones - but the first term is 2 and the second is 1. The third term is then 3, the fourth 4, the fifth 7, the sixth 11, etc.).

Let the first generator take as an argument how many terms it should generate. Let the second one be an infinite generator (with a `while True` loop).

In `main`, first print the values of the first 10 terms of the Lucas sequence using the first generator.

Then print the same 10 terms using the second generator, and then in the next loop print those of the next 10 terms that are divisible by 3, and in another loop the even ones among the following 10 (i.e. from the first to the tenth - all of them, from the eleventh to the twentieth - divisible by 3, and from the twenty-first to the thirtieth - even).

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
