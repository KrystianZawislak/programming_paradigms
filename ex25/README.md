# Exercise 25 — Fibonacci Generators

> Course: Programming Paradigms
> Date: 2026-11-18

## Task

### 🇵🇱 Treść zadania (PL)

Napisz dwa generatory zwracający kolejne wartości ciągu Fibonacciego (ciąg Fibonacciego ma tę włąściwość, że kolejny jego element jest sumą dwóch poprzednich - przyjmijmy, że wartość pierwszego i drugiego wyrazu wynosi 1. Trzeci wyraz ma wtedy wartość 2, czwarty 3, piąty 5, szósty 8 itd).

Pierwszy generator niech otrzymuje jako argument ile wyrazów ma wygenerować. Drugi niech będzie generatorem nieskończonym (z pętlą while True 🙂)

W main najpierw wypisz wartości 10 pierwszych wyrazów ciągu Fibonacciego z użyciem pierwwszego generatora.

Następnie wypisz te same 10 wyrazów używając drugiego generatora, a potem w następnej pętli wypisz te z 10 następnych wyrazów, które są podzielnie podzienle przez 3 oraz w kolejnej pętli podzielne przez 5 spośród następnych 10-ciu (czyli od pierwszego do dziesiątego -wszystkie, od jedenastego do dwudziestego podzielne przez 3 a od dwudziestego pierwszego do trzydziestego podzielne przez 5).

### 🇬🇧 Task description (EN)

Write two generators returning consecutive values of the Fibonacci sequence (the Fibonacci sequence has the property that each next element is the sum of the two previous ones - let's assume that the first and the second term are both 1. The third term is then 2, the fourth 3, the fifth 5, the sixth 8, etc.).

Let the first generator take as an argument how many terms it should generate. Let the second one be an infinite generator (with a `while True` loop 🙂).

In `main`, first print the values of the first 10 terms of the Fibonacci sequence using the first generator.

Then print the same 10 terms using the second generator, and then in the next loop print those of the next 10 terms that are divisible by 3, and in another loop those of the following 10 that are divisible by 5 (i.e. from the first to the tenth - all of them, from the eleventh to the twentieth - divisible by 3, and from the twenty-first to the thirtieth - divisible by 5).

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - `fibonacci_until(how_many)` yields the given number of terms, `fibonacci_inf()` yields terms forever (`while True`); `main` keeps one `fibonacci_inf` generator and continues it across three loops (terms 1-10, 11-20, 21-30). |

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
1
1
2
3
5
8
13
21
34
55
------------
1
1
2
3
5
8
13
21
34
55
------------
144
987
6765
------------
75025
832040
------------
```
