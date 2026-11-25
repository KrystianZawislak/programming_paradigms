# Exercise 14 — Roman Numerals to Integers

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 14 — Roman Numerals to Integers](../../../class_exercises/3_collections/14_roman_numerals/) by Piotr Pawlik
> Date: 2026-11-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz program, który zamieni napis zawierający liczbę rzymską na liczbę całkowitą.

Stwórz dwa słowniki. Jeden zamieniający pojedyncze 'cyfry rzymskie' na wartości 'arabskie', a drugi robiące to samo dla 'dwuznaków', czyli IV, IX, XL, XC itd.

Zaimplementuj algorytm:

W pętli while, używając indeksu, weź dwie kolejne litery napisu (wycięciem - ang. slicing, czyli z użyciem [ : ]) i sprawdź czy wynik wycięcia należy do słownika 'dwuznaków'. Jeżeli tak to dodaj do sumy wartość z tego słownika i zwiększ indeks o 2. Jeżeli nie to dodaj do sumy wartość słownika pojedynczych 'cyfr rzymskich' dla pierwszego ze znaków 'dwuznaku' i zwiększ indeks o 1. Pętla powinna zatrzymać się na przedostatnim znaku, wartość odpowiadająca ostatniemu znakowi ma być dodana po pętli (to już na pewno nie jest 'dwuznak'). Proszę przy odwoływaniu się do ostatniego znaku nie korzystać z długości napisu ani z indeksu używanego w pętli.

Wypisz sumę, czyli wartość 'arabską'. Sprawdź program dla liczb MCMXCIV (1994), CDXLIV (444) oraz MMXXVI (2026).

### 🇬🇧 Task description (EN)

Write a program that converts a string containing a Roman numeral into an integer.

Create two dictionaries. One converting single 'Roman digits' into 'Arabic' values, and the other doing the same for 'digraphs', i.e. IV, IX, XL, XC, etc.

Implement the algorithm:

In a `while` loop, using an index, take two consecutive letters of the string (by slicing, i.e. with [ : ]) and check whether the slice belongs to the 'digraph' dictionary. If so, add the value from this dictionary to the sum and increase the index by 2. If not, add the value of the single 'Roman digit' dictionary for the first character of the 'digraph' and increase the index by 1. The loop should stop at the penultimate character; the value of the last character should be added after the loop (it is certainly not a 'digraph'). When accessing the last character, do not use the length of the string or the index used in the loop.

Print the sum, i.e. the 'Arabic' value. Test the program with MCMXCIV (1994), CDXLIV (444) and MMXXVI (2026).

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
