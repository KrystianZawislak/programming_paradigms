# Exercise 28 — Floating-Point range Generator (my_range)

> Course: Programming Paradigms
> Date: 2026-11-18

## Task

### 🇵🇱 Treść zadania (PL)

Napisz generator my_range, który przyjmuje od jednego do trzech parametrów i naśladuje działanie standardowego generatora range, ale działa dla argumentów zmiennoprzecinkowych.

A więc:

```
my_range ( a, b ,k ) wygeneruje wartości:   a, a+k, . . . ,x  gdzie x < b
my_range ( a, b ) wygeneruje to samo co: my_range ( a, b, 1.0 )
my_range ( n ) wygeneruje to samo co: my_range ( 0.0 , n )
```

Czyli np.:

```
my_range(1.1, 2.2, 0.5) wygeneruje: 1.1, 1.6, 2.1
my_range(1.1, 2.1, 0.5) wygeneruje: 1.1, 1.6
my_range(1.1, 2.2) wygeneruje: 1.1, 2.1
my_range(2.2) wygeneruje: 0.0, 1.0, 2.0
my_range(2.2, 0.1, -0.5) wygeneruje: 2.2, 1.7, 1.2, 0.7, 0.2
```

Dla k == 0.0 oraz dla liczby argumentów >3 i <1 generator nic nie powinien wygenerować.

Należy też pamiętać, że k może być ujemne.

Test działania my_range powinien być zrobiony w funkcji main i powinien polegać na użyciu wymienionych powyżej przykładów w pętlach for wypisujących wygenerowane wartości.

### 🇬🇧 Task description (EN)

Write a generator `my_range` that takes from one to three parameters and imitates the standard `range` generator, but works for floating-point arguments.

So:

```
my_range ( a, b ,k ) will generate the values:   a, a+k, . . . ,x  where x < b
my_range ( a, b ) will generate the same as: my_range ( a, b, 1.0 )
my_range ( n ) will generate the same as: my_range ( 0.0 , n )
```

For example:

```
my_range(1.1, 2.2, 0.5) will generate: 1.1, 1.6, 2.1
my_range(1.1, 2.1, 0.5) will generate: 1.1, 1.6
my_range(1.1, 2.2) will generate: 1.1, 2.1
my_range(2.2) will generate: 0.0, 1.0, 2.0
my_range(2.2, 0.1, -0.5) will generate: 2.2, 1.7, 1.2, 0.7, 0.2
```

For k == 0.0 and for the number of arguments >3 and <1 the generator should generate nothing.

Remember also that k can be negative.

The test of `my_range` should be done in the `main` function and should consist of using the examples above in `for` loops printing the generated values.

## Files

| File      | Description |
| --------- | ----------- |
| `main.py` | Solution - `my_range(*args)` sets `start`, `end` and `jump` depending on `len(args)`, returns immediately (generates nothing) for a wrong number of arguments or `jump == 0.0`, and yields values while `start < end` (positive step) or `start > end` (negative step); `main` runs the five examples from the task. |

## How to run

macOS / Linux:

```bash
python3 main.py
```

Windows:

```powershell
py main.py
```

Example output (the long tails in the last block come from floating-point rounding):

```
1.1
1.6
2.1
--------------------
1.1
1.6
--------------------
1.1
2.1
--------------------
0.0
1.0
2.0
--------------------
2.2
1.7000000000000002
1.2000000000000002
0.7000000000000002
0.20000000000000018
--------------------
```
