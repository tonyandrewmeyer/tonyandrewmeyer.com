---
title: "emlx Files"
date: 2006-01-03T16:01:29+12:00
slug: "emlx-files"
categories:
  - "Python"
---
For the moment, I'm using [Apple](http://www.apple.com)'s [Mail](http://www.apple.com/macosx/features/mail/) as my primary email client (even though it's bafflingly slow at displaying messages at times (they're simple text files!), gets stuck updating at times, and won't let me tell it that [ihug](http://www.ihug.co.nz)'s SSL certificate is ok (which is partly ihug's fault for buying some cheap one instead of something that programs would recognise) it does have some nice features, and beats any of the other mail clients I've tried).

As of Tiger, Mail stores messages in individual emlx files, scattered through various folders in the ~/Library/Mail folder.  For use with [SpamBayes](http://spambayes.org)' test setup (as well as others, like the [TREC](http://plg.uwaterloo.ca/%7Egvcormac/spam/) one), I need messages in individual files in plain [RFC2822](http://www.faqs.org/rfcs/rfc2822.html) format.

What I needed was a simple export script (much like the existing Outlook export script - except hopefully faster and including attachments) that would create RFC2822 copies of the emlx files in the standard SpamBayes format (ham and spam directories containing a reservoir directory containing messages as individual text files).

I had thought that this might be quite difficult (take a look at the Outlook export script!) since emlx is a proprietory format.  Thankfully, I [discovered](http://bdash.net.nz/blog/2005/05/05/apple-s-mail-2-0/) that the first line is the size of the message in bytes (as text), followed by the RFC2822 message itself, followed by a plist containing various Mail information I'm not interested in (flags, sender, etc).  Nice to see that Apple can keep things simple.

  
So the SpamBayes distribution now contains a simple export_apple_mail.py script that will do the job.  

technorati tags: [email](http://technorati.com/tag/email), [spam](http://technorati.com/tag/spam), [spambayes](http://technorati.com/tag/spambayes), [python](http://technorati.com/tag/python), [trec](http://technorati.com/tag/trec)
