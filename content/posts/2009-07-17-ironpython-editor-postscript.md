---
title: "IronPython editor postscript"
date: 2009-07-17T16:43:26+12:00
slug: "ironpython-editor-postscript"
categories:
  - "Python"
  - "Tools"
  - "Work"
tags:
  - "eclipse"
  - "editor"
  - "IDE"
  - "IronPython"
  - "netbeans"
  - "pydev"
  - "teaching"
comment_id: "156"
comment_count: 5
pingback_id: "156"
pingback_count: 1
---
[I earlier tried various editors I was considering using to teach IronPython](http://tonyandrewmeyer.wordpress.com/2009/07/12/choosing-an-ironpython-editor-for-teaching/).  One of the glaring omissions was Eclipse/PyDev, which has built-in support and is a very well-known IDE (particularly in the [Java](http://java.com) community).  The main reason that I skipped Eclipse was that when I was searching for an IDE to use professionally about five years ago I tried Eclipse (for [Python](http://python.org), C, and C++ development) and I really hated it - the IDE was very slow (especially to launch), it was very Java-centric, and just didn't suit me at all.  I'd briefly tried Eclipse before that as well, with similar results.
Over the last few days, I decided that I was probably being unfair, and since this was a choice for my students rather than for me personally, I really ought to try Eclipse (with the PyDev extensions).  I also noticed recently a post about using IronPython with NetBeans - I'd heard of NetBeans before, but only in a Java development context, and since I stay as far away from Java development as I can, I had no experience with NetBeans at all.

## [Eclipse](http://www.eclipse.org/)/[PyDev](http://pydev.sourceforge.net/)

I was right to re-examine Eclipse.  The things that I remember bothering me so much five years ago (speed, the interface) seem to have been completely addressed, and it looks like a quite usable product.  When adding PyDev (which was quite simple), there's support for IronPython that appears completely built-in (although it's still obvious that Java is the #1 choice).  It seemed like a quite reasonable contender, unlike I tried to actually configure it to use the IronPython interpreter (which has to be done manually).  I was using a completely standard, fresh, installation of IronPython 2.0.1 (from the .msi) installed in the default location (here 'C:\Programs\Iron Python 2.0.1') with 'Eclipse Classic 3.5' and version 6u14 of the Java Runtime.
I believe that, in theory, you can click the automatic configuration button, or manually locate the IronPython interpreter, and it'll just work.  Unfortunately, for me nothing seemed to work.  The error message indicated that having spaces on the Eclipse path could be a problem (which seems pretty shocking in 2009), so I tried moving Eclipse to C:\, which didn't help.  I tried moving IronPython to C:\ (and renaming the folder to have no spaces), and that didn't help.  I imagine that someone more familiar with Eclipse, or with PyDev with CPython/[Jython](http://www.jython.org/), might have been able to solve this easily.  However, if I can't figure it out in 10 minutes, then I am not at all comfortable with telling my first-year students to use it (even though we walk through the installation together, some of them will need to do that by themselves as well).

## [NetBeans](http://www.netbeans.org/)

It wasn't entirely clear which version of NetBeans to use, but I presumed that the most appropriate was NetBeans 6.7 "Python EA2".  Although [the post I saw](http://stevegilham.blogspot.com/2009/05/using-ironpython-with-netbeans-python.html) indicated that you needed to rename ipy.exe and ipyw.exe, I found that just selecting ipy.exe worked fine.  I quite liked this IDE, and it appeared (although I didn't use it for long) that using IronPython worked fine.   There's no graphical form designer, so NetBeans is in the same category as Komodo Edit (which I discussed previously).  In many ways, it's probably a better choice than Komodo Edit (in that the IronPython integration is simpler to do, although it does require that Java is installed), although I don't know if there is any way to provide .NET auto-complete.  It's a fairly full-featured IDE, like Komodo and unlike DIE, which would normally be a positive, but in this specific case (first-year programming students) is actually a negative, since they need to ignore all the 'team' functionality, and you have to work within projects (which is true of Visual Studio as well).  This is an "early access" version - since I'm not familiar with NetBeans I don't know how unreliable that makes it - it makes me a little nervous about suggesting it to students, but I certainly didn't have any trouble with it myself.

## Conclusion

If you're able to get Eclipse/PyDev installed, then I suspect it might slightly beat out my previous recommendations of Komodo Edit and DIE; since I didn't get it working, I can't recommend it to the students.  NetBeans, however, will get added to the list of suggested tools (alongside Komodo Edit and DIE).  If I wasn't so familiar with Komodo Edit, I'd probably use NetBeans as the editor I use to demonstrate, but it didn't wow me so much that it overcomes the familiarity.
