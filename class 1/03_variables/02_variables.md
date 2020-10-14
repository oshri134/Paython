## Variables

Variables are easy to understand. They simply **point to values**.

```python
>>> a = 1   # create a variable called a that points to 1
>>> b = 2   # create another variable
>>> a       # get the value that the variable points to
1
>>> b
2
>>>
```
We can also change the value of a variable after setting it.

```python
>>> a = 2    # make a point to 2 instead of 1
>>> a
2
>>>
```

Setting a variable to another variable gets the value of the other
variable and sets the first variable to point to that value.

```python
>>> a = 1
>>> b = a  # this makes b point to 1, not a
>>> a = 5
>>> b      # b didn't change when a changed
1
>>>
```

Trying to access a variable that is not defined creates an error
message.

```python
>>> thingy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'thingy' is not defined
>>>
```

Variables are simple to understand, but there are a few details that we
need to keep in mind:

- Multiple variables can point to the same value, but one variable
  cannot point to multiple values.


Variables are an important part of most programming languages, and they
allow programmers to write much larger programs than they could write
without variables.

Variable names are case-sensitive, like many other things in Python.

```python
>>> thing = 1
>>> THING = 2
>>> thIng = 3
>>> thing
1
>>> THING
2
>>> thIng
3
>>>
```

There are also words that cannot be used as variable names
because they have a special meaning. They are called **keywords**, and
we can run `help('keywords')` to see the full list if we want to.
Trying to use a keyword as a variable name causes a syntax error.

```python
>>> if = 123
  File "<stdin>", line 1
    if = 123
       ^
SyntaxError: invalid syntax
>>>
```

When assigning something to a variable using a `=`, the right side of
the `=` is always executed before the left side. This means that we can
do something with a variable on the right side, then assign the result
back to the same variable on the left side.

```python
>>> a = 1
>>> a = a + 1
>>> a
2
>>>
```
