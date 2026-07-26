"""
## Day 3 Recap — Dictionaries & Collections

### Dictionaries
- Dictionaries are hash tables: keys map to values with average O(1) lookup.
- Keys must be immutable and hashable; values can be anything.
- Important methods:
  - `get(key, default)` avoids `KeyError`
  - `items()` returns `(key, value)` pairs
  - `keys()` returns all keys
  - `values()` returns all values
  - `pop(key[, default])` removes and returns value
  - `popitem()` removes last inserted pair
  - `update(other)` merges another mapping
  - `setdefault(key, default)` inserts default if missing
  - `fromkeys(iterable, value=None)` builds a new dict from keys

### Core concepts
- Hashing
  - Dict performance relies on stable hashes
  - Most mistakes come from using mutable keys or assuming order before Python 3.7
- Dictionary comprehension
  - Clean, expressive construction:
    - `{k: v*2 for k, v in source.items() if condition}`
  - Best for transforming or filtering maps
- Nested dictionary
  - Useful for hierarchical data; access safely with `get()` or `defaultdict`
  - Common bug: `d['a']['b']` fails if intermediate key missing
  - Fix with `setdefault()` or `defaultdict(dict)`

### Collections module
- `Counter`
  - Best for frequency counts, top-K frequency, duplicate detection
  - Example: `Counter(text).most_common(3)`
- `defaultdict`
  - Simplifies nested structures and grouping
  - Example: `defaultdict(list)` avoids manual `if key not in d`
- `deque`
  - Use for efficient O(1) append/pop at both ends
  - Better than list for queues and sliding windows
- `OrderedDict`
  - Preserves insertion order in older Python versions; now mostly for specialized order-sensitive logic
- `namedtuple`
  - Immutable tuple with named fields; better readability than plain tuples

### Common pitfalls & fixes
- Using `dict[key]` instead of `get()`:
  - Bug: raises `KeyError`
  - Fix: `d.get(key, default)`
- Modifying dict while iterating:
  - Bug: runtime error or skipped entries
  - Fix: iterate over `list(d.items())` or copy keys first
- Mutable default values with `fromkeys()`:
  - Bug: `{}.fromkeys(keys, [])` shares one list object
  - Fix: use dict comprehension or `defaultdict(list)`
- Overcomplicating nested dict creation:
  - Use `defaultdict(dict)` or `setdefault()`
- Using `Counter` like a normal dict instead of `most_common`, `elements`, or `subtract`

### Interview practice focus
- Character frequency: use `Counter` or manual dict increment
- Word frequency: split text and count safely
- Group anagrams: normalize with sorted key or char-count tuple
- Most frequent character: `Counter.most_common(1)`
- Top K frequent elements: `Counter.most_common(k)` or heap
- First unique character: count then scan once
- Majority element: hash count or Boyer–Moore for O(n) time
- Duplicate finder: use dict/set to track seen items

### Professional engineer angle
- Think in terms of:
  - hashable key contracts
  - safe lookups
  - choosing dict vs list vs set based on access pattern
- Use `collections` for intent: `Counter` for frequency, `defaultdict` for grouping, `deque` for queue semantics
- Avoid mistakes by validating assumptions:
  - is the key present?
  - are keys immutable?
  - is data already ordered?
  - are you mutating during iteration?

This summary keeps the core Python interview patterns clear, highlights likely mistakes, and shows how to solve them in production-quality code.
"""

# Performing all methods using one dict example

my_dict = {
    "Name": "Ganesh Malepati",
    "Age": 25,
    "Gender": "Male",
    "Occupation": "IT-Employee",
    "Organization": "Capgemini",
    "Role": "SDET",
    "Salary": 26300
}

print(f"Original Dict: {my_dict}")


print(my_dict.get("Occupation"))
print(my_dict.get("Role"))

for key, val in my_dict.items():
    print(f"Key - {key} : Value - {val}")

for key in my_dict.keys():
    print(f"Keys: {key}")

for val in my_dict.values():
    print(f"Values: {val}")


my_dict.update({"Organization": "Amazon"})
print(my_dict)


# Codeing-Practice-Session

# Code-1

def character_frequency(data):
    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1
    
    return freq

data = "Ganesh Malepati"
print(character_frequency(data))
print("\n")


# Code-2

def word_frequency_sentence(sent):
    sentence = sent.split()
    freq = {}
    for word in sentence:
        freq[word] = freq.get(word, 0) + 1
    return freq

sent = "By next wednesday i need to complete full python ramp-up. This time i need to do a greater comeback than previous"
print(word_frequency_sentence(sent))
print("\n")


# Code-3

def group_anagrams(agms_data):
    freq = {}
    for word in agms_data:
        key = ''.join(sorted(word))
        if key in freq:
            freq[key].append(word)
        else:
            freq[key] = [word]
    return freq


agms_data = ["eat", "ate", "tan", "tea", "nat", "bat", "listen", "silent", "tab", "bat", "fan"]
print(group_anagrams(agms_data))


# Code-4

from collections import Counter
def most_frequent_character(data, k):
    count = Counter(data)
    return [num for num, freq in count.most_common(k)]

data = [1,2,4,3,4,1,2,3,2,1,2,4,3,2,1,4,2,3,4]
print(most_frequent_character(data, k=3))

    # Brut-force soultion

def most_frequent_elements_by_bruteforce_approach(data, k):
    freq = {}
    for i in data:
        freq[i] = freq.get(i, 0) + 1

    sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    result = []
    for key, val in sorted_items[:k]:
        result.append(key)

    return result

data = [1,2,4,3,4,1,2,3,2,1,2,4,3,2,1,4,2,3,4]
print(most_frequent_elements_by_bruteforce_approach(data, k=1))