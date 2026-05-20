---
title: "Python return styles"
date: 2023-09-19T18:15:20+12:00
slug: "python-return-styles"
categories:
  - "Python"
  - "Work"
---
I was reading through the [charmed tech ops code](https://github.com/canonical/operator) today and noticed a bunch of code [like](https://github.com/canonical/operator/blob/c4e3266a6568ba310064ca8b9bff7adb89676224/ops/model.py#L912):

```
def f():
    if check:
        return val
    else:
        return None
```

I don't particularly love this (although I do feel you should match the style of an existing code base and should avoid changes that don't meet a reasonable level of value-add). I would generally leave out the `else` (and dedent the second `return`). It seemed likely that these generate the same opcodes so this is purely about readability, but it was worth checking that:

```
>>> def f1(a):
...   if a == 1:
...     return 'A'
...   else:
...     return None
... 
>>> def f2(a):
...   if a == 1:
...     return 'A'
...   return None
... 
>>> def f3(a):
...   return 'A' if a == 1 else None
... 
>>> def f4(a):
...   if a == 1:
...     return 'A'
... 
>>> dis.dis(f1)
  1           0 RESUME                   0
  2           2 LOAD_FAST                0 (a)
              4 LOAD_CONST               1 (1)
              6 COMPARE_OP               2 (==)
             12 POP_JUMP_FORWARD_IF_FALSE     2 (to 18)
  3          14 LOAD_CONST               2 ('A')
             16 RETURN_VALUE
  5     >>   18 LOAD_CONST               0 (None)
             20 RETURN_VALUE
>>> dis.dis(f2)
  1           0 RESUME                   0
  2           2 LOAD_FAST                0 (a)
              4 LOAD_CONST               1 (1)
              6 COMPARE_OP               2 (==)
             12 POP_JUMP_FORWARD_IF_FALSE     2 (to 18)
  3          14 LOAD_CONST               2 ('A')
             16 RETURN_VALUE
  4     >>   18 LOAD_CONST               0 (None)
             20 RETURN_VALUE
>>> dis.dis(f3)
  1           0 RESUME                   0
  2           2 LOAD_FAST                0 (a)
              4 LOAD_CONST               1 (1)
              6 COMPARE_OP               2 (==)
             12 POP_JUMP_FORWARD_IF_FALSE     2 (to 18)
             14 LOAD_CONST               2 ('A')
             16 JUMP_FORWARD             1 (to 20)
        >>   18 LOAD_CONST               0 (None)
        >>   20 RETURN_VALUE
>>> dis.dis(f4)
  1           0 RESUME                   0
  2           2 LOAD_FAST                0 (a)
              4 LOAD_CONST               1 (1)
              6 COMPARE_OP               2 (==)
             12 POP_JUMP_FORWARD_IF_FALSE     2 (to 18)
  3          14 LOAD_CONST               2 ('A')
             16 RETURN_VALUE
  2     >>   18 LOAD_CONST               0 (None)
             20 RETURN_VALUE
>>>
```

Interestingly, there is one difference out of those four variants, where instead of a second `RETURN_VALUE` op, there's a `JUMP_FORWARD` to the single `RETURN_VALUE`. I assume that means that it's slower in a way that's so imperceptible that it's not worth caring about, but let's check:

```
>>> timeit.Timer("f(random.random())", setup="import random\ndef f(x): 'a' if x > 0.5 else 'b'").timeit(10000000)
1.4031157046556473
>>> timeit.Timer("f(random.random())", setup="import random\ndef f(x):\n if x > 0.5:\n  return 'a'\n else:\n  return 'b'").timeit(10000000)
1.326032117009163
```

I feel this does land in the expected place, where it's about style & readability. I suppose `f1()` explicitly shows that it's making a choice between two cases, but I feel that's countered by `f2()` and `f3()` showing that the function returns a value. In general, it's nice to have the smallest amount of indentation, so I would not choose to use `f1()`.

Between `f2()` and `f3()`, I would generally choose the single-line approach of `f3()` if the line didn't wrap (or exceed whatever the wrapping length is for the project, e.g. 100 characters). I would *not* do this:

```
def f3_alt():
    return (
        really_really_really_really_really_really_really_long_val
        if another_very_very_very_very_long_condition
        else also_quite_long_here_and_now_we_wrap
    )
```

If you're doing this, then there's no benefit over the `f2()` style (and, as it turns out, there is a very tiny performance penalty).

Python has an implicit `return None` at the end of a method that doesn't otherwise return. This means that for this specific case, where one of the values is None, there's also the choice between `f2()` and `f4()`. In reality, `f4()` would be slightly better than it is here, in that it would probably have a return type (with `|None`) and a docstring that explains that `None` is a possible return value. However, I still (weakly) prefer `f2()` where it's called out explicitly rather than `f4()` where you need to know that this is what Python does.
