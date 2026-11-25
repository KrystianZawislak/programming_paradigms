# Programming Paradigms

Assignments from the *Programming Paradigms* course, split into two parts:

- **[class_exercises/](class_exercises/)** - exercises from the classes. Task descriptions were written by **Piotr Pawlik**, the course lecturer (the author is also given in each exercise README). The 🇵🇱 descriptions are quoted verbatim; the 🇬🇧 translations and the solutions are my own.
- **[exam_practice/](exam_practice/)** - practice tasks for the test, written by Claude. Each one mirrors the class exercise with the same number: same difficulty, same required constructs and restrictions, different data.

Both parts are grouped by the course topics; exercise numbers are global and the same in both parts.

## Structure

```
.
├── _template/                         # README template for new exercises
├── new_exercise.sh                    # script that creates a new exercise folder
├── class_exercises/
│   ├── 1_unstructured_programming/
│   │   ├── 01_goto_christmas_trees/
│   │   │   ├── README.md              # task (PL + EN), files, how to run
│   │   │   └── main.c
│   │   └── ...
│   └── ...
└── exam_practice/                     # same topics, same numbers
    └── ...
```

## Adding a new exercise

```bash
./new_exercise.sh 6 point_class "Point Class"            # class_exercises/6_.../30_point_class
./new_exercise.sh practice 6 point_class "Point Class"   # same in exam_practice/
./new_exercise.sh                                        # prints usage and the topic list
```

The number is assigned automatically (next free one). A new topic is a new folder,
e.g. `class_exercises/7_<topic_name>/`. Paste the task description into the new
`README.md` — the Polish original under **Treść zadania (PL)** and the English version
under **Task description (EN)**.

## Class exercises


### 1. Unstructured programming (Programowanie niestrukturalne)

| #   | Title | Status |
| --- | ----- | ------ |
| [1](class_exercises/1_unstructured_programming/01_goto_christmas_trees/) | Unstructured Christmas Trees (`goto`) | ✅ |
| [2](class_exercises/1_unstructured_programming/02_sum_and_product_pointer/) | Sum and Product (return value vs. pointer) | ✅ |

### 2. Control statements (Instrukcje sterujące)

| #   | Title | Status |
| --- | ----- | ------ |
| [3](class_exercises/2_control_statements/03_christmas_trees/) | Christmas Trees in Python | ✅ |
| [4](class_exercises/2_control_statements/04_counting_letters/) | Counting 'a' and 'A' | ✅ |
| [5](class_exercises/2_control_statements/05_letter_indexes_enumerate/) | Indexes of 'a' and 'A' | ✅ |
| [6](class_exercises/2_control_statements/06_multiplication_table/) | Multiplication Table | ✅ |
| [7](class_exercises/2_control_statements/07_guess_the_number_while_else/) | Guess the Number (while-else) | ✅ |
| [8](class_exercises/2_control_statements/08_days_of_week_match/) | Days of the Week (match) | ✅ |
| [9](class_exercises/2_control_statements/09_coins_100_zl/) | Making 100 zł from Coins | ✅ |
| [10](class_exercises/2_control_statements/10_prime_numbers_for_else/) | Prime Numbers (for-else) | ✅ |

### 3. Collections (Kolekcje)

| #   | Title | Status |
| --- | ----- | ------ |
| [11](class_exercises/3_collections/11_tuple_sums/) | Sums of Tuples | ✅ |
| [12](class_exercises/3_collections/12_leap_years_list_comprehension/) | Leap Years (list comprehension) | ✅ |
| [13](class_exercises/3_collections/13_digits_to_words/) | Digits to Words (dictionary) | ✅ |
| [14](class_exercises/3_collections/14_roman_numerals/) | Roman Numerals to Integers | ✅ |
| [15](class_exercises/3_collections/15_contacts_tuple_keys/) | Contacts (dictionary with tuple keys) | ✅ |
| [16](class_exercises/3_collections/16_letter_positions/) | Letter Positions | ✅ |
| [17](class_exercises/3_collections/17_words_to_number/) | Words to Number (20-59) | ✅ |
| [18](class_exercises/3_collections/18_2d_array_from_lists/) | 2D Array from Lists | ✅ |

### 4. Functions (Funkcje)

