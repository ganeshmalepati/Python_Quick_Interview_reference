"""
Daily Recap – Top 25 Python Practice Questions

1) Reverse String
- Main logic: reverse by iterating from the end or use slicing s[::-1].
- Common mistake: treating strings like mutable lists; use a new string or slicing.
- Overcome: pick a simple, readable approach and validate with examples.

2) Palindrome
- Main logic: compare characters from both ends toward the center.
- Common mistake: ignoring case and spaces in real-world strings.
- Overcome: normalize input first (lowercase, remove non-alphanumerics).

3) Anagram
- Main logic: compare character frequencies or sort both strings.
- Common mistake: checking only length or order.
- Overcome: use frequency counting for clarity and correctness.

4) First Non-Repeating Character
- Main logic: count frequencies, then scan for the first character with count 1.
- Common mistake: scanning twice without a map.
- Overcome: build a frequency table and reuse it.

5) Longest Substring Without Repeating Characters
- Main logic: use a sliding window with two pointers and a set/map.
- Common mistake: forgetting to shrink the window when a duplicate appears.
- Overcome: always move the left pointer while the duplicate remains.

6) Character Frequency Count
- Main logic: map each character to its frequency.
- Common mistake: using manual loops without a dictionary.
- Overcome: prefer dict.get(key, 0) for compact counting logic.

7) Remove Duplicates from String
- Main logic: keep first occurrence and skip repeats using a seen set.
- Common mistake: losing order when using a set alone.
- Overcome: preserve insertion order with a list plus set.

8) Two Sum
- Main logic: store seen values and check the complement target - value.
- Common mistake: doing nested loops when a hash map is enough.
- Overcome: think in terms of lookup efficiency and complement matching.

9) Find Missing Number
- Main logic: compare expected sum with actual sum, or use XOR.
- Common mistake: assuming the list is sorted or contains only one missing value.
- Overcome: validate constraints before choosing the formula.

10) Move Zeroes
- Main logic: keep non-zero values in front using a pointer.
- Common mistake: swapping too often and adding unnecessary complexity.
- Overcome: use a single write pointer and keep the logic linear.

11) Merge Sorted Arrays
- Main logic: merge with two pointers and append leftovers.
- Common mistake: using costly concatenation in a loop.
- Overcome: merge in one pass with O(n + m) efficiency.

12) Second Largest Number
- Main logic: track the largest and second-largest values in one pass.
- Common mistake: not handling duplicates or very small input properly.
- Overcome: initialize carefully and test edge cases like [1, 1, 1].

13) Maximum Subarray Sum
- Main logic: Kadane's algorithm keeps the best current sum.
- Common mistake: assuming the answer must include the first element.
- Overcome: update current sum as max(current_value, current_sum + value).

14) Binary Search
- Main logic: repeatedly halve the search space.
- Common mistake: using the wrong mid or forgetting the boundary condition.
- Overcome: define left/right clearly and keep the loop invariant in mind.

15) Valid Parentheses
- Main logic: use a stack to match opening and closing brackets.
- Common mistake: not checking empty stack before popping.
- Overcome: treat the stack as the source of truth for unmatched elements.

16) Group Anagrams
- Main logic: sort each word and group by the same sorted key.
- Common mistake: using raw strings as keys without normalization.
- Overcome: use a canonical representation like sorted characters.

17) Rotate Array
- Main logic: shift elements by k using slicing or reversal.
- Common mistake: confusing left rotation with right rotation.
- Overcome: write down the expected position change before coding.

18) Find Duplicate Elements
- Main logic: count values or use a set for repeated entries.
- Common mistake: adding duplicates to the result multiple times.
- Overcome: store duplicates in a set or count frequencies once.

19) Count Word Frequency
- Main logic: split the sentence and count each word.
- Common mistake: ignoring punctuation and case differences.
- Overcome: normalize text before counting.

20) Top K Frequent Elements
- Main logic: count frequencies and select the highest counts.
- Common mistake: using a complex sort when Counter is enough.
- Overcome: prefer built-in collections for clarity and speed.

21) JSON Parsing
- Main logic: read and decode JSON into Python objects.
- Common mistake: assuming the file format is always valid.
- Overcome: handle FileNotFoundError and JSONDecodeError gracefully.

22) Compare Two JSONs
- Main logic: parse both payloads and compare structure and values.
- Common mistake: comparing raw strings instead of parsed objects.
- Overcome: normalize and compare dictionaries/lists logically.

23) Log File Analysis
- Main logic: parse lines, extract fields, and count or group them.
- Common mistake: treating logs as plain text without structure.
- Overcome: split by delimiters and use regex only where necessary.

24) API Response Validation
- Main logic: verify that expected keys and value types exist.
- Common mistake: assuming the response is always complete.
- Overcome: define a schema and validate required fields early.

25) Test Result Aggregation
- Main logic: group results by test case, status, or execution date.
- Common mistake: mixing up aggregation with filtering.
- Overcome: decide first whether you need counts, summaries, or detailed records.

Engineering mindset:
- Look for the simplest pattern first: two pointers, hash maps, stacks, or sorting.
- Always test edge cases: empty input, duplicates, single-element input, and invalid data.
- Write code that is easy to read, not just clever.
"""

