# Exercise 26 — Fibonacci Iterator Class

> Course: Programming Paradigms
> Task author: Piotr Pawlik
> Date: 2026-11-18

## Task

### 🇵🇱 Treść zadania (PL)

Przerób zadanie z generatorem Fibonacciego tak, aby zdefiniować go jako klasę iteratora z metodami `__iter__` i `__next__`

Zaimplementuj jedną klasę która obejmie oba przypadki - generatora ze skończoną i nieskończoną liczbą generowanych wartości - utworzenie obiektu iteratora z parametrem niech tworzy generator 'skońskczony', a bez parametru - nieskończony (podpowiedź - init może mieć parametr z wartością domyślną).

Skopiuj main z poprzedniego ćwiczenia i uruchom go po ewentualnych małych zmianach.

### 🇬🇧 Task description (EN)

Rework the Fibonacci generator exercise ([ex25](../ex25/)) so that it is defined as an iterator class with the `__iter__` and `__next__` methods.

Implement one class that covers both cases - a generator with a finite and an infinite number of generated values - creating an iterator object with a parameter should create a 'finite' generator, and without a parameter - an infinite one (hint - `__init__` can have a parameter with a default value).

Copy `main` from the previous exercise and run it after possible small changes.

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - `Fibo_Iter(how_many=None)` iterator class: `__init__` stores the state (`how_many` becomes `float("inf")` when not given), `__iter__` returns `self`, `__next__` returns the current term and moves to the next one, raising `StopIteration` after `how_many` terms; `main` uses `Fibo_Iter(10)` in a `for` loop and one `Fibo_Iter()` object with `next()` for terms 1-10, 11-20 and 21-30. |

## How to run

macOS / Linux:

```bash
python3 main.py
```

Windows:

```powershell
py main.py
```

Example output (the same as in [ex25](../ex25/)):

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
