"""
    ## Interview Coding Patterns – Complete Guide

    These patterns are common because many interview problems are built from the same core idea. If you learn the pattern, you can solve many different questions more quickly.

    ---

    ## 1. HashMap Pattern

    ### What it is
    A HashMap stores data as key-value pairs. It gives very fast lookup, insertion, and deletion, usually in average time $O(1)$.

    ### Why it is useful
    It is ideal when you need to:
    - count frequencies
    - check whether something already exists
    - map one value to another
    - group items by a property

    ### Core idea
    Instead of scanning everything repeatedly, store information as you go and retrieve it immediately.

    ### Common problems
    - Two Sum
    - Find two numbers that add up to a target.
    - Use a map to store seen numbers and look for the complement.
    - Character frequency
    - Count how many times each character appears.
    - Word frequency
    - Count how many times each word appears in a sentence or list.
    - Group anagrams
    - Group words that contain the same letters but in different order.
    - Use a normalized key such as sorted letters.
    - Top K frequent
    - Find the most repeated elements.
    - Count frequency first, then sort or use a heap.

    ### Interview takeaway
    If the problem mentions “find a pair”, “count”, “group”, or “map”, HashMap is often the first pattern to think about.

    ---

    ## 2. Two Pointer Pattern

    ### What it is
    Two Pointer means using two indices to scan data from different positions, usually from both ends or in a coordinated way.

    ### Why it is useful
    It helps solve problems efficiently without using extra space, often in $O(n)$ time.

    ### Core idea
    You move the pointers based on a condition and reduce the search space step by step.

    ### Common problems
    - Reverse string
    - Use one pointer at the start and one at the end.
    - Swap values until they meet.
    - Palindrome
    - Compare characters from both ends.
    - Remove duplicates
    - Move one pointer to scan and another to write unique values.
    - Merge arrays
    - Merge two sorted arrays by comparing values from the end or start.

    ### Interview takeaway
    Use Two Pointers when the data is linear, ordered, or can be compared from opposite sides.

    ---

    ## 3. Sliding Window Pattern

    ### What it is
    Sliding Window is used for problems involving contiguous subarrays or substrings. You keep a window and move its boundaries to the right.

    ### Why it is useful
    It avoids recomputing everything from scratch each time. Instead, you update the window incrementally.

    ### Core idea
    Keep a window that satisfies some condition, then expand or shrink it while maintaining useful information like sum, count, or frequency.

    ### Common problems
    - Longest substring
    - Find the longest substring that satisfies a condition (for example, unique characters).
    - Maximum sum subarray
    - Find the subarray with the largest sum.
    - Minimum window substring
    - Find the smallest substring containing all required characters.

    ### Interview takeaway
    Use Sliding Window when the problem is about “contiguous elements” and you need a subarray or substring with some property.

    ---

    ## 4. Heap Pattern

    ### What it is
    A Heap is a special tree-based structure that gives quick access to the smallest or largest element. In Python, this is usually implemented with a min-heap or max-heap.

    ### Why it is useful
    It is perfect for problems involving:
    - smallest/largest values
    - top K results
    - priority-based processing

    ### Core idea
    Instead of sorting everything, keep only the most important elements in the heap.

    ### Common problems
    - Kth largest
    - Keep a heap of size $k$.
    - Top K elements
    - Maintain the largest or smallest K values.
    - Merge K lists
    - Understand the idea of repeatedly taking the smallest current element from multiple sorted lists.

    ### Interview takeaway
    Use a Heap when the problem asks for “top K”, “kth largest”, or “best item first”.

    ---

    ## 5. Stack Pattern

    ### What it is
    A Stack follows Last In, First Out (LIFO). The last inserted element is removed first.

    ### Why it is useful
    It is excellent for problems involving:
    - matching pairs
    - nesting
    - previous/next greater values
    - reversing order

    ### Core idea
    When you see a structure that depends on the most recent item, stack is often the right choice.

    ### Common problems
    - Valid parentheses
    - Push opening brackets and pop when you see a closing one.
    - Reverse string
    - Push characters and then pop them back out.
    - Next greater element
    - Use a stack to keep track of previous values.

    ### Interview takeaway
    Use a Stack when the problem involves nesting, matching, or tracking previous elements in a LIFO way.

    ---

    ## 6. Queue / Deque Pattern

    ### What it is
    A Queue follows First In, First Out (FIFO). A Deque supports insertion and removal from both ends.

    ### Why it is useful
    It is useful when you need:
    - ordering by arrival time
    - breadth-first traversal
    - sliding window maximum problems

    ### Core idea
    A queue processes items in the order they arrive, which is useful for level-wise traversal and streaming data.

    ### Common problems
    - Sliding window maximum
    - Use a deque to maintain candidates for the current window.
    - BFS basics
    - Traverse graphs or trees level by level.

    ### Interview takeaway
    Use Queue/Deque for processing items in order and for problems that need the earliest or latest element quickly.

    ---

    ## Quick Comparison

    - HashMap: best for counting, mapping, and grouping
    - Two Pointers: best for linear arrays and in-place problems
    - Sliding Window: best for contiguous subarrays/substrings
    - Heap: best for top K and priority-based problems
    - Stack: best for nesting, matching, and reverse-order logic
    - Queue/Deque: best for order-based processing and BFS

    ---

    ## Best Way to Study These Patterns

    1. Learn the pattern idea first.
    2. Solve 3–5 problems from that pattern.
    3. Notice the repeated structure.
    4. Practice identifying the pattern from the problem statement.

    > In interviews, the real skill is not memorizing one solution, but recognizing the pattern quickly.

    If you want, I can next give you:
    - a one-page revision sheet for these patterns, or
    - solved examples for each problem in Python.

"""


