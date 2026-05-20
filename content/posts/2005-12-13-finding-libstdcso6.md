---
title: "Finding libstdc++.so.6"
date: 2005-12-13T11:12:11+12:00
slug: "finding-libstdcso6"
categories:
  - "Old"
  - "PhD"
---
When I tried to build [Python](http://python.org) [2.4.1](http://python.org/2.4.1) on [doublehelix](http://doublehelix.massey.ac.nz) I ran into two problems:

- configure wouldn't complete, saying that it couldn't run compiled C programs.  I looked at the configure script and right before this it had something about not removing this section with autoconf 3.0:

# FIXME: These cross compiler hacks should be removed for Autoconf 3.0  
# If not cross compiling, check that we can run a simple program.

So I went ahead and commented out that section and it ran.  I suspect that this was actually caused by the second problem.

- make ran fine until it tried to use python to build the extension modules (or if I tried to run python manually once it was built).  I got "./python: error while loading shared libraries: libstdc++.so.6: cannot open shared object file: No such file or directory"

There's a lot of stuff online about this problem, and generally the solution is to either modify /etc/ld.so.conf to include a path to the library, or put the path on LD_LIBRARY_PATH.  I don't have access to /etc/, so the second seemed like the best plan.  A simple 'find / -name libstdc++.so.6' found three files with the right name, so I put the first one (/usr/local/lib) into LD_LIBRARY_PATH.  
  
Unfortunately, this didn't work - nothing seemed to change at all. I tried lots of other things, but nothing worked.  
  
The problem turned out to be that although they all had the same name, the three libstdc++.so.6 files were not the same (I imagine that one is specific to 64 bit compiling).  If I put the one in /lib64/ssa on LD_LIBRARY_PATH, all worked nicely (what normally goes into /lib64/ssa, I do not know).

technorati tags: [PhD](http://technorati.com/tag/PhD), [Coding](http://technorati.com/tag/Coding)
