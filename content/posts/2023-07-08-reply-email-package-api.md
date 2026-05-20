---
title: "Reply: Email Package API"
date: 2023-07-08T22:44:57+12:00
slug: "reply-email-package-api"
draft: true
---
*(Post theme: )*

## Type Annotations

## The standard library email package

I feel Ben is a little hard on the standard library email package (I've been writing email-related code in Python for 20 years so it's possible I'm just too close to it - but as part of that I do regularly have to share code or explain code or help others write code, where the other person doesn't have that history). It's also complicated because the standard library really has *two* email package APIs both sitting in the "email" namespace (this is not great).

(This is a *long* diversion, but I think the email package provides a convenient example of where I believe there's elements of good API design, and since there are actually two, good examples of how designs change and how backwards compatibility can be handled. But I've put it last for a reason, and skipping this whole section wouldn't be unreasonable).

It's true that email.mime.multipart.MIMEMultipart is very deeply nested. However, it's pretty uncommon to actually need to use any of the MIME classes directly (and they're also part of the legacy compat32 API). Most of the time that someone is using the email package, they are wanting to create an email or parse an email. If you're parsing an email, then you're generally going to be doing this:

```
import email  
import email.policy  
  
msg1 = email.message_from_bytes([byte string from a network or similar], policy=email.policy.strict)  
msg2 = email.message_from_string([Unicode string probably from a template], policy=email.policy.SMTP)  
msg3 = email.message_from_file([object supporting the file protocol, maybe a file, or sys.stdin, etc], policy=email.policy.SMTPUTF8)
```

You could argue that these could be email.from_bytes (I agree with Ben that import email, email.x is much better than from email import x) but I feel like the leading "message" is ok. Alternatively, these could be class methods like email.message.Message.frombytes, similar to datetime.datetime.fromtimestamp), but I don't feel there's a consensus as to which of these is more Pythonic.

Having to specify the policy is not great. If you leave that out, you get the "compat32" policy, which is essentially the email package from Python 2.2 until 3.3. It's entirely usable, and a lot of code will work with either type of object, so specifying the policy isn't strictly required. However, it is better to work with the newer API. Python 3.3 was released in 2012, and I feel that the default could have changed by now (even if it was by introducing convenience functions with different names).

Other than that, I believe these are well designed.

If you're creating an email, then there's a reasonable chance you're starting with a string so doing the same thing, for example:

```
import email  
  
import jinja2.sandbox  
  
env = jinja2.sandbox.ImmutableSandboxedEnvironment()  
template = env.from_string([template from somewhere]).render(**[args for the template])  
# You might want to specify a policy here, but if you're just going to send this with SMTP or something similar, the "compat32" object will be fine.  
msg = email.message_from_string(template)
```

If you're creating a message from scratch, then that's something like this with the older API:

```
import email.utils  
import email.header  
import email.message  
  
msg = email.message.Message()  
msg["Date"] = email.utils.formatdate(localtime=True)  
msg["From"] = email.utils.formataddr(("Tony Meyer", "feedback@tonyandrewmeyer.com"))  
msg["To"] = email.utils.formataddr(("Samuel Meyer", "music@fdasavage.nz"))  
msg["Subject"] = email.header.make_header([("Hello from Pūhoi", "utf8")])  
msg["Content-Language"] = "en"  
msg["Message-ID"] = email.utils.make_msgid()  
  
msg.preamble = "Content is visible in a MIME-capable reader\n"  
msg.add_attachment([attachment data bytes, such as an image or file])  
msg.set_payload([text/plain content here])  
msg.add_alternative([text/html content here], subtype="html")  
msg.get_payload()[1].add_related([attachment data bytes being used in the HTML, such as an image], cid=[unique content ID that gets used in the HTML to reference this data])
```

There are some things here that I *don't* like:

- I think email.message.Message could be copied into the email package's top level namespace (along the lines of Ben's comments about flat being better than nested). This is complicated by all the backwards compatibly aspects (for example, that you should use the EmailMessage class and not the Message class).
- I use this package and these functions all the time, and have done for years, and I still regularly forget that you need to pass a tuple of (display name, email address) to formataddr rather than calling it with those as two arguments. I believe the reasoning behind this choice is synchronicity with email.utils.parseaddr, but I think arguments would be much better - there's even a natural order (in the email structure itself and in the way emails are almost always displayed, the display name comes first) so there's no need to make these keyword-only.
- formataddr and formatdate are arguably a bit deep. Rather than copying them into the top-level namespace, I think the change most consistent with the rest of the package, and most enjoyable to use, would be for the email.message.Message class to have two additional methods, like add_header, but specifically for adding address or date headers (by far the most common two types, since they're r[equired](https://www.rfc-editor.org/rfc/rfc5322) and also tricky to get right so you want the code to handle things like non-ASCII encoding for you) - something like add_address_header and add_date_header - which combine add_header and the formatting function. The plain functions would still be in email.utils for the rare cases when you need to use them directly.
- formataddr also can't handle [non-ASCII local parts](https://datatracker.ietf.org/doc/html/rfc6531) or [domains](https://en.wikipedia.org/wiki/Internationalized_domain_name).
- make_msgid is an ugly name. The format methods don't have underscores, but this does, but only one, and "message" is abbreviated as "msg". I feel like the class could handle Message-ID fields more automagically.
- It seems to me that there could be generic preamble text set the first time any MIME content is added to a Message object (which you could customise if you really wanted to, but no-one does).

With the 3.3+ API, it's something like this:

```
import email.utils  
import email.message  
import email.headerregistry  
  
msg = email.message.EmailMessage()  
msg["Date"] = email.utils.localtime()  
msg["From"] = email.headerregistry.Address("Tony Meyer", "feedback", "tonyandrewmeyer.com")  
msg["To"] = email.headerregistry.Address("Samuel Meyer", "music", "fdasavage.nz")  
msg["Subject"] = "Hello from Pūhoi"  
msg["Content-Language"] = "en"  
msg["Message-ID"] = email.utils.make_msgid()  
  
msg.preamble = "Content is visible in a MIME-capable reader\n"  
msg.add_attachment([attachment data bytes, such as an image or file])  
msg.set_content([text/plain content here])  
msg.add_alternative([text/html content here], subtype="html")  
msg.get_payload()[1].add_related([attachment data bytes being used in the HTML, such as an image], cid=[unique content ID that gets used in the HTML to reference this data])
```

A lot of the issues I had with the older API are resolved here. There are still some parts I dislike:

- Why is the Address class in email.headerregistry?
