# Exercise 15 — Contacts (dictionary with tuple keys)

> Course: Programming Paradigms
> Task author: Piotr Pawlik
> Date: 2026-10-21

## Task

### 🇵🇱 Treść zadania (PL)

Dany jest "spis kontaktów" w postaci słownika:

```python
kontakty = {('Jan', 'Kowalski'):"123456789", ('Adam', 'Nowak'):"987654321" , ('Adam', 'Kowalski'): "600300900"}
```

Wypisz numer telefonu Adama Nowaka (jednym printem - używając słownika).
Napisz kod, który wypisze (używając pętli, przechodzącej po całym słowniku) numery telefonu obu Kowalskich.

### 🇬🇧 Task description (EN)

A "contact list" is given as a dictionary:

```python
contacts = {('Jan', 'Kowalski'):"123456789", ('Adam', 'Nowak'):"987654321" , ('Adam', 'Kowalski'): "600300900"}
```

Print Adam Nowak's phone number (with a single `print` - using the dictionary).
Write code that prints (using a loop going over the whole dictionary) the phone numbers of both Kowalskis.

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - looks up Adam Nowak by the `(name, surname)` tuple key, then loops over all keys unpacked into `name, surname` and prints the numbers of everyone with the surname Kowalski. |

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
987654321
123456789
600300900
```
