# Exercise 20 — Custom print Function (wyswietl)

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 20](../../class_exercises/ex20/) (Custom print Function (drukuj)) by Piotr Pawlik
> Date: 2026-11-21

## Task

### 🇵🇱 Treść zadania (PL)

Zabawimy się w twórcę języka Python. Zakładamy, że w Pythonie nie ma funkcji print i mamy ją sami napisać. Niech nasza funkcja nazywa się wyswietl. Ma ona działać tak samo jak znana nam funkcja print w najprostszej postaci - czyli wypisywać przekazane jej (rozdzielone przecinkami) różne dane (napisy, liczby, listy, krotki itp.)

Do dyspozycji mamy (po wpisaniu `import sys`) systemową funkcję write, która w postaci:

```python
sys.stdout.write(napis)
```

potrafi wypisać jeden napis na ekran

oraz wiemy, że każdą daną która ma być wypisana na ekran można zamienić na napis funkcją str.

Można zatem idąc po wszystkich danych zamieniać je na napisy i łączyć w jeden napis wynikowy (jak w zadaniu Cyfry słownie). Proszę to zrobić bez używania funkcji join.

Nasza funkcja wyswietl ma mieć także parametry sep i end takie, jakie występują w oryginalnym princie: sep ma rozdzielać wypisywane dane a end ma być dołączane na końcu wypisywanego napisu. Domyślnie sep to spacja a end to `'\n'`.

Problem umieszczania sep po ostatniej danej można rozwiązać stosując wycięcie, gdzie jako zakres wycinania podamy:

```python
[:-len(sep)]
```

Umieść poniższy kod w main, aby upewnić się, że działa tak jak z oryginalnym printem (czyli zamiana słowa wyswietl na print powinna dać taki sam wynik):

```python
wyswietl(21, 11, 2026, sep=".")

cena = 19.99
wyswietl( "Bilet kosztuje", cena , "zł", [1, 2] )

for _ in range(5):
    wyswietl( "#", end="" )
```

### 🇬🇧 Task description (EN)

Let's play at being the creator of the Python language. We assume that Python has no `print` function and we have to write it ourselves. Let our function be called `wyswietl` (Polish for "display"). It should work the same as the `print` function we know, in its simplest form - i.e. print the various data passed to it (separated by commas): strings, numbers, lists, tuples, etc.

We have at our disposal (after `import sys`) the system function `write`, which in the form:

```python
sys.stdout.write(string)
```

can print one string to the screen,

and we know that any piece of data to be printed can be converted to a string with the `str` function.

So, going over all the data, we can convert each of them to a string and concatenate them into one resulting string (as in the "Digits to Words" exercise, [ex13](../ex13/)). Please do this without using the `join` function.

Our `wyswietl` function should also have the `sep` and `end` parameters, like the original `print`: `sep` separates the printed data and `end` is appended at the end of the printed string. By default `sep` is a space and `end` is `'\n'`.

The problem of `sep` being placed after the last piece of data can be solved with slicing, using the range:

```python
[:-len(sep)]
```

Put the code below in `main` to make sure it works the same as the original `print` (i.e. replacing the word `wyswietl` with `print` should give the same result):

```python
wyswietl(21, 11, 2026, sep=".")

price = 19.99
wyswietl( "The ticket costs", price , "zł", [1, 2] )

for _ in range(5):
    wyswietl( "#", end="" )
```

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