| #   | Title | Status |
| --- | ----- | ------ |
| [19](class_exercises/4_functions/19_mean_and_variance/) | Mean and Variance | ✅ |
| [20](class_exercises/4_functions/20_custom_print_drukuj/) | Custom print Function (drukuj) | ✅ |
| [21](class_exercises/4_functions/21_numerical_derivative/) | Numerical Derivative | ✅ |
| [22](class_exercises/4_functions/22_upper_decorator/) | String Decorator (upper) | ✅ |
| [23](class_exercises/4_functions/23_bisection/) | Bisection Method | ✅ |
| [24](class_exercises/4_functions/24_primes_timing_decorator/) | Prime Numbers with a Timing Decorator | ✅ |

### 5. Subroutines (Podprogramy)

| #   | Title | Status |
| --- | ----- | ------ |
| [25](class_exercises/5_subroutines/25_fibonacci_generators/) | Fibonacci Generators | ✅ |
| [26](class_exercises/5_subroutines/26_fibonacci_iterator_class/) | Fibonacci Iterator Class | ✅ |
| [27](class_exercises/5_subroutines/27_class_decorator/) | Class-Based String Decorator (upper) | ✅ |
| [28](class_exercises/5_subroutines/28_float_range_generator/) | Floating-Point range Generator (my_range) | ✅ |

### 6. Objects - members and inheritance (Obiekty - składowe i dziedziczenie)

| #   | Title | Status |
| --- | ----- | ------ |
| [29](class_exercises/6_objects_members_and_inheritance/29_fraction_class/) | Fraction Class (operator overloading) | ✅ |
| [30](class_exercises/6_objects_members_and_inheritance/30_shapes_abstract_class/) | Geometric Shapes (abstract class, inheritance) | ✅ |
| [31](class_exercises/6_objects_members_and_inheritance/31_matrix_indexing/) | Matrix with C, Pascal and Matlab Indexing | ✅ |

## Exam practice


### 1. Unstructured programming (Programowanie niestrukturalne)

| #   | Title | Based on | Status |
| --- | ----- | -------- | ------ |
| [1](exam_practice/1_unstructured_programming/01_goto_upside_down_trees/) | Upside-Down Trees (`goto`) | [1](class_exercises/1_unstructured_programming/01_goto_christmas_trees/) | ⬜ |
| [2](exam_practice/1_unstructured_programming/02_difference_and_quotient_pointer/) | Difference and Quotient (return value vs. pointer) | [2](class_exercises/1_unstructured_programming/02_sum_and_product_pointer/) | ⬜ |

### 2. Control statements (Instrukcje sterujące)

| #   | Title | Based on | Status |
| --- | ----- | -------- | ------ |
| [3](exam_practice/2_control_statements/03_upside_down_trees/) | Upside-Down Trees in Python | [3](class_exercises/2_control_statements/03_christmas_trees/) | ⬜ |
| [4](exam_practice/2_control_statements/04_counting_letters/) | Counting 'o' and 'O' | [4](class_exercises/2_control_statements/04_counting_letters/) | ⬜ |
| [5](exam_practice/2_control_statements/05_letter_indexes_enumerate/) | Indexes of 'o' and 'O' | [5](class_exercises/2_control_statements/05_letter_indexes_enumerate/) | ⬜ |
| [6](exam_practice/2_control_statements/06_multiplication_table_12x12/) | Multiplication Table 12x12 | [6](class_exercises/2_control_statements/06_multiplication_table/) | ⬜ |
| [7](exam_practice/2_control_statements/07_guess_the_number_while_else/) | Guess the Number 1-20 (while-else) | [7](class_exercises/2_control_statements/07_guess_the_number_while_else/) | ⬜ |
| [8](exam_practice/2_control_statements/08_months_match/) | Months of the Year (match) | [8](class_exercises/2_control_statements/08_days_of_week_match/) | ⬜ |
| [9](exam_practice/2_control_statements/09_coins_50_zl/) | Making 50 zł from Coins | [9](class_exercises/2_control_statements/09_coins_100_zl/) | ⬜ |
| [10](exam_practice/2_control_statements/10_prime_numbers_for_else/) | Prime Numbers 100-200 (for-else) | [10](class_exercises/2_control_statements/10_prime_numbers_for_else/) | ⬜ |

### 3. Collections (Kolekcje)

