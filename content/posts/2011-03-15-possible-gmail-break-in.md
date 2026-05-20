---
title: "Possible gmail break-in"
date: 2011-03-15T08:09:49+12:00
slug: "possible-gmail-break-in"
categories:
  - "Me"
  - "Tools"
  - "Work"
tags:
  - "authentication"
  - "break-in"
  - "gmail"
  - "identification"
  - "passwords"
comment_id: "289"
comment_count: 6
---
When I logged into gmail this morning, I saw the message that I dread the most - detection of an unusual access.  There was a connection (two days ago) from a server in Malaysia, although it's actually an AWS server (Amazon web services).
There are two possibilities: the good one is that this is something that I've previously given access to my account, accessing it via an alternate method (e.g. Backupify can access my mail to back it up, and they use AWS) so that it showed up an unusual.  The bad one is that someone was using AWS to bulk-attack accounts and got in.
In favour of the good one, as far as I can tell, no email was sent - I can't see anything amiss at all.  The email account is the central lockbox for everything, of course, so it's possible that it was just used to break into other things, or the email content was retrieved.  My password (changed now, of course) was a random 8-character string of lower-case alphanumeric characters, so not particularly simple to break (although not difficult either, given sufficient resources).  I never give out the password to anything that I do not completely trust, and nor do I give out access via other methods (e.g. oauth, openid) unless I trust those services too.
I had intended to turn on two-factor identification, but hadn't got to it yet.  I've done that now, for the main account at least.  My password is now over 30 characters long, including upper and lower case and punctuation - I probably should have changed this a while ago too.
For now, I'm leaning towards the good possibility, so I won't be completely resetting everything that can send a password reminder to my gmail account.  I'll be keeping an eye on things as closely as I can in the next week or so, though.  If you see anything suspicious come from me, please let me know.
