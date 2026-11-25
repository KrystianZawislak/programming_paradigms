# Exercise 22 — String Decorator (spaces to underscores)

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 22 — String Decorator (upper)](../../../class_exercises/4_functions/22_upper_decorator/) by Piotr Pawlik
> Date: 2026-11-21

## Task

### 🇵🇱 Treść zadania (PL)

W tym ćwiczeniu powstanie dekorator funkcji zwracających napis.

Na potrzeby przetestowania dekoratora potrzebujemy dwóch takich funkcji. Pierwsza niech będzie przerobionym zadaniem "Cyfry słownie" (zadanie 13) - proszę napisać funkcję otrzymującą napis z liczbą i zwracającą napis z liczbą słownie. Druga niech będzie przerobionym zadaniem "wyswietl" (zadanie 20) tylko zamiast wypisywać na ekran niech funkcja zwraca stworzony napis.

Wywołaj obie funkcje w main, pierwszą z napisem "2026" a drugą z napisami "Paradygmaty", "programowania", "są", "super" rozdzielonymi domyślnym separatorem (spacją). Sprawdź wynik działania programu.

Napisz dekorator zamieniający wszystkie spacje w napisie zwracanym przez funkcję na podkreślenia (robi to metoda replace zawołana dla obiektu będącego napisem, np. `napis.replace(" ", "_")`)

**UWAGA** - od tego momentu main ani obie funkcje już nie mają być zmieniane - nic tu nie dodajemy ani nie usuwamy.

'Udekoruj' pierwszą funkcję za pomocą notacji z @. Zauważ jak zmieni się wynik działania programu.

'Udekoruj' drugą funkcję za pomocą notacji bez @ (poprzez 'ręczne' uruchomienie dekoratora po definicji dekorowanej funkcji). Zauważ jak zmieni się wynik działania programu.

### 🇬🇧 Task description (EN)

In this exercise we will create a decorator for functions that return a string.

To test the decorator we need two such functions. Let the first one be a reworked "Digits to Words" exercise ([ex13](../../3_collections/13_phone_number_to_words/)) - write a function that takes a string with a number and returns a string with the number in words. Let the second one be a reworked "wyswietl" exercise ([ex20](../20_custom_print_wyswietl/)), but instead of printing to the screen, the function should return the created string.

Call both functions in `main`, the first one with the string "2026" and the second one with the strings "Paradygmaty", "programowania", "są", "super" separated by the default separator (a space). Check the result of the program.

Write a decorator that replaces all spaces in the string returned by a function with underscores (this is done by the `replace` method called on a string object, e.g. `string.replace(" ", "_")`).

**NOTE** - from this point on, neither `main` nor the two functions may be changed - we don't add or remove anything there.

'Decorate' the first function using the @ notation. Notice how the result of the program changes.

'Decorate' the second function without the @ notation (by 'manually' calling the decorator after the definition of the decorated function). Notice how the result of the program changes.

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
