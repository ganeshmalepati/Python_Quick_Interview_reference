"""
Day 1 – Core Python & Strings Recap

    ### Core Python Concepts

    #### Variables
    - A variable is a named reference to a value in memory.
    - Python variables are dynamically typed: `x = 10`, then `x = "hello"` is valid.
    - Common mistake: assuming a variable retains a type across the program. Always treat the current value, not the previous type.
    - Tip: use meaningful names (`user_count`, `invoice_total`) and avoid shadowing built-ins like `list`, `str`, `id`.

    #### Data types
    - Built-ins: `int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`.
    - Engineers should think in terms of “behavior”:
    - immutable vs mutable,
    - numeric vs sequence,
    - mapping vs iterable.
    - Common mistake: mutating a list when you meant an immutable tuple. Choose the right type for intent.

    #### Input/output
    - `input()` reads strings from the console.
    - `print()` formats output and can join values with `sep` and `end`.
    - Common mistake: forgetting `input()` returns `str`, not a number.
    - Overcome it by validating and casting immediately.

    #### Type casting
    - Explicit conversion: `int("42")`, `float("3.14")`, `str(100)`.
    - Use `bool()` carefully: `bool("")` is `False`, `bool("False")` is `True`.
    - Common mistake: casting invalid strings without error handling.
    - Overcome with `try/except` or `str.isdigit()` guard.

    #### Operators
    - Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
    - Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
    - Logical: `and`, `or`, `not`
    - Identity vs equality: `is` checks object identity, `==` checks value equality.
    - Common mistake: using `is` for string or int equality. Use `==` unless you want identity.

    #### if / elif / else
    - Conditional branches evaluate logical conditions in order.
    - Use `elif` instead of nested `if` for clarity.
    - Common mistake: non-exhaustive branches or relying on truthiness unintentionally.
    - Overcome with explicit comparisons and comments for edge cases.

    #### Loops
    - `for` iterates over any iterable.
    - `while` repeats while a condition stays true.
    - Use loops for repeated operations, not for one-off cases.
    - Common mistake: infinite `while` loops due to condition never changing.
    - Overcome by ensuring loop variables update and adding break conditions.

    #### break, continue, pass
    - `break` exits the loop immediately.
    - `continue` skips to the next iteration.
    - `pass` is a no-op placeholder.
    - Common mistake: using `break` to avoid poor loop logic instead of simplifying structure.
    - Overcome by designing loop flow cleanly, then applying `break/continue` only when they improve clarity.

    #### enumerate()
    - `enumerate(iterable)` yields `(index, value)`.
    - Used when you need loop counters with items.
    - Common mistake: manually tracking an index variable instead of using `enumerate`.
    - Overcome by preferring `for i, value in enumerate(items)`.

    #### zip()
    - `zip(a, b, ...)` pairs elements from multiple iterables.
    - Stop length is the shortest iterable.
    - Common mistake: assuming `zip` extends to the longest sequence.
    - Overcome by checking lengths or using `itertools.zip_longest` when needed.

    #### range()
    - `range(stop)`, `range(start, stop)`, `range(start, stop, step)`
    - Produces a lazy sequence of integers.
    - Common mistake: expecting `range` to return a list in Python 3. Use `list(range(...))` only when needed.
    - Overcome by treating `range` as an iterable and not consuming it unnecessarily.

    ---

    ### Strings (Core Methods)

    #### len()
    - Returns string length.
    - Use for validation and iteration boundaries.
    - Mistake: assuming `len()` counts “characters” the same as bytes in encoded data.

    #### lower() / upper()
    - Converts case for normalized comparison.
    - Useful for case-insensitive matching.
    - Mistake: forgetting `lower()` returns a new string because strings are immutable.

    #### title() / capitalize()
    - `title()` capitalizes each word; `capitalize()` only the first character.
    - Mistake: using `title()` for acronyms and losing casing (`API` → `Api`).

    #### split()
    - Splits a string into a list by delimiter.
    - Default splits on whitespace.
    - Mistake: `split()` on `","` when the string has spaces around commas. Use `split(",")` carefully or clean input first.

    #### join()
    - `'sep'.join(list_of_strings)` concatenates strings.
    - Preferred over repeated `+` for performance.
    - Mistake: joining non-string elements. Convert first or use comprehension.

    #### replace()
    - Replaces substrings.
    - Useful for simple normalization.
    - Mistake: expecting it to modify in place. It returns a new string.

    #### strip()
    - Removes whitespace from ends.
    - Can also remove specified characters.
    - Mistake: assuming `strip()` removes interior whitespace. It only trims ends.

    #### find() / index()
    - Both locate substrings; `find()` returns `-1` if missing, `index()` raises `ValueError`.
    - Use `find()` for safe existence checks, `index()` when absence is exceptional.
    - Mistake: using `index()` without a try/except.

    #### count()
    - Counts occurrences of a substring.
    - Useful for validation or statistics.
    - Mistake: overlapping substrings are not counted separately in the way some expect.

    #### startswith() / endswith()
    - Boolean checks for prefix/suffix.
    - More readable and reliable than slicing comparisons.
    - Mistake: manually comparing slices and risking off-by-one errors.

    #### isalpha() / isdigit() / isalnum()
    - Character class checks for alphabetic, digit-only, or alphanumeric strings.
    - Mistake: forgetting these reject empty strings and whitespace.
    - Overcome by checking length and stripping input first.

    ---

    ### String Behavior & Best Practices

    #### String immutability
    - Strings cannot change after creation.
    - Every modification returns a new string.
    - Mistake: assuming `s.replace(...)` updates `s`. Always reassign if needed: `s = s.replace(...)`.
    - Benefit: immutability makes strings safe in shared contexts and easier to reason about.

    #### Slicing
    - `s[start:stop]` returns a substring.
    - `s[:n]`, `s[n:]`, `s[start:stop:step]`
    - Mistake: misreading `stop` as inclusive. It is exclusive.
    - Overcome by thinking in half-open intervals: `[start, stop)`.

    #### Negative indexing
    - `s[-1]` is last char, `s[-2]` is second last.
    - Works naturally with slices: `s[-3:]`, `s[:-3]`.
    - Mistake: mixing negative indices with positive ranges can be confusing. Keep examples simple.

    #### String formatting
    - `%` formatting is older, `.format()` is flexible.
    - Example: `"Hello, {}".format(name)`.
    - Mistake: nesting format syntax or using the wrong placeholder type.
    - Prefer `f-strings` for clarity in modern Python.

    #### f-strings
    - `f"User={name}, age={age}"`
    - Most readable and performs well.
    - Supports expressions and formatting: `f"{value:.2f}"`.
    - Mistake: using complex logic inside f-strings. Keep expressions simple and move logic outside for readability.

    ---

    ### Key Mistakes and How to Avoid Them

    - Confusing object identity and equality: use `==` for values.
    - Forgetting that input is always a string: cast explicitly and validate.
    - Assuming strings mutate: reassign results from methods.
    - Misusing loops and conditionals: prefer readable flow over clever shortcuts.
    - Mishandling `zip()` length mismatch: be explicit about expected sequence lengths.
    - Using string methods without considering whitespace or encoding.

    ---

    Most Common Mistakes Professionals Still Make
        Using is instead of == (or vice versa) for value comparisons.
        Forgetting that strings are immutable and expecting methods like lower() or replace() to modify the original string.
        Assuming range(stop) includes the stop value.
        Using split(" ") instead of split() when whitespace can vary.
        Calling list.join(",") instead of ",".join(list).
        Using index() when a value may not exist, causing unexpected exceptions.
        Forgetting that zip() truncates to the shortest iterable unless strict=True is used.
        Accidentally sharing mutable objects through assignment instead of copying.
        Deeply nested if statements instead of using early returns or guard clauses.
        Ignoring invalid input and type conversion failures.


""" 


