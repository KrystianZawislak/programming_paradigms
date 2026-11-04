# Exercise 20 — Custom print Function (drukuj)

> Course: Programming Paradigms
> Date: 2026-11-04

## Task

### 🇵🇱 Treść zadania (PL)

Zabawimy się w twórcę języka Python. Zakładamy, że w Pythonie nie ma funkcji print i mamy ją sami napisać. Ponieważ robimy to w Polsce, więc niech nazywa się ona drukuj. Ma ona działać tak samo jak znana nam funkcja print w najprostszej postaci - czyli wypisywać przekazane jej (rozdzielone przecinkami) różne dane (napisy, liczby, listy, krotki itp.)

Do dyspozycji mamy (po wpisaniu `import sys`) systemową funkcję write, która w postaci:

```python
sys.stdout.write(napis)
```

potrafi wypisać jeden napis na ekran

oraz wiemy, że każdą daną która ma być wypisana na ekran można zamienić na napis funkcją str.

Można zatem idąc po wszystkich danych zamieniać je na napisy i łączyć w jeden napis wynikowy (jak w zadaniu Cyfry słownie). Proszę to zrobić bez używania funkcji join, gdyż nie została ona omówiona na wykładzie.

Nasza funkcja drukuj ma mieć także parametry sep i end takie, jakie występują w oryginalnym princie: sep ma rozdzielać wypisywane dane a end ma być dołączane na końcu wypisywanego napisu. Domyślnie sep to spacja a end to `'\n'`.

Problem umieszczania sep po ostatniej danej można rozwiązać stosując wycięcie, gdzie jako zakres wycinania podamy:

```python
[:-len(sep)]
```

Umieść poniższy kod w main, aby upewnić się, że działa tak jak z oryginalnym printem (czyli zamiana słowa drukuj na print powinna dać taki sam wynik):

```python
drukuj(192,168,0,1, sep=":")

temperatura = 36.6
drukuj( "Temperatura wynosi", temperatura , "stopni" )

for _ in range(10):
    drukuj( "*", end="" )
```

### 🇬🇧 Task description (EN)

Let's play at being the creator of the Python language. We assume that Python has no `print` function and we have to write it ourselves. Since we are doing this in Poland, let it be called `drukuj` (Polish for "print"). It should work the same as the `print` function we know, in its simplest form - i.e. print the various data passed to it (separated by commas): strings, numbers, lists, tuples, etc.

We have at our disposal (after `import sys`) the system function `write`, which in the form:

```python
sys.stdout.write(string)
```

can print one string to the screen,

and we know that any piece of data to be printed can be converted to a string with the `str` function.

So, going over all the data, we can convert each of them to a string and concatenate them into one resulting string (as in the "Digits to Words" exercise). Please do this without using the `join` function, as it has not been covered in the lecture.

Our `drukuj` function should also have the `sep` and `end` parameters, like the original `print`: `sep` separates the printed data and `end` is appended at the end of the printed string. By default `sep` is a space and `end` is `'\n'`.

The problem of `sep` being placed after the last piece of data can be solved with slicing, using the range:

```python
[:-len(sep)]
```

Put the code below in `main` to make sure it works the same as the original `print` (i.e. replacing the word `drukuj` with `print` should give the same result):

```python
drukuj(192,168,0,1, sep=":")

temperature = 36.6
drukuj( "The temperature is", temperature , "degrees" )

for _ in range(10):
    drukuj( "*", end="" )
```

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - `drukuj(*args, sep=' ', end='\n')` converts each argument with `str`, appends `sep` after it, cuts the last `sep` off with `[:-len(sep)]` and writes the result plus `end` with `sys.stdout.write`. |

## How to run

macOS / Linux:

```bash
python3 main.py
```

Windows:

```powershell
py main.py
```

Example output (the same as with `print`):

```
192:168:0:1
The temperature is 36.6 degrees
**********
```
