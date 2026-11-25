# Exercise 19 — Mean and Variance

> Course: Programming Paradigms
> Task author: Piotr Pawlik
> Date: 2026-11-04

## Task

### 🇵🇱 Treść zadania (PL)

Należy napisać JEDNĄ funkcję liczącą średnią wartości z tablicy (x) oraz ich wariancję (w) wg wzorów:

$$w = \frac{1}{N-1} \sum_{i=1}^{N} (x_i - \bar{x})^2$$

$$\bar{x} = \frac{1}{N} \sum_{i=1}^{N} x_i$$

gdzie N - liczba elementów tablicy, x<sub>i</sub> - i-ty element tablicy. Proszę tu wykorzystać dwie pętle **for** (**nie** używać np. **sum**).

Funkcja ma otrzymywać tablicę jako argument i zwracać OBIE obliczone wartości (ale **nie** w postaci słownika).

W main dwukrotnie wywołaj napisaną funkcję z tablicami [3,3,3,3] oraz [5,6,7,8,9] i dla każdej tablicy wypisz uzyskane wyniki w **dwóch** osobnych liniach w postaci:

```
Średnia wynosi: ...
Wariancja wynosi: ...
```

### 🇬🇧 Task description (EN)

Write ONE function that computes the mean of the values in an array (x) and their variance (w) according to the formulas:

$$w = \frac{1}{N-1} \sum_{i=1}^{N} (x_i - \bar{x})^2$$

$$\bar{x} = \frac{1}{N} \sum_{i=1}^{N} x_i$$

where N - the number of elements of the array, x<sub>i</sub> - the i-th element of the array. Use two **for** loops here (do **not** use e.g. **sum**).

The function should take the array as an argument and return BOTH computed values (but **not** as a dictionary).

In `main`, call the function twice, with the arrays [3,3,3,3] and [5,6,7,8,9], and for each array print the results in **two** separate lines in the form:

```
The mean is: ...
The variance is: ...
```

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - `mean_and_variance` computes the mean in the first `for` loop and the variance in the second one, and returns both as a tuple. |

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
The mean is: 3.0
The variance is: 0.0
The mean is: 7.0
The variance is: 2.5
```
