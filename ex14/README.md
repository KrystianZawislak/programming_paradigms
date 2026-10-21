# Exercise 14 — Roman Numerals to Integers

> Course: Programming Paradigms
> Date: 2026-10-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program, który zamieni napis zawierający liczbę rzymską na liczbę całkowitą.

Stwórz dwa słowniki. Jeden zamieniający pojedyncze 'cyfry rzymskie' na wartości 'arabskie', a drugi robiące to samo dla 'dwuznaków', czyli IV, IX, XL, XC itd.

Zaimplementuj algorytm:

W pętli while, używając indeksu, weź dwie kolejne litery napisu (wycięciem - ang. slicing, czyli z użyciem [ : ]) i sprawdź czy wynik wycięcia należy do słownika 'dwuznaków'. Jeżeli tak to dodaj do sumy wartość z tego słownika i zwiększ indeks o 2. Jeżeli nie to dodaj do sumy wartość słownika pojedynczych 'cyfr rzymskich' dla pierwszgo ze znaków 'dwuznaku' i zwiększ indeks o 1. Pętla powinna zatrzymać się na przedostatnim znaku, wartość odpowiadająca ostatniemu znakowi ma być dodana po pętli (to już na pewno nie jest 'dwuznak'). Proszę przy odwoływaniu się do ostatniego znaku nie korzystać z długości napisu ani z indeksu używanego w pętli.

Wypisz sumę, czyli wartość 'arabską'.

### 🇬🇧 Task description (EN)

Write a program that converts a string containing a Roman numeral into an integer.

Create two dictionaries. One converting single 'Roman digits' into 'Arabic' values, and the other doing the same for 'digraphs', i.e. IV, IX, XL, XC, etc.

Implement the algorithm:

In a `while` loop, using an index, take two consecutive letters of the string (by slicing, i.e. with `[ : ]`) and check whether the slice is in the 'digraphs' dictionary. If it is, add the value from that dictionary to the sum and increase the index by 2. If not, add the value from the single 'Roman digits' dictionary for the first character of the 'digraph' and increase the index by 1. The loop should stop at the second-to-last character; the value of the last character is to be added after the loop (it certainly is not a 'digraph' anymore). When referring to the last character, do not use the length of the string or the index used in the loop.

Print the sum, i.e. the 'Arabic' value.

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - two dictionaries (single Roman digits and digraphs), `while` loop over two-letter slices, the last character added after the loop with `roman_numeral[-1]`, unless the last two characters (`roman_numeral[-2:]`) form a digraph already counted in the loop. |

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
MMXXVI
2026
```

```
LVIII
58
```

```
MCMXCIV
1994
```
