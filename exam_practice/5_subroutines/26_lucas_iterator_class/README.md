# Exercise 26 — Lucas Iterator Class

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 26 — Fibonacci Iterator Class](../../../class_exercises/5_subroutines/26_fibonacci_iterator_class/) by Piotr Pawlik
> Date: 2026-11-21

## Task

### 🇵🇱 Treść zadania (PL)

Przerób zadanie z generatorem ciągu Lucasa (zadanie 25) tak, aby zdefiniować go jako klasę iteratora z metodami `__iter__` i `__next__`

Zaimplementuj jedną klasę która obejmie oba przypadki - generatora ze skończoną i nieskończoną liczbą generowanych wartości - utworzenie obiektu iteratora z parametrem niech tworzy generator 'skończony', a bez parametru - nieskończony (podpowiedź - init może mieć parametr z wartością domyślną).

Skopiuj main z poprzedniego ćwiczenia i uruchom go po ewentualnych małych zmianach.

### 🇬🇧 Task description (EN)

Rework the Lucas sequence generator exercise ([ex25](../25_lucas_generators/)) so that it is defined as an iterator class with the `__iter__` and `__next__` methods.

Implement one class that covers both cases - a generator with a finite and an infinite number of generated values - creating an iterator object with a parameter should create a 'finite' generator, and without a parameter - an infinite one (hint - `__init__` can have a parameter with a default value).

Copy `main` from the previous exercise and run it after possible small changes.

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
