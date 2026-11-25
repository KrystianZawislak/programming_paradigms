# Exercise 19 — Mean and Standard Deviation

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 19 — Mean and Variance](../../../class_exercises/4_functions/19_mean_and_variance/) by Piotr Pawlik
> Date: 2026-11-21

## Task

### 🇵🇱 Treść zadania (PL)

Należy napisać JEDNĄ funkcję liczącą średnią wartości z tablicy (x) oraz ich odchylenie standardowe (s) wg wzorów:

$$\bar{x} = \frac{1}{N} \sum_{i=1}^{N} x_i$$

$$s = \sqrt{\frac{1}{N-1} \sum_{i=1}^{N} (x_i - \bar{x})^2}$$

gdzie N - liczba elementów tablicy, x<sub>i</sub> - i-ty element tablicy. Proszę tu wykorzystać dwie pętle **for** (**nie** używać np. **sum**). Pierwiastek jest dostępny jako `math.sqrt` (po `import math`).

Funkcja ma otrzymywać tablicę jako argument i zwracać OBIE obliczone wartości (ale **nie** w postaci słownika).

W main dwukrotnie wywołaj napisaną funkcję z tablicami [10,10,10] oraz [2,4,4,4,5,5,7,9] i dla każdej tablicy wypisz uzyskane wyniki w **dwóch** osobnych liniach w postaci:

```
Średnia wynosi: ...
Odchylenie standardowe wynosi: ...
```

### 🇬🇧 Task description (EN)

Write ONE function that computes the mean of the values in an array (x) and their standard deviation (s) according to the formulas:

$$\bar{x} = \frac{1}{N} \sum_{i=1}^{N} x_i$$

$$s = \sqrt{\frac{1}{N-1} \sum_{i=1}^{N} (x_i - \bar{x})^2}$$

where N - the number of elements of the array, x<sub>i</sub> - the i-th element of the array. Use two **for** loops here (do **not** use e.g. **sum**). The square root is available as `math.sqrt` (after `import math`).

The function should take the array as an argument and return BOTH computed values (but **not** as a dictionary).

In `main`, call the function twice, with the arrays [10,10,10] and [2,4,4,4,5,5,7,9], and for each array print the results in **two** separate lines in the form:

```
The mean is: ...
The standard deviation is: ...
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
