---
title: "Choosing an IronPython editor for teaching"
date: 2009-07-12T11:25:28+12:00
slug: "choosing-an-ironpython-editor-for-teaching"
categories:
  - "Python"
  - "Tools"
tags:
  - "DIE"
  - "editor"
  - "IDE"
  - "IronPython"
  - "Komodo"
  - "Northtec"
  - "Notepad++"
  - "teaching"
  - "Visual Studio"
comment_id: "152"
comment_count: 9
---
The [Northtec](http://northtec.ac.nz) D520 "Programming" course is changing to [IronPython](http://www.codeplex.com/IronPython) (from [Visual Basic](http://en.wikipedia.org/wiki/Visual_Basic)) this year, so I have to figure out what editor/IDE the students should use.  In some ways, [Visual Studio](http://www.microsoft.com/express/) would be ideal, since they need to get exposed to that during the course (and it's an excellent IDE, with a really great form designer), but since there isn't any real IronPython support in Visual Studio (hopefully coming in 2010), it's not really a viable option.  Instead, they'll start with a simpler editor, and then briefly learn how to use Visual Studio's form designer and subclass the forms in IronPython (as described in [IronPython in Action](http://www.ironpythoninaction.com/)).
The requirements here are a bit different than when selecting an editor/IDE for actual development work.  Firstly, it needs to be free (at least for educational use), and it needs to be reasonably simple to use the basic functionality (since these are first-year students).  Code-completion isn't necessary (on the one hand, it helps them out while they are learning - on the other, they rely a little too much on it), nor is a built-in debugger, or support for complex projects.
I considered seven different editors/IDEs - there are a couple of others, but they either seemed too young (e.g. [IronPython IDE](http://lynanda.com/mediawiki/index.php/Main_Page), [IronEditor](http://www.codeplex.com/IronEditor)), or inappropriate for other reasons (e.g. [ZeusEdit](http://zeusedit.com/python.html) is not free, I can't stand [Eclipse](http://pydev.sourceforge.net/).  **UPDATE**: [I decided to try Eclipse and Netbeans after all](http://tonyandrewmeyer.wordpress.com/2009/07/17/ironpython-editor-postscript/)).

## [Notepad++](http://notepad-plus.sourceforge.net/)

This is the editor that the students use (with [CPython](http://python.org)) in D500 in the first semester.  As such, it has a significant advantage in that the students are familiar with it.  It has a very traditional open-source look (a command/option for everything, and ease-of-use be damned), and seems like a pretty decent programmer's text editor.  There's no IronPython support, but the CPython code highlighting should work sufficiently well, and since it's just an editor, there isn't really a need for anything else.  In theory, I should be able to add a "IronPython Shell" (and maybe even "Run in IronPython") command to the "Run" menu, but I wasn't able to get that to work.

## [IronPython Studio](http://www.codeplex.com/IronPythonStudio)

This is a project (not from the IronPython team, or the Visual Studio team) that uses the Visual Studio SDK to build a Visual Studio that does include IronPython support.  In many ways, it's ideal - it **is** Visual Studio (not a clone, like SharpDevelop, discussed below), and it includes native support for IronPython.  All the components of Visual Studio (the good editor, the graphical form designer, the debugger) are present, and moving from IronPython Studio to Visual Studio would be fairly seamless. However, the IronPython support is for IronPython 1, and the students really need to be working with IronPython 2.0 or IronPython 2.6.  I believe that the project can be rebuilt to use the newer IronPython versions, but that's too complex for the students, and too untested to rely on for the semester.

## [SharpDevelop 3.0](http://www.icsharpcode.net/OpenSource/SD/Download/)

It seems like [SharpDevelop](http://www.icsharpcode.net/OpenSource/SD/) is to Visual Studio as [OpenOffice](http://openoffice.org) is to [Microsoft Office](http://office.microsoft.com/), i.e. an open-source project that aims to completely reproduce the commercial product, rather than develop anything interesting of their own.  That does appeal in some ways (since it includes IronPython support, which Visual Studio currently lacks).  However, the 3.0 release doesn't include a graphical form designer (at least for IronPython), which is the largest benefit (for these students) of Visual Studio (or a clone).  Although I'm a huge fan of open-source development, I'm less of a fan of clones of commercial software, and reluctant to have students get used to the clone, rather than the software that they would actually use in practice.  If the graphical form designer were present, that would probably be enough to overcome that reluctance, but as it is, I would rather have them start with a simpler editor and move to Visual Studio without IronPython support.

## [SharpDevelop 3.1b1](http://www.icsharpcode.net/OpenSource/SD/Download/)

The 3.1 version of SharpDevelop (currently in beta) **does** have the graphical form designer for IronPython projects.  However, if I try to do just about anything in the beta version, it crashes.  I expect that this is something specific to my configuration (and would be resolved by the final release), but since the students will have exactly the same VM image, it'll hit them, too.  So, unfortunately, this can't really be considered.

## [Wing IDE 101](http://wingware.com/wingide-101)

Wing IDE is the recommendation of [Michael Foord](http://twitter.com/voidspace), author of IronPython in Action, which carries a considerable amount of weight.  Although [Wing IDE](http://wingware.com/products) isn't free, there is a version specifically designed for education (Wing IDE 101).  The biggest drawback is that, although the Python support is excellent, the IDE doesn't support IronPython.  There are [ways to add auto-complete support](http://www.voidspace.org.uk/ironpython/wing-how-to.shtml) (which I believe is disabled in the 101 version anyway), but choosing to execute the file with Python will use CPython, and the built-in interactive interpreter is CPython.  I believe having Python support in the IDE but having to switch out to the shell to use IronPython would just confuse the students.  (However, if they used Wing IDE 101 in their first, CPython, course, then I would probably choose to continue with it).

## [Davy's IronPython Editor](http://code.google.com/p/davysironpythoneditor/)

DIE reminds me a lot of [Jen's File Editor](http://home.arcor.de/jensaltmann/JFE/jfe_eng.htm), which is the editor that was used throughout my own undergraduate study (but for C and C++, not Python).  I very much like the simplicity, and I like that it's easy to use both CPython and IronPython (so the students could compare, and try to make code that was compatible with both variants).  The editor is reasonably young, however, and still fairly rough (e.g. the preferences dialogue requires "y" or "n" strings rather than using checkboxes), and the program exposes log information that a regular user wouldn't be interested in.  The most annoying weakness for me personally is the lack of auto-indent (since I'm used to that from everywhere else).

## [Visual Studio under Experimental Hive](http://www.microsoft.com/downloads/details.aspx?FamilyId=59EC6EC3-4273-48A3-BA25-DC925A45584D&displaylang=en)

The Visual Studio SDK includes a sample project that adds IronPython support to Visual Studio (this is what IronPython Studio, discussed above, is based on).  If the SDK is installed, then it's pretty simple to build the IronPython project, which leaves the user with a "Visual Studio under Experimental Hive" (this could optionally include other SDK projects) that is the desired Visual Studio with native IronPython support.  The biggest drawback here is that this is experimental, unsupported, code - worse in some respects than using a beta version.  However, I've played around with it a reasonable amount, and haven't had any problems, so perhaps the stability of Visual Studio is enough to overcome the "experimental" aspect.

## [Komodo Edit](http://www.activestate.com/komodo_edit/)

I use Komodo Edit as my primary editor (although on [OS X](http://apple.com)) for actual development work, so it has a significant personal advantage in that respect.  In many ways, it's similar to the Notepad++ option, in that there isn't any real IronPython support, but the CPython support is sufficiently good that it would suffice.  However, unlike Notepad++, I was able to easily add a "Run with IronPython" command (as well as "Run with CPython", "IronPython Shell", and "CPython Shell").  Like Wing IDE, [it's possible to add code-intelligence for IronPython](http://lists.ironpython.com/pipermail/users-ironpython.com/2004-August/000062.html).

## Conclusion

Unfortunately, there isn't a clear winner.  My recommendation will be that the students spend the first half of the course using a text editor: if they are comfortable continuing to use Notepad++, then that makes the most sense.  If they are willing to try a new tool, then I would recommend Komodo Edit (or DIE if they want something that just works without having to do any additional configuration).  When the time comes to start learning how to use a graphical form designer, then I would recommend that they install the Visual Studio SDK and add IronPython support under the "Experimental Hive", although they'll also learn how to use standard Visual Studio and subclass C#/Visual Basic forms in IronPython.  It seems like they could then continue to use the "Experimental Hive" for the rest of the semester (even for Console projects), although they would know how to fall back to the previous tools if necessary.
