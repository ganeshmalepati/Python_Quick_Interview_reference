"""
Day 2 -- Lists, Tuples & Sets

### Lists
- Lists are ordered, mutable sequences.
- Key methods:
  - `append(x)` adds one item
  - `extend(iterable)` concatenates another iterable
  - `insert(i, x)` places an item at index
  - `remove(x)` deletes first matching value
  - `pop([i])` removes and returns by index
  - `clear()` empties the list
  - `sort()` sorts in place
  - `reverse()` reverses in place
  - `copy()` returns a shallow copy
  - `index(x)` finds first occurrence
  - `count(x)` counts occurrences

- Important concepts:
  - Mutable vs immutable: lists can change in place; strings and tuples cannot.
  - Shallow vs deep copy:
    - `list.copy()` or slicing `lst[:]` copies the outer list only.
    - Nested mutable elements still share references.
    - Use `copy.deepcopy()` for fully independent nested structures.
  - List comprehension:
    - Concise, readable, and often faster than loops.
    - Example: `[x*2 for x in nums if x % 2 == 0]`
  - Nested lists:
    - Use nested loops or nested comprehensions.
    - Beware shared inner lists when using multiplication like `[[0]*n]*m`.

### Tuples
- Tuples are ordered, immutable sequences.
- Packing/unpacking:
  - `t = 1, 2, 3` packs values
  - `a, b, c = t` unpacks them
- Why immutable:
  - Safer for fixed collections
  - Can be used as dictionary keys
- Tuple as dict key:
  - Only hashable, immutable objects can serve as keys.
  - Use tuples for compound keys like `(user_id, date)`.

### Sets
- Sets are unordered collections of unique items.
- Common methods:
  - `add(x)` insert element
  - `remove(x)` delete element, raises `KeyError` if missing
  - `discard(x)` delete element safely
  - `union(other)` returns combined unique items
  - `intersection(other)` returns common items
  - `difference(other)` returns items in one set but not the other
  - `issubset(other)` checks containment
  - `issuperset(other)` checks superset relation

### Common pitfalls & how to avoid them
- Reusing a list reference instead of copying:
  - Bug: `b = a` means both names point to same list.
  - Fix: use `a.copy()` or `list(a)` for independent copy.
- Mutating nested lists inadvertently:
  - Bug: `matrix = [[0]*n]*m`
  - Fix: use `[ [0]*n for _ in range(m) ]`
- Using `remove()` when element may not exist:
  - Bug: `remove()` raises if missing
  - Fix: use `discard()` for sets, or guard with `if x in lst`.
- Sorting vs returning a sorted list:
  - Bug: `sorted_list = lst.sort()` returns `None`
  - Fix: use `lst.sort()` for in-place or `sorted(lst)` for a new list.
- Assuming tuple immutability protects nested objects:
  - Note: tuples are immutable, but mutable items inside them can still change.

### Practice problem focus
- Second largest: handle duplicates safely
- Rotate array: use slicing or modulo indexing
- Remove duplicates: use `set` or preserve order with `dict.fromkeys()`
- Merge arrays: use `extend()` or `+`, sort if needed
- Missing number: use arithmetic sum or XOR
- Move zeros: preserve order while shifting non-zero elements
- Two Sum / Pair with target sum: use hash map for O(n)
- Product except self: compute prefix/suffix products without division
- Kth largest: use `heapq.nlargest()` or quickselect for performance

### Summary for daily recap
- Lists: mutable, rich API, list comprehensions, shallow vs deep copy
- Tuples: immutable packing/unpacking, stable hashable keys
- Sets: unique items, set algebra, safe remove semantics
- Engineers should focus on reference behavior, copy semantics, and in-place vs functional operations to avoid the most common bugs.

Extra imp info
--------------

Mutable

Object can change after creation. 
After obj creation also when we do any addition or deletion it will reflect to the same object

Immutable

Cannot change.
Once we have created one object it cannot modify or delete if we perform such actions it will creates a new object reference.

Why are strings immutable?

Expected answers:

Thread safety
Hashable
Dictionary keys
Memory optimization
 

--> list.append() will take the entire obj as a single and adds at the end of the list.
    Ex:- nums.append([4,5])
    Result:- [1,2,3,[4,5]]
    People expect:- [1,2,3,4,5] (Wrong)
--> list.extend() will add each and every element seperately like adds multiple items.
    a=[1,2]
    a.extend([3,4])
    Result:- [1,2,3,4]
    a.extend("abc")
    Result:- [1,2,'a','b','c']

--> Professional Difference  ---  sorted(nums)  -- returns new list.
--> Professional Difference  ---  nums.sort()   -- modifies existing list.

--> Shallow Copy --  b=a.copy()  --  Outer list copied.  --  b[0].append(10)->Both change(list a and b).
--> Deep Copy -- import copy -> b=copy.deepcopy(a)  --  Everything copied -> Independent. -- It won't change the original list.

"""


