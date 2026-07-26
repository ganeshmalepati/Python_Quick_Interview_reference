"""
    **Day 5 — File Handling, JSON & Python Modules (Concise Recap for Engineers)**

    - **Scope**: File modes, context managers, JSON/CSV APIs, key stdlib modules, common mistakes, and focused practice problems with hints.

    **File Handling**
    - **Modes**: `r`: read, `w`: write (truncate), `a`: append, `x`: create-only (fails if exists).
    - **Encoding**: Always specify `encoding='utf-8'` for text files to avoid cross-platform bugs.
    - **Binary vs text**: Use `'rb'/'wb'` for binary (images, protobuf), text modes for strings.
    - **Context manager**: `with open(path, mode, encoding=...) as f:` ensures deterministic close and resource cleanup.
    - **Large files**: Iterate line-by-line (`for line in f:`) or use `f.readline()`/`f.read(size)` to avoid memory spikes.
    - **Atomic writes**: Write to a temp file and `os.replace()` to avoid partial writes on crash.

    **JSON**
    - **APIs**:
    - `json.load(fp)` — parse from file object
    - `json.loads(s)` — parse from string
    - `json.dump(obj, fp, indent=2)` — write to file
    - `json.dumps(obj)` — to string
    - **Common pitfalls**:
    - Non-serializable objects (datetime, bytes): convert explicitly (ISO strings) or provide `default=` handler.
    - Relying on key order: since Py3.7 insertion order preserved, but don't depend on it for semantics unless documented.
    - **Tips**: Validate with schema (jsonschema) for API contracts; use streaming parsers (`ijson`) for huge JSON.

    **CSV**
    - **Reading/Writing**: use the `csv` module (`csv.reader`, `csv.DictReader`, `csv.writer`, `csv.DictWriter`) to handle quoting and delimiters safely.
    - **Pitfalls**:
    - Newline/encoding issues: open with `newline=''` and `encoding='utf-8'`.
    - Mixed delimiters or inconsistent columns: validate header and row lengths; prefer `DictReader` for robust access.
    - **When to use**: CSV for simple tabular exchange; prefer `parquet`/binary formats for large datasets and schema guarantees.

    **Useful Modules & Typical Functions**
    - **os / pathlib**: `os.path.exists`, `os.replace`, `pathlib.Path()` for robust path manipulation.
    - **sys**: `sys.argv`, `sys.exit`, `sys.stdin/stdout` for CLI tools.
    - **math / random / datetime / re**: common helpers — `math.ceil`, `random.Random`, `datetime.fromisoformat`, `re.compile`.
    - **heapq**: `nlargest`, `nsmallest`, `heappush/heappop` for top-k and priority queues.
    - **collections**: `Counter`, `defaultdict`, `deque`, `namedtuple` for idiomatic data structures.
    - **itertools**: `groupby`, `chain`, `islice`, `combinations` for iterator algebra and memory-efficient pipelines.
    - **json / csv / gzip / bz2 / zipfile**: serialization + compression helpers.

    **Common Mistakes & Fixes**
    - **Forgetting `encoding`**: leads to silent corruption—always set `encoding='utf-8'`.
    - **Using `open(..., 'w')` on existing file without backup**: use `x` or write to temp + `os.replace()`.
    - **Mutating objects before `json.dump()`**: ensure snapshot semantics or serialize copies to avoid race conditions.
    - **Parsing CSV with simple `split(',')`**: fails on quoted commas—use `csv` module.
    - **Comparing JSONs by string**: use parsed objects and compare with normalized keys or use deep-diff tools.
    - **Loading large JSON into memory**: use streaming (`ijson`) or process in chunks.

    **Practice Problems — Short Hints**
    - **Count words in file**: stream file, `re.findall(r'\w+', line.lower())`, `Counter.update(...)`.
    - **Parse logs**: compile a `re` with named groups, parse line-by-line, write structured JSON or DB rows.
    - **Read CSV**: use `csv.DictReader`, validate headers, convert types explicitly.
    - **Compare JSONs**: `json.load()` both, then use recursive comparison (consider ignoring ordering or timestamps).
    - **Flatten nested JSON**: recursive walk producing dotted keys (`parent.child`) or use libraries like `flatten_json`.
    - **Extract API fields**: validate with schema; use `dict.get()` with defaults and map missing fields to errors.

    **Quick Examples (conceptual)**
    - Safe file write:
    - `with open(tmp, 'w', encoding='utf-8') as f: json.dump(obj, f); os.replace(tmp, final)`
    - Count words:
    - `from collections import Counter` then stream update: `c.update(re.findall(r'\w+', line.lower()))`

    Would you like a one-file runnable `examples.py` that demonstrates these patterns (safe write, word count, CSV read, JSON compare)? If yes, I can add it to the workspace.



    
    **Day 5: File Handling, JSON, and Python Modules**

    ### File Handling

    File handling is a crucial aspect of programming, and Python provides several modes to interact with files:

    *   **r (read)**: Opens a file for reading. If the file does not exist, it raises a `FileNotFoundError`.
    *   **w (write)**: Opens a file for writing. If the file exists, its content is truncated. If the file does not exist, it is created.
    *   **a (append)**: Opens a file for appending. If the file does not exist, it is created.
    *   **x (create)**: Opens a file for exclusive creation. If the file exists, it raises a `FileExistsError`.

    **Common Mistake:** Not closing files after use, which can lead to file descriptor leaks.

    **Solution:** Use the `with open()` context manager, which automatically closes the file when you're done with it.

    **Example:**
    ```python
    with open('example.txt', 'r') as file:
        content = file.read()
    ```

    ### JSON

    JSON (JavaScript Object Notation) is a lightweight data interchange format.

    *   **json.load()**: Loads JSON data from a file.
    *   **json.loads()**: Loads JSON data from a string.
    *   **json.dump()**: Dumps JSON data to a file.
    *   **json.dumps()**: Dumps JSON data to a string.

    **Common Mistake:** Not handling JSON decoding errors.

    **Solution:** Use try-except blocks to catch `JSONDecodeError` exceptions.

    **Example:**
    ```python
    import json

    try:
        with open('example.json', 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    ```

    ### CSV

    CSV (Comma Separated Values) is a file format used for tabular data.

    *   **Read**: Use the `csv` module to read CSV files.
    *   **Write**: Use the `csv` module to write CSV files.

    **Common Mistake:** Not handling CSV quoting and escaping correctly.

    **Solution:** Use the `csv` module's built-in quoting and escaping mechanisms.

    **Example:**
    ```python
    import csv

    with open('example.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    ```

    Module Cheat Sheet
        Module	    Most Used Functions	                        Common Use Cases
        os	        listdir, mkdir, remove, rename	            File operations
        pathlib	    Path, exists, glob, iterdir	                Modern path handling
        sys	        argv, exit, path, version	                Runtime information
        math	    sqrt, ceil, floor, factorial	            Mathematical operations
        random	    randint, choice, shuffle                    Test data generation
        datetime	now, strftime, timedelta	                Date and time manipulation
        re	        search, findall, sub, compile	            Pattern matching
        heapq	    heappush, heappop, heapify	                Priority queues
        collections	Counter, defaultdict, deque	                Efficient data structures
        itertools	product, permutations, combinations, chain	Iterator utilities

"""

# Practice-Code


def count_words_in_files(file_name):
    word_count = {}
    with open(file_name, "r") as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    return word_count

result = count_words_in_files("MCP_Document_Reference.txt")
print(result)



# def parse_logs(filename):

#     log_levels = {}

#     with open(filename, "r") as file:

#         for line in file:

#             parts = line.strip().split()

#             if len(parts) < 3:
#                 continue

#             level = parts[2]

#             log_levels[level] = log_levels.get(level, 0) + 1

#     return log_levels


# result = parse_logs("application.log")

# print(result)


# Compare Two JSON responses

print("\n")

import json

with open("response1.json") as file:
    json1 = json.load(file)

with open("response2.json") as file:
    json2 = json.load(file)

for key in json1:
    if json1.get(key) != json2.get(key):
        print(f"{key}")
        
        print(f"JSON1: {json1.get(key)}")

        print(f"JSON2: {json2.get(key)}")

        print("JSON1:", json1.get(key))

        print("JSON2:", json2.get(key))

        print()




