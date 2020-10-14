## None
None is Python's "nothing" value. It behaves just like any other value,
and it's often used as a default value for different kinds of things.
Right now it might seem useless but we'll find a bunch of ways to use
None later.

None's behavior on the interactive prompt might be a bit confusing at
first:

```python
>>> thingy = None
>>> thingy
>>>
```

Typing `thingy` didn't echo back None.
This is because the prompt never echoes back None. 

If we want to see a None on the interactive prompt, we can use print.

```python
>>> print(thingy)
None
>>>
```
