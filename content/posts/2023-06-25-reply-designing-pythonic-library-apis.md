---
title: "Reply: Designing Pythonic library APIs"
date: 2023-06-25T11:52:47+12:00
slug: "reply-designing-pythonic-library-apis"
---
*(Post theme: [Code Monkey by Jonathan Coulton](https://music.apple.com/nz/album/code-monkey/211036259?i=211036269))*

Ben Hoyt has a great [post on designing Pythonic library APIs](https://benhoyt.com/writings/python-api-design/) (itself a written version of a talk he gave). I have some thoughts in response:

## Style

I love [PEP 20, the Zen of Python](https://peps.python.org/pep-0020/) (I used to have a set of t-shirts I had made that had one koan on each), and I think it's actually applicable more widely than just code (Python or otherwise). I certainly agree that following its guidelines is a great start.

Ben suggests following [PEP 8 (the style guide)](https://pep8.org), I would go further than that:

- Assuming that there's some sort of CI pipeline, that should include enforcement of a style (ideally auto-correcting to one). [Black](https://black.readthedocs.io/en/stable/index.html#) is the obvious choice here, and it's (for the most part) following PEP 8, but the most important thing is to have a consistent style where a tool does all the work.
- Shift work 'left' of the CI pipeline, and make it easy for contributors, by having your style format of choice part of [pre-commit](https://pre-commit.com) or some similar workflow, and have an appropriate configuration file for that in the source repository.
- Follow [PEP 257](https://peps.python.org/pep-0257/) for your docstrings (and obviously *have* good docstrings). IDEs sometimes shove in a bunch of text around return values/types and enforce conventions - I'm less bothered about those, and I think generally they (and the related recommendations in PEP 257) have been supplanted by type annotations in many cases. When other people are using the library, they'll see these docstrings, and they're probably also part of your automated reference documentation.
- While on the topic of docstrings, put an example or two in them anywhere it makes sense, and use [doctest](https://docs.python.org/3/library/doctest.html) to make sure that they stay correct.
- Have a style for imports (and use [isort](https://pycqa.github.io/isort/) or something similar) to automate/enforce that as well. I personally prefer sorting by (length, normalised case alphabetical) with groupings for, from top to bottom, the standard library, third-party libraries (with a blank line between each, ordered approximately by how well established they are), internal libraries, and then finally imports from within the same package. But again, it's the consistency that matters most. (This one isn't really about API design).

## "Pythonic"

In addition to the items that Ben mentions, I think it's important to design the API so that it works well with Python idioms. Exactly what this entails depends a lot on the specifics of the API, but for example:

- Functions & methods should be designed so that they can easily be used with the functools module (Ben has an example of this).
- Provide generators rather than returning a tuple or list when possible. These should work well with the itertools module, with yield from, etc.
- Work well with the standard library logging module (but don't be noisy when someone isn't using it). The logging module is an example of an API in the standard library that is poorly designed (or perhaps just is not particularly Pythonic), in my opinion, but it's the default choice for logging and utilised by tools like Sentry.
- Context managers. For example, if your object connects to something (a file, over a network, etc) then have the cleanup done in a method called close() so that you can using contextlib.closing (but actually also provide your own __exit__ to handle this).
- Where appropriate, make it easy to serialise data. This might include supporting pickling objects, but might also be to other formats (JSON, YAML, etc).

## Async

The Python releases that I really like are the ones that focus on improving performance (sometimes this is CPython specific) and usability (like the improved tracebacks in 3.11), and the standard library. In my opinion, for the most part, the Python language itself does not need regular changes, and sometimes these can be at the detriment of some of the aspects of Python that make it great (like readability and ease of learning).

I'm not (yet?) a fan of the walrus operator or pattern matching, for example. I have mixed opinions about type annotations. However, one change to the language over the last decade that I feel is definitely worthwhile is the addition of async & await. It was possible to use coroutines in Python previously, and understanding how async works does add complexity to learning the language, but I feel it expands what can be easily done with the language, in the same way that you can use Python in a very object-orientated way, or a very functional way, and so on.

One catch with async & await is that they have a tendency to spread throughout your code. You can 'collapse' async code into a synchronous action by adding an event loop and waiting until everything is done, but for the most part if you're using an async library then you're probably building your entire app in an async fashion. It's definitely much simpler to make use of a synchronous call inside of an async method than vice-versa.

There are libraries that have added async functionality after originally being synchronous (e.g. Django) but from what I've heard that has been complicated to get right and the API is less natural than otherwise (e.g. compare with FastAPI).

Whether or not a library should have predominately async methods, or both async and sync versions, or avoid async entirely depends a lot on what it's doing and how it's expected to be used. However, it's definitely something to think a lot about in advance, rather than try to adjust mid-flight.

## Exception Chaining

Ben has a good section on errors and exceptions. The only thing I would add is that you can and should explicitly chain exceptions so that it's clearer to the caller what's happening. I think Ben is referring to that here, but doesn't call it out explicitly:

> For example, if your library can raise [`ssl.SSLError`](https://docs.python.org/3/library/ssl.html#ssl.SSLError) when it’s calling an HTTP API, it’s probably best to catch that and re-raise as `fishnchips.NetworkError`.
>
> [Ben Hoyt](https://benhoyt.com/writings/python-api-design/#errors-and-exceptions)

Instead of doing this:

```
try:  
    ...  
except ssl.SSLError:  
    raise fishnchips.NetworkError()
```

You should do this to show that the SSLError was the "direct cause" of the NetworkError:

```
try:  
    ...  
except ssl.SSLError as e:  
    raise fishnchips.NetworkError() from e
```

Related to errors & exceptions, you should make use of the warnings module and the various [warning Exception classes](https://docs.python.org/3/library/warnings.html#warning-categories).

In this section, Ben also says:

> APIs should be designed so that it’s hard to make mistakes.

He doesn't have this as one of the takeaways, but I would 'promote' it to one.

## The standard library unittest package

Ben has unittest as an example of a poor standard library API. I agree with this, and I think it provides a good example of where API design can be challenging. The main problems with the unittest API (such as assertEqual(a, b) not being assert_equal(a, b) or a plain assert a == b) come from the API being an implementation of the [xUnit](https://en.wikipedia.org/wiki/XUnit) API (originally SUnit and popularised by J[ava's JUnit](https://junit.org/junit5/) but extremely widely used).

The question here is how closely the Python xUnit implementation should match the implementations in other languages (or, put another way, whether the Python standard library should have an xUnit implementation versus a library that supports unit tests that isn't necessarily xUnit). If you're coming to Python's unittest module from Java (and JUnit) then these are comfortingly familiar:

```
import static org.junit.jupiter.api.Assertions.assertEquals;  
  
import example.util.Calculator;  
  
import org.junit.jupiter.api.Test;  
  
class MyFirstJUnitJupiterTests {  
  
    private final Calculator calculator = new Calculator();  
  
    @Test  
    void addition() {  
        assertEquals(2, calculator.add(1, 1));  
    }  
  
}
```

```
import unittest  
  
# Probably a relative import in practice.  
import example.util  
  
  
class MyFirstUnittestTests(unittest.TestCase):  
    def setup(self):  
        self.calculator = example.util.Calculator()  
  
    def test_addition(self):  
        # In Python 2, this could have been assertEquals()  
        self.assertEqual(2, self.calculator.add(1, 1))
```

There are lots of other examples of APIs like this, where some underlying functionality is being exposed in many different languages, or where similar functionality is being implemented in many different languages. Sometimes, you get both, like with the python-mysql library:

```
import contextlib  
  
import MySQLdb  
  
# Fairly Pythonic, and aligns with the DB API (PEP 249)  
# The Connection object should have an __exit__ that closes.  
with contextlib.closing(MySQLdb.connect(**[connection args])) as db:  
    with db.cursor() as c:  
        c.execute("SELECT col1, col2 FROM tbl")  
        for col1, col2 in c.fetchall():  
            pass  
  
# Low level API that essentially exposes the MySQL C API.  
import _mysql as mysql  
  
conn = mysql.connect(**[connection args])  
conn.query("SELECT col1, col2 FROM tbl")  
result = conn.store_result()  
for col1, col2 in result.fetch_row(maxrows=0):  
    pass  
conn.close()
```

In general, I believe it's better to design your API to match the language, and copy the *intentions* and *outcomes* from the source, rather than try to completely match the API. This is one reason why [pytest](https://docs.pytest.org/en/7.3.x/) is superior to the standard library unittest.

## The standard library csv package

Ben has the csv module as an example of a good API, and I generally agree, and I think it's particularly so given how poorly defined the CSV format is, which makes working with CSV files much more challenging. The one nit I have is:

```
import csv  
  
with open("some.csv", newline="") as f:  
    reader = csv.reader(f)  
    for row in reader:  
        pass
```

I don't love that you have to know/remember to open the file with newline="" (in Python 2, you had to remember to open the file in binary mode). Most of the time it won't make any difference, but when you have a CSV with a newline in a quoted field it'll break if you don't do this (I'd argue that if you have that sort of CSV you perhaps are using the wrong serialisation format, but often that's out of your control).

It's more Pythonic to create objects from files than filenames (more technically: pass something *file-like* that supports the file protocol rather than something that supports the string protocol). It does feel like passing a string to csv.reader is generally wrong (you'll get each character in the string as a one column row), and the first argument to csv.reader can already be a list (or similar) or file (or similar), so perhaps a string could be taken to mean a filename. csv.reader_from_filename doesn't seem Pythonic, or csv.DictReader.from_filename. Having csv.reader call reconfigure() on the passed object is probably a bit too magic (explicit is better than implicit!).

In summary, this is a (very small part) of the csv API that I don't like, but I don't have a good suggestion for solving it, either.

## from library import something

Ben says:

> **Takeaway: Design your library to be used as** `import lib ... lib.Thing()` **rather than** `from lib import LibThing ... LibThing()`**.**
>
> [Ben Hoyt](https://benhoyt.com/writings/python-api-design/#module-and-package-structure)

I agree with the majority of his post but a huge 100% to this specifically. Namespaces are one honking great idea!

## Global configuration and state

In this example code of Ben's, he argues against having a module-level DEFAULT_TIMEOUT:

```
DEFAULT_TIMEOUT = 10  
  
def order(..., timeout=None):  
    if timeout is None:  
        timeout = DEFAULT_TIMEOUT  
    ...
```

This is an interesting argument, and goes against the common refrain (probably originating from languages like C) that you shouldn't have 'magic' numbers in your code and should define them at the top level instead.

If your intention is that people should be able to change the default, then you should definitely do this differently (e.g. as Ben describes). If your intention is that this default is never to be changed, then you can make this a little better in modern Python (3.8+):

```
import typing  
  
_DEFAULT_TIMEOUT: typing.Final[int] = 10  
  
def order(..., timeout=_DEFAULT_TIMEOUT):  
    ...
```

However, you'll need some sort of type checker to validate that it's actually not changed (which does go along with Python's "consenting adult" type approach to things like private variables).

## Type Annotations

Ben has a good section on type annotations, which pretty much exactly matches my feelings. I don't love them, or feel that they are themselves really Pythonic (although their use in libraries like [Pydantic](https://pydantic.dev) does, somehow). I completely agree with Ben's takeaway:

> On balance, I definitely think it’s the right thing to do in 2023 to ship your library with type annotations.
>
> And of course, don’t just use them, but run [Pyright](https://microsoft.github.io/pyright/) or [MyPy](https://www.mypy-lang.org/) over your library’s code on every commit.
>
> [Ben Hoyt](https://benhoyt.com/writings/python-api-design/#type-annotations)

Ben's last example of a positive of type annotations is:

> They help your IDE provide better navigation and auto-completion.

I agree that this is the case, and one of the more compelling reasons to use type annotations, and also why there's - to a certain extent - an obligation on library/package developers to provide them. However, I find it generally disappointing. I strongly feel that this functionality should be provided by the IDE without the user needing to put in all the manual work of explicitly typing everything. I wish we had solved this need with better tools rather than by putting a heap of additional work on developers - and especially without adding a heap of boilerplate to Python code. I understand that the dynamic nature of Python makes this hard, but hard problems are good ones to solve.

## Overriding Operators

Ben gives a rule of thumb:

> Only override math operators like `a+b` if you’re creating a number type.
>
> [Ben Hoyt](https://benhoyt.com/writings/python-api-design/#pythons-expressiveness-be-careful)

I agree with this for almost all math operators, except perhaps + (for example, using + to concatenate strings is more natural than str.join, and I think it was right to make that implementation faster rather than focus all energy on getting people to call join).

I think the standard library has a perfect example of a mistake here, which is [pathlib](https://docs.python.org/3/library/pathlib.html) and the division operator. I believe this is a cute hack that is maybe ok in a third-party library, but definitely does not belong in the standard library:

```
>>> import pathlib  
>>> p = pathlib.Path("~")  
>>> conf = p / ".mypackage" / "config.ini"  
>>> str(conf)  
'~/.mypackage/config.ini'
```

There was a lot of controversy about this back in 2012 (the [PEP](https://peps.python.org/pep-0428/#division-operator) has a reference to some of it), and maybe the right decision was made, but it's unPythonic and distasteful in my view.

## Keyword arguments

Ben makes an argument for keyword arguments helping with backwards-compatibility, which I agree with. He has this example:

```
def order(chips=None, fish=None):  
    """Place an order.  
  
    Args:  
        chips: number of scoops of chips  
        fish: number of fish  
    """
```

I would argue that these should be keyword-*only* arguments. If I'm writing a call to order, I'll never remember whether fish or chips comes first (I would even argue that they are backwards here, because - at least where I am - people say "fish and chips", not "chips and fish" - an [irreversible binomial](https://en.wikipedia.org/wiki/Irreversible_binomial) if you're a linguist). An IDE might help out when writing, but when reading the code, you're not necessarily going to have that context made available. A two character change, but it prevents easy mistakes:

```
def order(*, chips=None, fish=None):  
    """Place an order.  
  
    Args:  
        chips: number of scoops of chips  
        fish: number of fish  
    """
```

I also worry a bit about how this would scale. A fish'n'chip shop probably has at least a dozen items on their menu, and that's a lot of arguments. It could be generalised, something like:

```
def order(**kwargs):  
    """Place an order.  
  
    The arguments should be the name of the item, with the value: either the number of the item,  
           a tuple of (quantity, type),  
           or a list of such tuples  
  
    For example:  
  
    >>> fishnchips.order(chips=1, fritters=(4, 'potato'), fish=[(1, 'crumbed'), (1, 'battered')])  
    """
```

The main concerns I have about this are:

- If you want to have arguments that are not items in the order (like the timeout one Ben has as an example), it feels messy for that to be mixed in with the items. Using **kwargs helps, because you'd make timeout a keyword-only explicit argument and that would distinguish it, but it still feels untidy to mix order items and order configuration into what is essentially one dictionary.
- The item names are limited to what's supported by Python names. That means it can't start with a number, can't have spaces, can't have punctuation, and so on. For the most part this is probably fine - you can have onion_rings instead of 'onion rings' and the like. It feels like it might get challenging to remember the rules for converting from 'real name' to 'argument name', though. I also suspect that eventually the method will need the 'real name' for logging or display or similar.
- Related to the issue of remembering the rules is remembering what can be ordered. With Ben's version, the signature tells you that you can have fish or chips. With my kwargs one, it does not - presumably there is some validation of the arguments in the function, but that doesn't help the caller prior to runtime.
- I'm not sure how well this would continue to scale. Say that after adding crumbed fish, we decide to sell both Snapper and Tarakihi. Do we now support an argument like fish=(3, 'crumbed', 'snapper')? How do I remember that it's not fish=(3, 'snapper', 'crumbed')? How are we going to handle burgers, which have lots of ingredients that people might want to customise?

I realise Ben was using this as an example of how keyword args and dynamic typing help backwards compatibility (which they do), and not trying to design the ultimate fish&chips library API. However, I feel like you'd need to move to a single collection of objects (probably dataclasses) before long.
