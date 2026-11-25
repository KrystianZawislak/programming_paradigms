# Exercise 16 — Letter Positions

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 16 — Letter Positions](../../../class_exercises/3_collections/16_letter_positions/) by Piotr Pawlik
> Date: 2026-11-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program, który w wejściowym napisie policzy ile razy występuje każda z liter i wskaże ich położenia (indeksy).

Dla każdej litery napisu przechodzimy po napisie zliczamy wystąpienia tej litery oraz wypisujemy ich indeksy. Na koniec wypisujemy w nawiasach liczbę znalezionych liter. Przykładowo dla napisu "Kasia ma psa" program powinien wypisać:

```
K: 0 (1)
a: 1 4 7 11 (4)
s: 2 10 (2)
i: 3 (1)
 : 5 8 (2)
m: 6 (1)
p: 9 (1)
```

W programie proszę użyć pętli for, ale nie używać range. Zamiast tego proszę użyć enumerate.

W programie proszę nie używać słownika. Zamiast tego proszę w jakiś sposób pomijać już sprawdzone litery (np. wykorzystać konwersję na zbiór lub utworzyć pusty napis do którego będą wpisywane litery już przeliczone, których kolejne wystąpienia należy pomijać).

### 🇬🇧 Task description (EN)

Write a program that counts how many times each letter occurs in the input string and shows their positions (indexes).

For each letter of the string, we go over the string, count the occurrences of this letter and print their indexes. At the end we print the number of letters found in parentheses. For example, for the string "Kasia ma psa" the program should print:

```
K: 0 (1)
a: 1 4 7 11 (4)
s: 2 10 (2)
i: 3 (1)
 : 5 8 (2)
m: 6 (1)
p: 9 (1)
```

Use a `for` loop in the program, but do not use `range`. Use `enumerate` instead.

Do not use a dictionary in the program. Instead, skip the already checked letters somehow (e.g. use conversion to a set, or create an empty string into which the already counted letters are added, whose further occurrences should be skipped).

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
