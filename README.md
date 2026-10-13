# Programming Paradigms

Assignments from the *Programming Paradigms* course.

## Structure

```
.
├── _template/          # README template for new exercises
├── new_exercise.sh     # script that creates the next exercise folder
├── ex1/
│   └── README.md       # task (PL + EN), solution notes, how to run
├── ex2/
└── ...
```

## Adding a new exercise

```bash
./new_exercise.sh                    # next free number, e.g. ex2
./new_exercise.sh "Higher-order functions"   # next number + title
./new_exercise.sh 5 "Recursion"      # specific number + title
```

Then paste the task description into the new `README.md` — the Polish original
under **Treść zadania (PL)** and the English version under **Task description (EN)**.

## Exercises

| #   | Title | Status |
| --- | ----- | ------ |
| [1](ex1/) | Unstructured Christmas Trees (`goto`) | ✅ |
| [2](ex2/) | Sum and Product (return value vs. pointer) | ✅ |
