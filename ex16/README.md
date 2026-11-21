# Exercise 16 — Letter Positions

> Course: Programming Paradigms
> Task author: Piotr Pawlik
> Date: 2026-10-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program, który w wejściowym napisie policzy ile razy występuje każda z liter i wskaże ich położenia (indeksy).

Dla każdej litery napisu przechodzimy po napisie zliczamy wystąpienia tej litery oraz wypisujemy ich indeksy. Na koniec wypisujemy w nawiasach liczbę znalezionych liter. Przykładowo dla napisu "Ala ma kota" program powinien wypisać:

```
A: 0 (1)
l: 1 (1)
a: 2 5 10 (3)
 : 3 6 (2)
m: 4 (1)
k: 7 (1)
o: 8 (1)
t: 9 (1)
```

W programie proszę użyć pętli for, ale nie używać range. Zamiast tego proszę użyć enumerate.

W programie proszę nie używać słownika. Zamiast tego proszę w jakiś sposób pomijać już sprawdzone litery (np. wykorzystać konwersję na zbiór lub utworzyć pusty napis do którego będą wpisywane litery już przeliczone, których kolejne wystąpienia należy pomijać).

### 🇬🇧 Task description (EN)

Write a program that counts how many times each letter occurs in the input string and shows their positions (indexes).

For each letter of the string we go over the string, count the occurrences of that letter and print their indexes. At the end we print the number of letters found in parentheses. For example, for the string "Ala ma kota" the program should print:

```
A: 0 (1)
l: 1 (1)
a: 2 5 10 (3)
 : 3 6 (2)
m: 4 (1)
k: 7 (1)
o: 8 (1)
t: 9 (1)
```

Use a `for` loop in the program, but do not use `range`. Use `enumerate` instead.

Do not use a dictionary in the program. Instead, skip the already checked letters somehow (e.g. by converting to a set, or by creating an empty string to which the already counted letters are added, so that their next occurrences are skipped).

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - converts the string to a `set` of unique characters, then for each of them goes over the string with `enumerate`, prints the indexes and the count. |

## How to run

macOS / Linux:

```bash
python3 main.py
```

Windows:

```powershell
py main.py
```

Example input/output (the order of the letters can differ between runs, because a `set` is unordered):

```
Ala ma kota
t: 9 (1)
m: 4 (1)
o: 8 (1)
a: 2  5  10 (3)
k: 7 (1)
l: 1 (1)
A: 0 (1)
 : 3  6 (2)
```
