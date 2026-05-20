---
title: "Mailbox flattening messages"
date: 2009-08-30T21:35:44+12:00
slug: "mailbox-flattening-messages"
categories:
  - "Python"
  - "Work"
tags:
  - "email"
  - "mailbox"
  - "unicode"
  - "unicodedecodeerror"
---
The [mailbox.py](http://docs.python.org/library/mailbox.html) code does this to dump a message (e.g. when adding to a Maildir file):

```
def _dump_message(self, message, target, mangle_from_=False):
    # Most files are opened in binary mode to allow predictable seeking.
    # To get native line endings on disk, the user-friendly \n line endings
    # used in strings and by email.Message are translated here.
    """Dump message contents to target file."""
    if isinstance(message, email.Message.Message):
        buffer = StringIO.StringIO()
        gen = email.Generator.Generator(buffer, mangle_from_, 0)
        gen.flatten(message)
        buffer.seek(0)
        target.write(buffer.read().replace('\n', os.linesep))
    elif isinstance(message, str):
        if mangle_from_:
            message = message.replace('\nFrom ', '\n>From ')
        message = message.replace('\n', os.linesep)
        target.write(message)
```

(There's a bit more that deals with other types of message).  Unfortunately, with some messages containing Unicode characters, this breaks with a UnicodeDecodeError:

```
Traceback (most recent call last):
  File "", line 1, in
  File "/usr/lib/python2.5/mailbox.py", line 245, in add
    self._dump_message(message, tmp_file)
  File "/usr/lib/python2.5/mailbox.py", line 203, in _dump_message
    buffer.seek(0)
  File "/usr/lib/python2.5/StringIO.py", line 106, in seek
    self.buf += ''.join(self.buflist)
UnicodeDecodeError: 'ascii' codec can't decode byte 0xd6 in position 106: ordinal not in range(128)
```

The message does flatten with message.as_string() - or str(message) - without any problems.  I'm not really sure why mailbox.py doesn't just use as_string(), rather than create a generator itself.  I'm also not totally sure where the error is coming from, especially since it happens inside of seek().
For now, I can just call mailbox.add() with msg.as_string(), rather than with msg directly, and it'll work fine.  At some point, if I have time, I'll revisit this and try and figure out if it's a [Python](http://python.org) [bug](http://bugs.python.org/) that should be reported.
