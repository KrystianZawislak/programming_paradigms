# Exercise 28 — Floating-Point range Generator (float_range)

> Course: Programming Paradigms — exam practice
> Task author: Claude, based on [class exercise 28 — Floating-Point range Generator (my_range)](../../../class_exercises/5_subroutines/28_float_range_generator/) by Piotr Pawlik
> Date: 2026-11-21

## Task

### 🇵🇱 Treść zadania (PL)

Napisz generator float_range, który przyjmuje od jednego do trzech parametrów i naśladuje działanie standardowego generatora range, ale działa dla argumentów zmiennoprzecinkowych.

A więc:

```
float_range ( a, b ,k ) wygeneruje wartości:   a, a+k, . . . ,x  gdzie x < b
float_range ( a, b ) wygeneruje to samo co: float_range ( a, b, 1.0 )
float_range ( n ) wygeneruje to samo co: float_range ( 0.0 , n )
```

Czyli np.:

```
float_range(0.5, 2.0, 0.4) wygeneruje: 0.5, 0.9, 1.3, 1.7
float_range(0.5, 1.7, 0.4) wygeneruje: 0.5, 0.9, 1.3
float_range(0.5, 2.0) wygeneruje: 0.5, 1.5
float_range(3.5) wygeneruje: 0.0, 1.0, 2.0, 3.0
float_range(3.0, 0.2, -0.7) wygeneruje: 3.0, 2.3, 1.6, 0.9
```

Dla k == 0.0 oraz dla liczby argumentów >3 i <1 generator nic nie powinien wygenerować.

Należy też pamiętać, że k może być ujemne.

Test działania float_range powinien być zrobiony w funkcji main i powinien polegać na użyciu wymienionych powyżej przykładów w pętlach for wypisujących wygenerowane wartości.

### 🇬🇧 Task description (EN)

Write a generator `float_range` that takes from one to three parameters and imitates the standard `range` generator, but works for floating-point arguments.

So:

```
float_range ( a, b ,k ) will generate the values:   a, a+k, . . . ,x  where x < b
float_range ( a, b ) will generate the same as: float_range ( a, b, 1.0 )
float_range ( n ) will generate the same as: float_range ( 0.0 , n )
```

For example:

```
float_range(0.5, 2.0, 0.4) will generate: 0.5, 0.9, 1.3, 1.7
float_range(0.5, 1.7, 0.4) will generate: 0.5, 0.9, 1.3
float_range(0.5, 2.0) will generate: 0.5, 1.5
float_range(3.5) will generate: 0.0, 1.0, 2.0, 3.0
float_range(3.0, 0.2, -0.7) will generate: 3.0, 2.3, 1.6, 0.9
```

For k == 0.0 and for the number of arguments >3 and <1 the generator should generate nothing.

Remember also that k can be negative.

The test of `float_range` should be done in the `main` function and should consist of using the examples above in `for` loops printing the generated values.

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
