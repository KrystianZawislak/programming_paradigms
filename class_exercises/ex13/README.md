# Exercise 13 — Digits to Words (dictionary)

> Course: Programming Paradigms
> Task author: Piotr Pawlik
> Date: 2026-10-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program, który zamieni napis zawierający ciąg cyfr (czyli liczbę ale zapisaną jako string) na napis 'słowny' (np. '1410' na 'jeden cztery jeden zero '). Znaki inne niż cyfry należy pomijać. Należy wykorzystać słownik zawierający liczebniki ('zero', 'jeden', itd). Odwołania do słownika proszę robić odwołania jak do tablicy (nawiasami [ ] ) a nie metodą get.

Program na koniec ma wypisać stworzony napis (nie listę).

Proszę nie używać isdigit

Przydatne:
- `""` lub `''` - pusty napis (np. `napis = ""`)
- `in` - operator który zwraca wartość logiczną czy element znajduje się w liście, krotce, itd. (np. `if element in lista`)

### 🇬🇧 Task description (EN)

Write a program that converts a string containing a sequence of digits (i.e. a number, but written as a string) into a 'worded' string (e.g. '1410' into 'one four one zero '). Characters other than digits should be skipped. Use a dictionary containing the numerals ('zero', 'one', etc.). Access the dictionary like an array (with `[ ]` brackets), not with the `get` method.

At the end, the program should print the created string (not a list).

Please do not use `isdigit`.

Useful:
- `""` or `''` - an empty string (e.g. `string = ""`)
- `in` - an operator that returns a boolean telling whether an element is in a list, tuple, etc. (e.g. `if element in list`)

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - for each character checks with `in` whether it is a key of the `digits` dictionary and appends its word (`digits[char]`) to the result string. |

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
1410
one four one zero
```

```
12a3-4
one two three four
```
