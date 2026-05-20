---
title: "Trac to iCal"
date: 2011-01-13T12:05:38+12:00
slug: "trac-to-ical"
categories:
  - "Python"
  - "Tools"
  - "Work"
tags:
  - "ical"
  - "icalendar"
  - "project management"
  - "trac"
comment_id: "257"
comment_count: 1
---
One project I work on uses [Trac](http://trac.edgewall.com) and has a custom "due date" field (it doesn't really have milestones - updates are more granular).  While this is useful, one problem is that I don't check this Trac instance every day, and so sometimes I've missed deadlines because I haven't noticed that they are due.  However, I do check my calendar every day (multiple times a day).  It seems like exporting this "due date" value into my calendar will help with this.
This little script creates a calendar that can be subscribed to.  I run it once a day (due dates don't change very often), and have iCal set to update once a day, so it should work fine.  If it's of use to you, use it (no restrictions).  Let me know if there are things that can be improved!  It requires the Python [iCalendar](http://codespeak.net/icalendar/) module, which I already use for parsing public holiday data.

```
#! /usr/bin/env python

import sqlite3
import datetime

import icalendar

cal = icalendar.Calendar()
cal.add("prodid", "-//PROJECT NAME Trac Deadlines//trac.tonyandrewmeyer.com//")
cal.add("version", "2.0")
cal.add("method", "publish")
cal.add("x-wr-calname", "PROJECT NAME Ticket Due Dates")
cal.add("x-wr-caldesc", "Due dates for PROJECT NAME tickets")
db = sqlite3.connect("/trac_location/db/trac.db")
c = db.cursor()
c.execute("select t.id, t.owner, t.summary, c.value from ticket t, "
           "ticket_custom c where t.id=c.ticket and t.status!='closed'")
for ticket_id, owner, summary, due_date in c.fetchall():
    if not due_date:
        continue
    due_date = datetime.datetime.strptime(due_date, '%d/%m/%Y')
    due_date = datetime.date(due_date.year, due_date.month, due_date.day)
    event = icalendar.Event()
    event.add("summary", "PROJECT NAME #%s (%s): %s" % (ticket_id, owner, summary))
    event.add("dtstart", due_date)
    event.add("dtend", due_date)
    event.add("dtstamp", datetime.datetime.now())
    event.add("url", "https://trac.tonyandrewmeyer.com/ticket/%s" % ticket_id)
    event["sequence"] = datetime.datetime.now().strftime("%Y%m%d%H%M")
    event["uid"] = "ticket_due_%s@trac.tonyandrewmeyer.com" % ticket_id
    cal.add_component(event)
c.close()
db.close()
open("/var/www/subfolder/project-name-trac-due.ics", "wb").write(cal.as_string())
```