# Code-Practice-Session "HashMap Pattern"

# Code-1

def two_sum_problem(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return [i, j]

arr = [34,56,45,77,2,57,89,686,5575,864,6474,454,3435,567,3463,463,567,67]
target = 3480
print(two_sum_problem(arr, target))


def two_sum_optimized(arr, target):
    result = {}
    for idx, val in enumerate(arr):
        complement = target - val
        if complement in  result:
            return [result[complement], idx]
        result[val] = idx
    return []


arr = [34,56,45,77,2,57,89,686,5575,864,6474,454,3435,567,3463,463,567,67]
target = 1140
print(two_sum_optimized(arr, target))



# Code-2

def character_frequency(name):
    res = {}
    for char in name:
        res[char] = res.get(char, 0) + 1
    return res

name = "Malepati Ganesh"
print(character_frequency(name))


# Code-3

def word_frequency(sent):
    sentence = sent.split()
    freq = {}
    for word in sentence:
        freq[word] = freq.get(word, 0) + 1
    return freq

sent = "Why are not able to remember the two sum problem technique, make a note of it, try to understand now"
print(word_frequency(sent))


# Code-4

def group_anagrams(data):
    freq_group = {}
    for word in data:
        key = ''.join(sorted(word))
        if key in freq_group:
            freq_group[key].append(word)
        else:
            freq_group[key] = [word]

    return freq_group

agms_data = ["eat", "ate", "tan", "tea", "nat", "bat", "listen", "silent", "tab", "bat", "fan"]
print(group_anagrams(agms_data))



# Code-5

from collections import Counter
def top_k_frequent_elements(arr, k):
    res = Counter(arr)
    return [num for num in res.most_common(k)]

arr = [1,2,4,3,4,1,2,3,2,1,2,4,3,2,1,4,2,3,4]
print(top_k_frequent_elements(arr, k=3))


# Code-Practice-Session "Two Pointer"

# Code-1

def reverse_string(name):
    rev_str = ""
    for char in name:
        rev_str = char + rev_str
    return rev_str

name = "Ganesh Malepati"
print(reverse_string(name))

# Code-2

def palindrome_of_string(data):
    left = 0
    right = len(data)-1
    while left < right:
        if data[left] != data[right]:
            return False
        left += 1
        right -= 1

    return True

data = "ganesh"
test_data_1 = "malayalam"
test_data_2 = "Radar"
print(palindrome_of_string(data))
print(palindrome_of_string(test_data_1))
print(palindrome_of_string(test_data_2))


# Code-3

def remove_duplicates(data):
    """Remove duplicates while keeping the first occurrence order."""
    seen = set()
    res = []
    for item in data:
        if item not in seen:
            seen.add(item)
            res.append(item)
    return res

# It works for lists
numbers = [1, 2, 2, 3, 3, 4, 4, 5]
print(remove_duplicates(numbers))

# It also works for strings because a string is an iterable of characters
word = "banana"
print(remove_duplicates(word))

# If you want a string back from string input, join the result
print("".join(remove_duplicates(word)))


# Code-4

def merge_arrays(arr1, arr2):
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

arr1 = [1,3,5,7]
arr2 = [2,4,6,8]
print(merge_arrays(arr1, arr2))


# Code-Practice-Session "Sliding Window"

# Code-1

def longest_substring(s):
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
    lon_sub_s = s[start: start + max_len]
    return max_len, lon_sub_s

s = "abccaadbbcabcbdcce"
print(longest_substring(s))

            


