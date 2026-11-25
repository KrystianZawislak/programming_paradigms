# Exercise 27 — Class-Based String Decorator (upper)

> Course: Programming Paradigms
> Task author: Piotr Pawlik
> Date: 2026-11-18

## Task

### 🇵🇱 Treść zadania (PL)

Przerób zadanie z zeszłego tygodnia z dekoratorem zamieniającym litery na wielkie tak, aby dekorator był klasą a nie funkcją (skopiuj rozwiązanie z zeszłego tygodnia i tylko zamień funkcję dekoratora na odpowiednią klasę).

### 🇬🇧 Task description (EN)

Rework last week's exercise with the decorator converting letters to uppercase ([ex22](../../4_functions/22_upper_decorator/)) so that the decorator is a class instead of a function (copy last week's solution and only replace the decorator function with an appropriate class).

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - `to_upper` decorator class: `__init__` stores the decorated function in `self.function`, `__call__` calls it and returns `result.upper()`; the rest of [ex22](../../4_functions/22_upper_decorator/) is unchanged (`@to_upper` on `numbers_in_words`, `drukuj = to_upper(drukuj)`). The old function decorator is left commented out at the top. |

## How to run

macOS / Linux:

```bash
python3 main.py
```

Windows:

```powershell
py main.py
```

Example output (the same as in [ex22](../../4_functions/22_upper_decorator/)):

```
ONE FOUR ONE ZERO 
ALA-MA-KOTA
```