list_1 = [23,4,5,6,77,65,46,3,86,8]
list_2 = list_1
list_2.append(56)
# print(list_2)
print(list_1)

l1 = [2,3,4,5,6]
l2 = [1,5,7,9,11]
# l1.append(l2)
# print(l1)
l1.extend(l2)
print(l1)

for i in l1:
    if i % 2 == 0:
        print(i) 



names = ["Ganesh", "Suresh", "Ramesh", "Naresh"]
grades = ["A", "A", "B", "C"]

student_grades = list(zip(names, grades))           # generates the result as list of tuple values [(,), (,), (,)]
print(student_grades)
for name, grade in student_grades:
    print(f"{name}: {grade}")

name = "GaNesh"
n = name.lower()                    # 100% need to define one var while converting to lower or else no effect in it (only for lower case)
s = name.upper()
print(n)
print(s)
print(name.upper())                 # Update to UPPER case without assign of var.


name = "Malepati Ganesh"
name.split()
print(name)
splt_name = name.split()           # 100% need to define one var while splitting the string or else no effect on original string it remains same.
print(splt_name)
print(''.join(splt_name))          # join will convert list -> string,      split will convert string -> list.



# Code Practice Session

# Code-1

def reverse_string(s):
    r_s = ""
    for char in s:
        r_s = char + r_s
    return r_s

s = "Ganesh Malepati"
print(reverse_string(s))


# Code-2

def palindrome_string(s):
    if not s:
        return ""
    
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

s = "malayalam"
n = "Gani"
print(palindrome_string(s))
print(palindrome_string(n))


# Code-3

def count_vowels(s):
    vowels = "AEIOUaeiou"
    count = 0
    res = []
    for char in s:
        if char in vowels:
            count += 1
            res.append(char)
    return count, res

s = "Ganesh Malepati"
print(count_vowels(s))


# Code-4

def character_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

s = "Namma Bengaluru"
print(character_frequency(s))


# Code-5

def first_non_repeat_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char in freq:
        if freq[char] == 1:
            return char

s = "swiss"
print(first_non_repeat_char(s))


# Code-6

def reverse_words(s):
    rev_s = ""
    for char in s:
        rev_s = char + rev_s
    return rev_s

s = "This week i need to complete the full python recap"
print(reverse_words(s))


# Code-7

def anagrams_check(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = {}
    for char in s1:
        freq[char] = freq.get(char, 0) + 1
    for char in s2:
        if char not in freq or freq[char] == 0:
            return False
        freq[char] -= 1
    
    return True

s1 = "listen"
s2 = "silent"
print(anagrams_check(s1, s2))
l1 = "Gani"
l2 = "Mani"
print(anagrams_check(l1, l2))


# Code-8

def longest_substring_witout_repeat_characters(s):
    left = 0
    max_len = 0
    start = 0
    window = set()
    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])

        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left

    longest_substring = s[start:start + max_len]

    return max_len, longest_substring


s = "abcababccbdcce"
print(longest_substring_witout_repeat_characters(s))






 