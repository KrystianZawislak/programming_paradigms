# Programming Paradigms

Assignments from the *Programming Paradigms* course, split into two parts:

- **[class_exercises/](class_exercises/)** - exercises from the classes. Task descriptions were written by **Piotr Pawlik**, the course lecturer (the author is also given in each exercise README). The 🇵🇱 descriptions are quoted verbatim; the 🇬🇧 translations and the solutions are my own.
- **[exam_practice/](exam_practice/)** - practice tasks for the test, written by Claude. Each one mirrors the class exercise with the same number: same difficulty, same required constructs and restrictions, different data.

## Structure

```
.
├── _template/              # README template for new exercises
├── new_exercise.sh         # script that creates the next exercise folder
├── class_exercises/
│   ├── ex1/
│   │   ├── README.md       # task (PL + EN), files, how to run
│   │   └── main.c
│   └── ...
└── exam_practice/
    ├── ex1/
    │   └── README.md       # task (PL + EN), files, how to run
    └── ...
```

## Adding a new exercise

```bash
./new_exercise.sh                              # next free number in class_exercises/
./new_exercise.sh "Higher-order functions"     # next number + title
./new_exercise.sh 5 "Recursion"                # specific number + title
./new_exercise.sh practice "Recursion"         # same, but in exam_practice/
```

Then paste the task description into the new `README.md` — the Polish original
under **Treść zadania (PL)** and the English version under **Task description (EN)**.

## Class exercises

| #   | Title | Status |
| --- | ----- | ------ |
| [1](class_exercises/ex1/) | Unstructured Christmas Trees (`goto`) | ✅ |
| [2](class_exercises/ex2/) | Sum and Product (return value vs. pointer) | ✅ |
| [3](class_exercises/ex3/) | Christmas Trees in Python | ✅ |
| [4](class_exercises/ex4/) | Counting 'a' and 'A' | ✅ |
| [5](class_exercises/ex5/) | Indexes of 'a' and 'A' | ✅ |
| [6](class_exercises/ex6/) | Multiplication Table | ✅ |
| [7](class_exercises/ex7/) | Guess the Number (while-else) | ✅ |
| [8](class_exercises/ex8/) | Days of the Week (match) | ✅ |
| [9](class_exercises/ex9/) | Making 100 zł from Coins | ✅ |
| [10](class_exercises/ex10/) | Prime Numbers (for-else) | ✅ |
| [11](class_exercises/ex11/) | Sums of Tuples | ✅ |
| [12](class_exercises/ex12/) | Leap Years (list comprehension) | ✅ |
| [13](class_exercises/ex13/) | Digits to Words (dictionary) | ✅ |
| [14](class_exercises/ex14/) | Roman Numerals to Integers | ✅ |
| [15](class_exercises/ex15/) | Contacts (dictionary with tuple keys) | ✅ |
| [16](class_exercises/ex16/) | Letter Positions | ✅ |
| [17](class_exercises/ex17/) | Words to Number (20-59) | ✅ |
| [18](class_exercises/ex18/) | 2D Array from Lists | ✅ |
| [19](class_exercises/ex19/) | Mean and Variance | ✅ |
| [20](class_exercises/ex20/) | Custom print Function (drukuj) | ✅ |
| [21](class_exercises/ex21/) | Numerical Derivative | ✅ |
| [22](class_exercises/ex22/) | String Decorator (upper) | ✅ |
| [23](class_exercises/ex23/) | Bisection Method | ✅ |
| [24](class_exercises/ex24/) | Prime Numbers with a Timing Decorator | ✅ |
| [25](class_exercises/ex25/) | Fibonacci Generators | ✅ |
| [26](class_exercises/ex26/) | Fibonacci Iterator Class | ✅ |
| [27](class_exercises/ex27/) | Class-Based String Decorator (upper) | ✅ |
| [28](class_exercises/ex28/) | Floating-Point range Generator (my_range) | ✅ |
