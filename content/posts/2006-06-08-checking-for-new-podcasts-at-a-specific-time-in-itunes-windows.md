---
title: "Checking for new podcasts at a specific time in iTunes (Windows)"
date: 2006-06-08T12:42:31+12:00
slug: "checking-for-new-podcasts-at-a-specific-time-in-itunes-windows"
categories:
  - "Tools"
comment_id: "49"
comment_count: 4
---
As far as I can tell, you can't tell iTunes when you want to check for new podcast episodes - it simply adds the periodic time (e.g. 24 hours) to the last time a check was done.
My ISP has changed their broadband usage system so that half of my monthly transfer allowance is "off-peak" (from next month, 2am to 10am). This really doesn't suit me well, as I typically spend only about an hour to two hours (8am or 9am to 10am) of this time online, so what I end up with is a huge chunk of unused allowance, and maxing out my "peak" allowance.
I don't want to change my habits so that I schedule everything for download. The point of having broadband was that I got what I wanted when I wanted it. The exception to this is podcasts, which are all time-shifted anyway, so I don't care when they download. They also account for a reasonable portion of my downloads (in terms of size - particularly the two video podcasts). So I really want these to download these around 4am.
One way to do this would be to get up at 4am one day and manually update. However, I like my sleep. That also means that if I ever decided to 'check now', I'd have to redo this.
So, my solution is to write a little Python script that tells iTunes (via COM) to update all podcasts, set iTunes to only update manually, and have Windows run this Python script as a scheduled task. If you want to do anything with this script, help yourself (it's really only 6 lines).

```
#! /usr/bin/env python
"""Tell iTunes to update all podcasts."""
import win32com
import pythoncom
import win32com.client

def main():
    pythoncom.CoInitialize()
    app = "iTunes.Application"
    iTunes = win32com.client.Dispatch(app)
    iTunes.UpdatePodcastFeeds()

if __name__ == "__main__":
    main()
```

technorati tags: [itunes](http://technorati.com/tag/itunes), [podcasts](http://technorati.com/tag/podcasts), [time](http://technorati.com/tag/time)
