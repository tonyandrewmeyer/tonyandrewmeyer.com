---
title: "My 2GB, 4 day 0.0.1 iPhone update"
date: 2009-08-03T11:24:26+12:00
slug: "my-2gb-4-day-0-0-1-iphone-update"
categories:
  - "rant"
tags:
  - "3.0.1"
  - "apple"
  - "iphone"
  - "recovery"
  - "update"
  - "vodafone"
comment_id: "170"
comment_count: 2
---
A few days ago, [Apple](http://apple.com) released version [3.0.1](http://support.apple.com/kb/HT3754) of the iPhone OS, which addressed a pretty major SMS vulnerability.  When Olyvia tried updating her 3GS to 3.0.1, something went wrong.  The iPhone entered "Recovery Mode", which means that it displays an image indicating that you need to connect it to iTunes, and you can't do anything else (no phone calls, no iPod, no applications - absolutely nothing).  Connecting the phone to iTunes prompted a message indicating that the phone needed to be recovered - doing so downloaded the 3.0.1 update, and then got stuck on the "Verifying Restore with Apple" step for a long time, until it would finally fail with error "3104".  This process could then be repeated, with the same results.
What this meant in practice was that the phone was bricked as of last Friday.  **An update should never be able to brick a (legitimate, not jailbroken) phone!** Even more, failing to verify a restore with Apple should never leave the phone in a broken state.
I tried many thing to resolve this:

- Restoring on three different computers (three OS X Leopard, one Windows XP).
- Using three USB cables.
- Using two Internet connections (different router, different physical location, different ISPs).
- Restoring with five different user accounts, including one that was created solely for this purpose.
- Removing iTunes and the Mobile Device helper completely and reinstalling.
- Restoring with an administrator account (both OS X and Windows XP) and a standard account.
- Redoing the restore at many different times of day, including times when most of the US would be asleep (so the server load should be fairly low), over Friday, Saturday, Sunday, and Monday.

None of this worked.  It did mean that I downloaded the 300MB+ update six times (one for each user account and once to refresh) over the four days.  That combined with the iTunes installation brings the total download cost to around 2GB.
I eventually gave up.  [Google](http://google.com) found many other people with this problem, but only a single [solution](http://ipitg.net/how-to-kick-iphone-out-of-recovery-mode-mac/), which involved opening a terminal connection to the phone and changing an environment variable.  I wasn't particularly comfortable doing that, since if something goes wrong I want [Vodafone](http://vodafone.co.nz)/Apple to just replace the phone without any argument.  Since there isn't any real support available over the weekend, I waited for Monday morning.
I wasn't sure whether to contact Apple (expecting a "please call Vodafone" answer) or Vodafone (expecting a "what do you mean you updated your phone?  Can you do that?" answer).  Thankfully, Vodafone NZ has a very responsive and helpful [Twitter](http://twitter.com) presence ([@vodafoneNZ](http://twitter.com/vodafoneNZ)).  I tweeted, asking who to call, and was asked for details.  I provided these (going into more detail in an email), and got back a (unfortunately not helpful at all) suggestion.  Since that didn't work, [Paul Brislen](http://twitter.com/paulbrislen) provided me with an 0800 number for the "iPhone Team" (I'd call them "iTeam", subtitled "there's an 'i' in iTeam", but anyway...).  Unfortunately, since I had to do a lot of travelling and offline things on Monday, I wasn't able to get to this until Tuesday.
I certainly appreciate a (free) phone number I can call.  However, I don't have a great deal of time to spend talking on the phone, explaining a rather complex problem and the many steps that I've already done to try and resolve the problem.  I also have poor cellphone coverage (Vodafone's fault) and a rather noisy landline ([Telecom](http://telecom.co.nz)'s fault), so voice calls aren't a great solution to a problem.  Faced with a (presumably) long and difficult phone call, the 'hack' solution of altering the environment variable looked a little more appealing.
I downloaded [iRecovery](http://ipitg.net/ifiles/iRecovery.zip) and opened a terminal (shell) connection to the iPhone.  Typing "printenv" gave a list of the environment variables - the ones that had a "P" at the start were presumably non-default values (these included "auto-boot", "bootdelay", "backlight-level", and "platform-uuid").  The article indicated that the "false" value for "auto-boot" was the problem (and the solution to use setenv to change it, then reboot the phone).  This seemed a reasonably safe thing to do (and also easily reversed), although I imagine that it would be rather scary to a non-programmer (who has no idea what "printenv" or "setenv" might mean).
Thankfully, this worked.  The iPhone rebooted - although it went straight back to the recovery page in iTunes, which wasn't hopeful.  However, this time the recovery process worked flawlessly (using the existing four-day-old copy of the download).  The phone was recovered from the automatic backup, and then sync'd.  Some of the settings are a bit out as you expect in a recovery, but the phone actually works, which is really all that matters.
I don't know what would have happened if I called the "iPhone Team" (and don't need to find out now).  I suspect that we wouldn't have got far, or maybe would have ended up doing exactly this (or perhaps having to return the phone for service).  I could be wrong about that.  I do feel that Vodafone (specifically @vodafoneNZ) handled this pretty well (and Apple extremely badly).