# Code-Practice0-Session

# Code-1
def reverse_string_problem(s):
    rev_str = ""
    for char in s:
        rev_str = char + rev_str
    return rev_str

s = "Ganesh Malepati"
print(reverse_string_problem(s))


# Code-2
def palindrome_of_string_problem(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

s = "Ganesh"
test_s = "malayalam"
print(palindrome_of_string_problem(s))
print(palindrome_of_string_problem(test_s))


# Code-3
def caseinsensitive_palidrome_problem(s):
    new_s = ''.join(char.lower() for char in s if char.isalnum())
    left = 0
    right = len(new_s)-1
    while left < right:
        if new_s[left] != new_s[right]:
            return False
        left += 1
        right -= 1
    return True


s = "12 A man, a plan, a canal: Panama 21"
print(caseinsensitive_palidrome_problem(s))


# Code-4
def check_anagrams(agms1, agms2):
    if len(agms1) != len(agms2):
        return False
    freq = {}
    for i in agms1:
        freq[i] = freq.get(i, 0) + 1
    for i in agms2:
        if i not in freq or freq[i] == 0:
            return False
        freq[i] -= 1
    return True

agms1 = "listen"
agms2 = "silent"
check_1 = "top"
check_2 = "mop"
print(check_anagrams(agms1, agms2))
print(check_anagrams(check_1, check_2))


# Code-5
def first_non_repeat_character(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char in freq:
        if freq[char] == 1:
            return char

s = "swiss"
print(first_non_repeat_character(s))


# Code-6
def longest_substring_without_repeat_characters(s):
    max_len = 0
    left = 0
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

    longest_sub_string = s[start:start + max_len]
    return max_len, longest_sub_string

s = "abccaadbbcabcbdcce"
print(longest_substring_without_repeat_characters(s))


# Code-7
def character_freq_count(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

s = "Ganesh Malepati"
print(character_freq_count(s))


# Code-8
def remove_duplicate_from_string(s):
    seen = set()
    res = []
    for char in s:
         if char not in seen:
             seen.add(char)
             res.append(char)
    return ''.join(res), res

s = "banana"
print(remove_duplicate_from_string(s))


# Code-9
def two_sum_approach_1(data, target):
    freq = {}
    for idx, val in enumerate(data):
        complement = target - val
        if complement in freq:
            return [freq[complement], idx]
        freq[val] = idx
    return []

data = [23,45,59,4,34,25,56,46,86]
target = 102
print(two_sum_approach_1(data, target))


# Code-10
def find_missing_number(nums):
    n = max(nums)
    actual = sum(nums)
    expected = n * (n+1) // 2
    return expected - actual

nums = [1,2,3,4,5,6,7,9,10]
print(find_missing_number(nums))


# Code-11
def move_zeros_end(nums):
    zero_position = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero_position], nums[i] = nums[i], nums[zero_position]
            zero_position += 1
    return nums

nums = [23,0,1,2,44,30,0,4,3,0,25,0,7,73,0,23,50,63,0]
print(move_zeros_end(nums))


# Code-12
def merge_two_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    res.extend(arr1[i:])
    res.extend(arr2[j:])

    return res

arr1 = [23, 34, 45, 65, 76, 89]
arr2 = [34, 67, 78, 89, 93, 99]
print(merge_two_sorted_arrays(arr1, arr2))


# Code-13
def second_largest_number(nums):
    first_largest = second_largest = float('-inf')
    for i in nums:
        if i > first_largest:
            first_largest, second_largest = i, first_largest
        elif first_largest > i > second_largest:
            second_largest = i
    return second_largest

nums = [2353, 34243, 3453, 23424, 3453, 3452, 6346, 7457, 7476, 85865, 587976, 4535, 457457, 587585, 85685, 69679, 6969]
print(second_largest_number(nums))


# Code-14
def maximum_subarray_sum(arr):
    if not arr:
        return 0
    curr_sum = arr[0]
    max_sum = arr[0]
    for i in range(1, len(arr)):
        curr_sum = max(arr[i], arr[i] + curr_sum)
        max_sum = max(curr_sum, max_sum)
    return max_sum

arr = [2,3,-8,7,-1,2,3]
print(maximum_subarray_sum(arr))


# Code-15
def Binary_search(arr, target):
    arr.sort()
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [12, 14, 5, 15, 17, 45, 34, 64, 26, 48, 59, 36, 85, 35, 44, 32, 62, 56, 85, 89]
print(Binary_search(arr, target=59))


# Code-16 
def valid_Parentheses(data):
    result = []
    map = {
        ")":"(",
        "}":"{",
        "]":"["
    }
    for char in data:
        if char in "([{":
            result.append(char)
        else:
            if not result:
                return False
            top = result.pop()
            if top != map[char]:
                return False
    return len(result) == 0

data = "{[[(([{()}]))]]}"
print(valid_Parentheses(data))


# Code-17
def group_anagrams(agms):
    freq = {}
    for i in agms:
        key = ''.join(sorted(i))
        if key in freq:
            freq[key].append(i)
        else:
            freq[key] = [i]
    return freq

agms_data = ["eat", "ate", "tan", "tea", "nat", "bat", "listen", "silent", "tab", "bat", "fan"]
print(group_anagrams(agms_data))


# Code-18
"""
Right Rotation

1 2 3 4 5

↓

5 1 2 3 4

Left Rotation
1 2 3 4 5

↓

2 3 4 5 1

"""
def rotate_array(arr, k):                   # First values move to last right rotation
    n = len(arr)
    k = k%n
    return arr[k:] + arr[:k]

arr = [23,34,45,56,67,78,89]
print(rotate_array(arr, k=1))

def rotate_array(arr, k):                   # last elements moves to first left rotation
    n = len(arr)-1
    k = k%n
    return arr[-k:] + arr[:-k]

arr = [23,34,45,56,67,78,89]
print(rotate_array(arr, k=2))


# Code-19
def find_duplicate_elements(arr):
    duplicates = {}
    result = []
    for i in arr:
        duplicates[i] = duplicates.get(i, 0) + 1
    for key, val in duplicates.items():
        if val > 1:
            result.append(key)
    return result

arr = [1,2,3,1,1,2,3,2,5,3,2,5,6,4,7,3,8,5,8,4,7,4,8,4,8,9]
print(find_duplicate_elements(arr))

def find_duplicate_elements(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

arr = [1,2,3,2,4,5,1]
print(find_duplicate_elements(arr))


# Code-20
def count_word_frequency(sent):
    sentence = sent.split()
    freq = {}
    for word in sentence:
        freq[word] = freq.get(word, 0) + 1
    return freq

sent = "Today, I need to complete the pytest and API Automation concepts."
print(count_word_frequency(sent))


# Code-21
from collections import Counter
def top_k_frequent_elements(arr, k):
    count = Counter(arr)
    return [num for num in count.most_common(k)]

arr = [5,1,2,1,5,2,3,4,3,2,3,4,3,5,6,7,4,7,5,3,7,8,9,6,5,4,5,4,5]
print(top_k_frequent_elements(arr, k=4))


# Code-22
import json
def json_parsing_problem():
    with open('response1.json') as file:
        result = json.load(file)
    return result

print(json_parsing_problem())


data = '''
{
    "name":"Ganesh",
    "age":24,
    "city":"Hyderabad"
}
'''

result = json.loads(data)

print(result)
print(type(result))


# Code-22-Compare Two JSON Values

import json 

with open('expected.json') as file:
    json1 = json.load(file)

with open('actual.json')as file:
    json2 = json.load(file)

for key in json1:
    if json1.get(key) != json2.get(key):
        print(f"Key: {key}")

        print(f"JSON1: {json1.get(key)}")
        print(f"JSON2: {json2.get(key)}")



with open('response1.json') as file:
    json1 = json.load(file)

with open('response2.json')as file:
    json2 = json.load(file)

for key in json1:
    if json1.get(key) != json2.get(key):
        print(f"Key: {key}")

        print(f"JSON1: {json1.get(key)}")
        print(f"JSON2: {json2.get(key)}")

