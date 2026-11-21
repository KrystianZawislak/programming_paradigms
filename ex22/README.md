# Exercise 22 — String Decorator (upper)

> Course: Programming Paradigms
> Task author: Piotr Pawlik
> Date: 2026-11-04

## Task

### 🇵🇱 Treść zadania (PL)

W tym ćwiczeniu powstanie dekorator funkcji zwracajacych napis.

Na potrzeby przetestowania dekoratora potrzebujemy dwóch takich funkcji. Pierwsza niech będzie przerobionym zadaniem "Cyfry słownie" z tematu 3 - proszę napisać funkcję otrzymującą napis z liczbą i zwracającą napis z liczbą słownie. Druga niech będzie przerobionym zadaniem "drukuj" tylko zamiast wypisywać na ekran niech funkcja zwraca stworzony napis.

Wywołaj obie funkcje w main, pierwszą z napisem "1410" a drugą z napisami "Ala", "ma", "kota" rozdzielonymi znakiem (separatorem) '-'. Sprawdź wynik działania programu.

Napisz dekorator zamieniający wszystkie litery napisu zwracanego przez funkcję na wielkie (robi to metoda upper zawołana dla obiektu będącego napisem, np. `napis.upper()`)

**UWAGA** - od tego momentu main ani obie funkcje już nie mają być zmieniane - nic tu nie dodajemy ani nie usuwamy.

'Udekoruj' pierwszą funkcję za pomocą notacji z @. Zauważ jak zmieni się wynik działania programu.

'Udekoruj' drugą funkcję za pomocą notacji bez @ (poprzez 'ręczne' uruchomienie dekoratora po definicji dekorowanej funkcji). Zauważ jak zmieni się wynik działania programu.

### 🇬🇧 Task description (EN)

In this exercise we will create a decorator for functions that return a string.

To test the decorator we need two such functions. Let the first one be a reworked "Digits to Words" exercise ([ex13](../ex13/)) - write a function that takes a string with a number and returns a string with the number in words. Let the second one be a reworked "drukuj" exercise ([ex20](../ex20/)), but instead of printing to the screen, the function should return the created string.

Call both functions in `main`, the first one with the string "1410" and the second one with the strings "Ala", "ma", "kota" separated by the character (separator) '-'. Check the result of the program.

Write a decorator that converts all letters of the string returned by a function to uppercase (this is done by the `upper` method called on a string object, e.g. `string.upper()`).

**NOTE** - from this point on, neither `main` nor the two functions may be changed - we don't add or remove anything there.

'Decorate' the first function using the @ notation. Notice how the result of the program changes.

'Decorate' the second function without the @ notation (by 'manually' calling the decorator after the definition of the decorated function). Notice how the result of the program changes.

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - `to_upper` decorator (a `wrapper` calling the function and returning `result.upper()`); `numbers_in_words` decorated with `@to_upper`, `drukuj` decorated manually with `drukuj = to_upper(drukuj)`. |

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
ONE FOUR ONE ZERO 
ALA-MA-KOTA
```
