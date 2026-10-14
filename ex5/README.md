# Exercise 5 — Indexes of 'a' and 'A'

> Course: Programming Paradigms
> Date: 2026-10-14

## Task

### 🇵🇱 Treść zadania (PL)

Napisz drugą wersję programu z zadania 2, która zamiast zliczać litery 'A' i 'a' wypisze ich położenia (indeksy). Należy użyć pętli for BEZ range. Ponadto w programie nie może wystąpić żadne działanie arytmetyczne (dodawanie, odejmowanie ...) - podpowiedź: enumerate.

### 🇬🇧 Task description (EN)

Write a second version of the program from task 2 ([ex4](../ex4/)) which, instead of counting the letters 'A' and 'a', prints their positions (indexes). Use a `for` loop WITHOUT `range`. Moreover, no arithmetic operation (addition, subtraction, ...) may appear in the program - hint: `enumerate`.

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - `for` loop over `enumerate(string)`, prints the index and the letter of every 'a' / 'A'. |

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
Enter string: Ala ma kota, a Ania ma Asa
0 A
2 a
5 a
10 a
13 a
15 A
18 a
21 a
23 A
25 a
```