# Codeing-Practice-Session


# Code-1

def second_largest_element(data):
    first_largest = second_large = float('-inf')
    for i in data:
        if i>first_largest:
            second_large = first_largest
            first_largest = i
        elif first_largest > i > second_large:
            second_large = i
    return second_large

data = [23525, 46363, 634, 2525, 346346, 3453, 3452524, 3634, 633435, 3, 43636, 3463, 34633, 364643, 453, 25453, 363, 6346, 3463463, 436346, 346346, 346, 36346]
print(second_largest_element(data))
    

# Code-2

def rotate_array_by_k_elements_left(arr, k):
    if not arr:
        return ""
    
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]


arr = [23, 34, 45, 56, 67, 78]
k = 3
print(rotate_array_by_k_elements_left(arr, k))


# Code-3

def rotate_array_by_k_elements_right(arr, k):
    if not arr:
        return ""
    
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]


arr = [23, 34, 45, 56, 67, 78]
k = 2
print(rotate_array_by_k_elements_right(arr, k))


# Code-4

def rotate_array_by_k_elements(arr, k):
    if not arr:
        return arr

    n = len(arr)
    k %= n

    def reverse(left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

    return arr


arr = [23, 34, 45, 56, 67, 78]
print(rotate_array_by_k_elements(arr, 3))


# Code-5

def remove_duplicates_array(arr):
    temp = set()
    res = []
    for i in arr:
        if i not in temp:
            temp.add(i)
            res.append(i)
    return res

arr = [2,3,4,5,3,4,5,3,2,1,3,5,6,7,4,6,5,7,7,5,8,7]
print(remove_duplicates_array(arr))


# Code-6

def merge_arrays(arr1, arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr1[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result

arr1 = [1,3,5,7]
arr2 = [2,4,6,8]
print(merge_arrays(arr1, arr2))


# Code-7

def find_missing_number(nums):
    n = max(nums)

    actual = sum(nums)
    expected = n * (n+1) // 2
    return expected - actual

nums = [1,2,3,4,5,6,8,9]
print(find_missing_number(nums))


# Code-8

def moves_zero_end_or_trail_zeros(arr):
    zero_position = arr[0]
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[zero_position], arr[i] = arr[i], arr[zero_position]
            zero_position += 1
    return arr

arr = [0,23,4,0,3,0,6,0,7,0,4,78,35,68,0]
print(moves_zero_end_or_trail_zeros(arr))


# Code-9
  # Brute Force Approach

def B_F_A(arr,target):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
              return [i, j]

arr = [34,56,45,77,2,57,89,686,5575,864,6474,454,3435,567,3463,463,567,67]
target = 3465
print(B_F_A(arr, target))


  # Optimized approach
def two_sum_optimize_approach(nums, target):
    res = {}
    for idx, val in enumerate(nums):
        complement = target - val
        if complement in res:
            return [res[complement], idx]
        res[val] = idx

    return []

arr = [34,56,45,77,2,57,89,686,5575,864,6474,454,3435,567,3463,463,567,67]
target = 3465
print(two_sum_optimize_approach(arr, target))



def two_sum_problem(arr, target):               # Applicable for only sorted array. so, check before doing.
    left = 0
    right = len(arr)-1
    arr.sort()

    while left < right:
        
        current = arr[left] + arr[right]

        if current == target:
            return [left, right]
        
        elif current < target:
            left += 1

        else:
            right -= 1
    return []

arr = [34,56,45,77,2,57,89,686,5575,864,6474,454,3435,567,3463,463,567,67]
target = 3465
print(two_sum_problem(arr,target))
    








