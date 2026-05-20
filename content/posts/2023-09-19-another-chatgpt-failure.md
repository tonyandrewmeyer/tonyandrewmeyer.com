---
title: "Asking ChatGPT for help, take 2"
date: 2023-09-19T23:24:19+12:00
slug: "another-chatgpt-failure"
categories:
  - "Python"
---
(*Post theme: [With a Little Help From My Friends by Joe Cocker](https://music.apple.com/nz/album/with-a-little-help-from-my-friends/1434915471?i=1434915474))*

People (at lunch) at [Kiwi PyCon](https://kiwiPyCon.nz) were praising ChatGPT as a tool to help write code more efficiently, so I had another go.

I recently moved a Django project to use [Whitenoise](https://whitenoise.readthedocs.io/en/latest/), and more specifically to have [manifest files](https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/#manifeststaticfilesstorage), where the version is appended to the collected file names. This all works great, except that there are a few files that users download, and instead of getting, for example, `template.xlsx`, they were getting `template.{md5hash}.xlsx`.

[I asked how to have the file downloaded with the original name, rather than the one with the version hash](https://chat.openai.com/share/c2b74db4-924d-4425-8e28-c5b0e068fb68). In retrospect, I realise I asked the wrong question, because this is an HTML question not a Django staticfiles one, but I hadn't thought about it enough at the time, and, anyway, surely the assistant is meant to pick up on that.

The answer told me to use [the 'as' functionality of the static tag](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#std-templatetag-static), but that's completely wrong. That's to get the URL into a variable to use in the template.

To be fair, it then did give the correct answer, that the `download` attribute of the `a` tag should be used. So I guess I'd give this a B- grade, for getting the solution but confusing it with a bunch of irrelevant info first.