| #   | Title | Based on | Status |
| --- | ----- | -------- | ------ |
| [11](exam_practice/3_collections/11_tuple_sums/) | Sums of Tuples | [11](class_exercises/3_collections/11_tuple_sums/) | ⬜ |
| [12](exam_practice/3_collections/12_leap_years_list_comprehension/) | Leap Years (list comprehension) | [12](class_exercises/3_collections/12_leap_years_list_comprehension/) | ⬜ |
| [13](exam_practice/3_collections/13_phone_number_to_words/) | Digits to Words (dictionary) | [13](class_exercises/3_collections/13_digits_to_words/) | ⬜ |
| [14](exam_practice/3_collections/14_roman_numerals/) | Roman Numerals to Integers | [14](class_exercises/3_collections/14_roman_numerals/) | ⬜ |
| [15](exam_practice/3_collections/15_contacts_tuple_keys/) | Contacts (dictionary with tuple keys) | [15](class_exercises/3_collections/15_contacts_tuple_keys/) | ⬜ |
| [16](exam_practice/3_collections/16_letter_positions/) | Letter Positions | [16](class_exercises/3_collections/16_letter_positions/) | ⬜ |
| [17](exam_practice/3_collections/17_words_to_number/) | Words to Number (60-99) | [17](class_exercises/3_collections/17_words_to_number/) | ⬜ |
| [18](exam_practice/3_collections/18_2d_array_cubes/) | 2D Array from Lists (cubes) | [18](class_exercises/3_collections/18_2d_array_from_lists/) | ⬜ |

### 4. Functions (Funkcje)

| #   | Title | Based on | Status |
| --- | ----- | -------- | ------ |
| [19](exam_practice/4_functions/19_mean_and_standard_deviation/) | Mean and Standard Deviation | [19](class_exercises/4_functions/19_mean_and_variance/) | ⬜ |
| [20](exam_practice/4_functions/20_custom_print_wyswietl/) | Custom print Function (wyswietl) | [20](class_exercises/4_functions/20_custom_print_drukuj/) | ⬜ |
| [21](exam_practice/4_functions/21_central_difference_derivative/) | Numerical Derivative (central difference) | [21](class_exercises/4_functions/21_numerical_derivative/) | ⬜ |
| [22](exam_practice/4_functions/22_underscore_decorator/) | String Decorator (spaces to underscores) | [22](class_exercises/4_functions/22_upper_decorator/) | ⬜ |
| [23](exam_practice/4_functions/23_bisection/) | Bisection Method | [23](class_exercises/4_functions/23_bisection/) | ⬜ |
| [24](exam_practice/4_functions/24_primes_timing_decorator/) | Prime Numbers with a Timing Decorator | [24](class_exercises/4_functions/24_primes_timing_decorator/) | ⬜ |

### 5. Subroutines (Podprogramy)

| #   | Title | Based on | Status |
| --- | ----- | -------- | ------ |
| [25](exam_practice/5_subroutines/25_lucas_generators/) | Lucas Sequence Generators | [25](class_exercises/5_subroutines/25_fibonacci_generators/) | ⬜ |
| [26](exam_practice/5_subroutines/26_lucas_iterator_class/) | Lucas Iterator Class | [26](class_exercises/5_subroutines/26_fibonacci_iterator_class/) | ⬜ |
| [27](exam_practice/5_subroutines/27_class_decorator/) | Class-Based String Decorator (spaces to underscores) | [27](class_exercises/5_subroutines/27_class_decorator/) | ⬜ |
| [28](exam_practice/5_subroutines/28_float_range_generator/) | Floating-Point range Generator (float_range) | [28](class_exercises/5_subroutines/28_float_range_generator/) | ⬜ |

### 6. Objects - members and inheritance (Obiekty - składowe i dziedziczenie)

| #   | Title | Based on | Status |
| --- | ----- | -------- | ------ |
| [29](exam_practice/6_objects_members_and_inheritance/29_fraction_class/) | Fraction Class (operator overloading) | [29](class_exercises/6_objects_members_and_inheritance/29_fraction_class/) | ⬜ |
| [30](exam_practice/6_objects_members_and_inheritance/30_solids_abstract_class/) | Solids (abstract class, inheritance) | [30](class_exercises/6_objects_members_and_inheritance/30_shapes_abstract_class/) | ⬜ |
| [31](exam_practice/6_objects_members_and_inheritance/31_matrix_indexing/) | Matrix with C, Pascal and Matlab Indexing | [31](class_exercises/6_objects_members_and_inheritance/31_matrix_indexing/) | ⬜ |
