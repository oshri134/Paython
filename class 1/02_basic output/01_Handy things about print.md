
## Handy things about print

We can also print an empty line by calling print without any
arguments.

```python
>>> print()

>>>
```

In Python, `\n` is a newline character. Printing a string that contains
a newline character also prints a newline:

```python
>>> print('hello\nworld')
hello
world
>>>
```

If we want to print a real backslash, we need to **escape** it by typing
two backslashes.
```python
    >>> print('hello\\nworld')
    hello\nworld
    >>>
```

We can also pass multiple arguments to the print function. We need to
separate them with commas and print will add spaces between them.

```python
>>> print("Hello", "World!")
Hello World!
>>>
```

Unlike with `+`, the arguments don't need to be strings.

```python
>>> print(42, "is an integer, and the value of pi is", 3.14)
42 is an integer, and the value of pi is 3.14
>>>
```
