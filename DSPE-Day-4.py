"""
    ## Day 4 Recap — Functions, OOPs & Exceptions

    ### Functions
    - Functions package behavior and improve reuse.
    - Arguments:
    - positional: order matters
    - keyword: explicit names, improves readability
    - default: safe defaults, avoid mutable default values
    - `*args` collects extra positional args as a tuple
    - `**kwargs` collects extra keyword args as a dict
    - `lambda` is a small anonymous function for simple inline logic
    - `map(func, iterable)` applies a function to every element
    - `filter(func, iterable)` keeps elements where func returns `True`
    - `reduce(func, iterable)` folds values into one result
    - Recursion:
    - solve problems by calling the same function
    - common patterns: factorial, Fibonacci, tree traversal
    - watch recursion depth and prefer iteration when recursion adds no clarity

    ### OOP
    - Class: blueprint for objects
    - Object: instance of a class
    - Constructor: `__init__` initializes instance state
    - Instance variables: per-object state
    - Class variables: shared across all instances
    - Encapsulation: keep data and behavior together, use private/protected naming for internal state
    - Inheritance: reuse and extend base class behavior
    - Polymorphism: same interface, different implementations
    - Abstraction: expose what matters, hide internal complexity
    - Method overriding: child class replaces parent behavior

    Example angles:
    - SDET/framework design: use classes for reusable test data models, page objects, and reusable fixtures
    - Encapsulation: avoid exposing internals directly, use getters/setters or properties
    - Inheritance vs composition: prefer composition when behavior is orthogonal

    ### Exception Handling
    - `try`: run code that may fail
    - `except`: handle specific exceptions
    - `finally`: cleanup code always executed
    - `raise`: explicitly throw errors
    - `assert`: internal sanity checks during development

    Common bug patterns:
    - Catching broad exceptions (`except Exception:`) hides real problems
    - Using `assert` for runtime validation in production
    - Forgetting `finally` cleanup for resources like files, network sockets, and DB connections
    - Raising wrong exception types or losing context

    ### Most common mistakes & how to overcome
    - Mutable default args:
    - Bug: `def f(x=[]): ...`
    - Fix: use `None` and initialize inside
    - Misusing `*args`/`**kwargs`:
    - Bug: wrong order or passing dict incorrectly
    - Fix: keep `*args` before `**kwargs`, use explicit keywords when needed
    - Lambda overload:
    - Bug: complex lambda hurts readability
    - Fix: use a named function if logic is more than one expression
    - Recursion without base case:
    - Bug: infinite recursion / stack overflow
    - Fix: always define and test the stopping condition first
    - Mutable vs immutable class vars:
    - Bug: shared list/dict across instances
    - Fix: initialize mutable state in `__init__` for instance-specific data
    - Inheritance abuse:
    - Bug: deep class hierarchies or using inheritance for unrelated behavior
    - Fix: prefer composition and keep interfaces narrow
    - Generic exception handling:
    - Bug: silencing `ValueError`, `TypeError`, etc.
    - Fix: catch specific exceptions and log context

    ### Practice focus
    - `Employee`, `Bank`, `Student`, `Rectangle`, `Car`
    - Model state with instance vars, behavior with methods
    - Use constructors to set required fields
    - Show polymorphism with overridden methods
    - Use exception handling for invalid input or illegal operations

    ### Daily recap summary
    - Functions: argument forms, `*args`/`**kwargs`, lambdas, functional utilities, recursion safety
    - OOP: classes/objects, constructor and variable scope, encapsulation, inheritance, polymorphism, abstraction
    - Exceptions: `try/except/finally`, `raise`, `assert`, and correct error handling
    - Engineers should focus on clean interface design, avoiding shared mutable state, explicit exception cases, and choosing recursion only when it improves clarity.
"""


def positional_args_add(a, b):          # Postion of args matters here or else concludes different outputs
    return a + b

print(positional_args_add(10, 30))
print(positional_args_add(40, 10))


# Keyword Arguments
def keyword_args_add(a, b):          # Order no longer matters.
    return a + b

print(keyword_args_add(23252, 2534554))


# Default Arguments
def default_args_add(name, place="Bengaluru"):      # If the second argument is omitted, the default value is used.
    return name, place

print(default_args_add("Ganesh"))


# Variable-Length Arguments
def arguments(*args):                               # Used when the number of positional arguments is unknown.
    return args

print(arguments(10,20,30,40))


# Keyword Variable Arguments (**kwargs)
def keyword_var_argurments(**kargs):                # Accepts an unknown number of keyword arguments.
    for key, val in kargs.items():
        print(f"{key}: {val}")
    
    # second method
    return kargs

keyword_var_argurments(name="Ganesh", place="Proddature", Age=25)
print(keyword_var_argurments(name="Ganesh", place="Proddature", Age=25))


# Combining both args and kargs

"""
    Difference Between *args and **kwargs

    *args	                **kwargs
    Positional arguments	Keyword arguments
    Stored as tuple	        Stored as dictionary
    Access by index     	Access by key
"""

def club_of_args_kargs(*args, **kargs):
    for i in args:
        print(i)
    
    for key, val in kargs.items():
        print(f"{key} : {val}")

club_of_args_kargs(10,30,460,45,name="Malepati Ganesh", Age=25, Place="Proddatur")



# Lambda function
"""
    Useful when passing small functions to higher-order functions.
    map():-    Applies a function to every element.
    filter();- Keeps only elements satisfying a condition.
    reduce():- Reduces an iterable into a single value.

    Prefer built-in functions (sum, max, min) where applicable. Use reduce() only when it clearly improves readability.

"""

res = lambda x: x*x
print(res(81))

data = [3,6,8,45,34,24,454,6565,4]
squa = list(map(lambda x: x*x, data))
print(squa)

data = [3,6,8,45,34,24,454,6565,4]
result = list(filter(lambda x: x%2==0, data))
print(result)

from functools import reduce
data = [3,6,8,45,34,24,454,6565,4]
result = reduce(lambda x,y: x+y, data)
print(result)


# Part-2 OOPs Concepts

