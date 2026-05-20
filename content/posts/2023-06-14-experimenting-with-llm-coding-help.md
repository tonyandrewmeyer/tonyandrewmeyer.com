---
title: "Experimenting with LLM coding help"
date: 2023-06-14T14:01:28+12:00
slug: "experimenting-with-llm-coding-help"
---
*(Post-theme: [With a Little Help From My Friends by the Beatles](https://music.apple.com/nz/album/with-a-little-help-from-my-friends/1441164604?i=1441164851))*

LLM & generative AI buzz is everywhere, and assistance writing code (either via something like copilot or by just querying a model) is supposedly a huge productivity boost, so I was curious enough to try this out. [Simon Willison](https://simonwillison.net) has written a lot of interesting things about LLM including how he's used it for developing, and made it seem like something that could be useful.

As a first experiment, I wanted to use the "ask the LLM to draft something for me" approach (rather than a IDE-integrated tool like copilot), and I wanted to avoid having to go through a 'conversation' of prompts (particularly one where I had to guide the model to a solution I already knew or guessed). It's usually pretty easy to find what I need by looking at the docs (or code), so if this is going to be useful for this sort of work, then I need it to be simple and fast.

Details of the two attempts I've made so far are below, but in summary: I'm underwhelmed so far. Maybe I'm not trying the right sort of problems (one was real, one was an exercise), or maybe I need to be better at prompt crafting or more willing to spend time 'talking' with the model. I have some investigation/experimentation to do with production use of LLM so may try out some more personal use then.

## Redirecting users to a custom landing page in Django

I have a Django site that's about 13 years old, so has gone through a lot of Django versions. It has the ability to specify a landing page (ie. where you end up after logging in) per-user, if one isn't specified in the params (ie. in the typical "next" arg). I noticed that at some point this had broken, and wanted to fix/re-implement it for modern Django.

I asked

> How do I get Django to redirect a user after logging in to a page specified in a user model field?

The answer I was given is:

```
You can get Django to redirect a user after logging in to a page specified in a user model field by defining a custom redirect function in your `views.py` file and using it in your `urls.py` file.  
  
In your `views.py` file, define a function that retrieves the desired redirect URL from the user model field and redirects the user to that URL after login:  
  
```python  
from django.contrib.auth.decorators import login_required  
from django.shortcuts import redirect  
  
@login_required  
def custom_redirect(request):  
    redirect_url = request.user.redirect_url # Replace 'redirect_url' with the name of your user model field  
    return redirect(redirect_url)  
```  
  
In your `urls.py` file, map the custom redirect function to the Django login view:  
  
```python  
from django.contrib.auth.views import LoginView  
from .views import custom_redirect  
  
urlpatterns = [  
    # Other URL patterns...  
    path('login/', LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'), name='login'),  
    path('redirect/', custom_redirect, name='custom_redirect'),  
]  
```  
  
Note that in the above code, we're using Django's built-in `LoginView` and setting the `redirect_authenticated_user` parameter to `True` to automatically redirect authenticated users to the `custom_redirect` URL. We're also specifying the path to the login template using the `template_name` parameter.  
  
Finally, update your user model to include the `redirect_url` field:  
  
```python  
from django.db import models  
from django.contrib.auth.models import AbstractUser  
  
class CustomUser(AbstractUser):  
    redirect_url = models.CharField(max_length=255, blank=True, null=True)  
```  
  
Now when a user logs in, they will be redirected to the URL specified in the `redirect_url` field of their user model.
```

The immediately obvious problem here is that this doesn't work. Nothing gets the user to the /redirect/ path, so although that would work to redirect to the user's chosen page, it isn't any part of the login flow. The second obvious problem is that the [redirect_authenticated_user](https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.views.LoginView.redirect_authenticated_user) doesn't do what the model described at all - it's basically about bypassing the login page when someone is already logged in.

(Side note: while looking up links for this post, I came across this [SO question](https://stackoverflow.com/questions/2320581/django-redirect-logged-in-users-from-login-page#2320702) about this (which is likely forming a lot of the LLM's answer I suspect). It's not that clear either, but I guess going to SO is what people typically did before LLM? Personally, my go-to is always the docs.)

I could make a solution like this work - if you set the LOGIN_REDIRECT_URL to be the redirect path and a few other adjustments. However, it's messy and handling a 'next' style param won't work properly without duplicating a bunch of code.

For reference, what I did (which I believe is the 'correct' approach, at least as-of the version of Django I'm using) is:

```
# Add this line to my URLs.  
path("accounts/login/", [...].login.LoginUserRedirectView.as_view()),  
  
  
# Add this class to a login module in my app.  
class LoginUserRedirectView(LoginView):  
    """Like the parent, but with a custom per-user redirect system."""  
    def get_redirect_url(self):  
        # It would probably be cleaner to just check for the Anonymous User.  
        if not self.request.user or not hasattr(self.request.user, "last_login"):  
            return super().get_redirect_url()  
        # Having "next" in the request parameters is already handled by the normal login view and will bypass this view completely.  
        redirect_to = self.request.POST.get(  
            self.redirect_field_name, self.request.GET.get(self.redirect_field_name)  
) or self.request.user.landing_page or ""  
        url_is_safe = url_has_allowed_host_and_scheme(  
url=redirect_to,  
allowed_hosts=self.get_success_url_allowed_hosts(),  
require_https=self.request.is_secure(),  
)  
        return redirect_to if url_is_safe else ""
```

The [documentation on this](https://docs.djangoproject.com/en/4.2/topics/auth/default/#module-django.contrib.auth.views) (unusually for Django) isn't great. However, the [code](https://github.com/django/django/blob/1c4f5f314e2b0c77b3fa0c75f703218e7e06f4be/django/contrib/auth/views.py#L43) is very clear, and makes it pretty obvious how to do the appropriate subclassing (as well as some safety checks).

## Evaluating a basic maths expression in Python

The second one I tried was from an interview exercise. When I was talking to interviewers after completing the test, one of them mentioned that there was a lot of submissions that were clearly from LLM, which made me curious how it would have done. Using one during the exercise didn't occur to me, but I doubt it would have appealed anyway, since it would consume a bunch of quite limited time and I wouldn't have expected it to do particularly well.

The task was to take a string like "3 + 7 / 5 * 2" and give 5.8. No brackets, only integers, only addition, subtraction, multiplication, and division, respecting the precedence of operators.

I asked

> Write a Python script that can add, subtract, divide, and multiply given an input string, and respects the order of operators, so multiplication and division are done before addition and subtraction.

The answer I was given is:

```
Here's an example Python script that can perform basic arithmetic operations while respecting the order of operations:  
  
```  
def calculate(expression):  
    # Split the expression into a list of tokens  
    tokens = expression.split()  
  
    # Initialize the result to the first number in the expression  
    result = float(tokens[0])  
  
    # Loop through the remaining tokens and perform the appropriate operation  
    for i in range(1, len(tokens), 2):  
        operator = tokens[i]  
        operand = float(tokens[i+1])  
  
        if operator == '+':  
            result += operand  
        elif operator == '-':  
            result -= operand  
        elif operator == '*':  
            result *= operand  
        elif operator == '/':  
            result /= operand  
  
    return result  
```  
  
To use this script, simply call the `calculate()` function with a string containing the arithmetic expression you want to evaluate. For example:  
  
```  
expression = '5 + 3 * 2 - 4 / 2'  
result = calculate(expression)  
print(result)  # Output: 10.0  
```
```

This is also very clearly wrong. For one thing, the example at the end has the wrong answer - if you ignore precedence then it would give 6 and if you do it correctly it would give 9 (I'm not sure how to get 10). Looking at the code, it also clearly does nothing at all to respect operator precedence.

More importantly, there's no code that even vaguely hints at dealing with operator precedence. Also, converting to a float is risky with maths unless you really know the context and understand the implications.

For the record, I considered three approaches to this.

### Eval()

The first was trivially simple - use eval(). I spent quite a bit of my allowed time internally debating whether the point of the exercise was to check whether I knew eval() existed and how to appropriately use it and that I wouldn't pointlessly re-implement built-ins - or whether it was not meant to be used, even though that wasn't in the (otherwise quite detailed) instructions. I put in a bunch of code to handle errors and additional safety restrictions, but at heart, this is just

```
return eval(input_string, {}, {})
```

### Double-pass Item Replacement

The second was to do two passes of the input string (first for multiplication and division, and second for addition and subtraction), replacing chunks of the expression by the results. This is fairly straightforward, and my main concerns at the time were that this seems like it would get very messy as soon as you try to extend it to do anything else, and that tracking your location in the expression gets messy when you're changing the length as you iterate through it.

Roughly, again ignoring error handling and so forth, and ignoring that this has a bunch of unneeded conversion to decimals, this is:

```
tokens = s.split()  
i = 1  
while i < len(tokens):  
    if tokens[i] == "*" or tokens[i] == "/":  
        left = decimal.Decimal(tokens[i - 1])  
        op = tokens[i]  
        right = decimal.Decimal(tokens[i + 1])  
        if op == "*":  
            tokens[i - 1:i + 2] = [left * right]  
        else:  # op == "/"  
            tokens[i - 1:i + 2] = [left / right]  
    else:  
        i += 2  
i = 1  
while len(tokens) > 1:  
    if tokens[i] == "+" or tokens[i] == "-":  
        left = decimal.Decimal(tokens[i - 1])  
        op = tokens[i]  
        right = decimal.Decimal(tokens[i + 1])  
        if op == "+":  
            tokens[i - 1:i + 2] = [left + right]  
        else:  # op == "-"  
            tokens[i - 1:i + 2] = [left - right]  
    else:  
        i += 2  
return tokens[0]
```

In terms of an exercise, this shows an understanding of replacing a slice of a list in Python, and the performance isn't terrible (memory is fine, looping twice is ok). There's a bunch of tidying up that could be done, but it would probably have sufficed. I don't like that it would get complicated quite quickly if you expanded it - adding parentheses and brackets, for example. It is better than eval, unless the point is to show that you shouldn't reimplement something unnecessarily.

### Convert to Post-fix Notation, Evaluate

The third approach, which is the one I like most, was to convert the expression to RPN and then evaluate the RPN expression. I could remember that RPN evaluation was trivial (from way, way, back in my student days) and also that it was fairly simple to convert from in-fix to post-fix (also something I vaguely remember doing, probably in a Data Structures & Algorithms course ~25 years ago, probably in C++). I remembered that Dijkstra had an algorithm for this and the name had something to do with railways, but not the exact details (I looked it up for this: the [Shunting Yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)), and that it was basically just using two lists (I would have had to look up the exact details or play around with this, but for the simple case of just addition, multiplication, subtraction, and division, I could remember enough).

Roughly (without extensive testing or any of the error checking, etc), this is:

```
# Convert from in-fix to post-fix.  
precedence = {"+": 2, "-": 2, "*": 3, "/": 3}  
tokens = s.split()  
op_stack = []  
output_queue = []  
for token in tokens:  
    if token in "+-*/":  
        while op_stack and precedence[op_stack[-1]] >= precedence[token]:  
            output_queue.append(op_stack.pop())  
        op_stack.append(token)  
    else:  # Assume a number for now, ie. we're ignoring parentheses and other things.  
        output_queue.append(decimal.Decimal(token))  
while op_stack:  
    output_queue.append(op_stack.pop())  
# Evaluate the post-fix expression.  
funcs = {"+": "__add__", "-": "__sub__", "*": "__mul__", "/": "__truediv__"}  
i = 0  # A for loop would work here, but I hate changing a list while iterating through it.  
while len(output_queue) > 1:  
    if output_queue[i] not in funcs:  
        i += 1  # Skip this, we'll grab it when we get an operator.  
        continue  
    i -= 2  # Go backwards to get the two operands.  
    left = output_queue.pop(i)  
    right = output_queue.pop(i)  
    op = output_queue.pop(i)  
    output_queue.insert(i, getattr(left, funcs[op])(right))  # This probably tries to be too clever and a simple 4-clause if statement would be fine.  
return output_queue[0]
```

In terms of the exercise, this beats eval (again assuming the point isn't avoiding pointless work) and I feel it beats the previous version, since it's more readily extendable. Using the magic methods rather than just an if statement is probably unnecessary, but shows an understanding that they exist, that you should call them against the object, and shows an understanding of using functions as first-class objects (having them in the dictionary). It's more expensive in terms of memory - it could be improved a bit, but generally it's creating new containers not adjusting the existing one, so will always be worse. The code could do with a bunch of cleanup, especially the RPN evaluation, but it suffices for something done in a quick exercise.

Performance-wise, with a few trivial test statements (not trying to do this seriously at all):

```
$ python -m timeit -s "import eval_math as m" "m.test_eval()"  
10000 loops, best of 5: 21.8 usec per loop  
$ python -m timeit -s "import eval_math as m" "m.test_double_loop()"  
20000 loops, best of 5: 10.6 usec per loop  
$ python -m timeit -s "import eval_math as m" "m.test_rpn()"  
10000 loops, best of 5: 24.5 usec per loop
```

There are, of course, [many other ways](https://en.wikipedia.org/wiki/Operator-precedence_parser) to do this.

## Conclusion

I'm sure that LLMs can assist with coding, and make me more efficient. I don't feel I have figured out the way to make that happen, yet. More experimenting to do in the future, I suppose.
