---
title: "Delicious Library queries via SMS"
date: 2006-11-28T18:20:34+12:00
slug: "delicious-library-queries-via-sms"
categories:
  - "Tools"
---
A few months ago, I finally got around to cataloging all my books using [Delicious Library](http://www.delicious-monster.com/). There were a few reasons for doing this - [my insurance company](http://www.state.co.nz/) wants a list of all the books in order to insure them for new-replacement value (rather than the few cents they probably consider they are worth), if anything did happen to them, I want to be able to print out a list and give it to a bookstore with an insurance cheque an wait for all the boxes to arrive, and, perhaps most importantly, it's becoming difficult to purchase new books because I have to remember whether I've already got the book (or have just read it, or have just heard of it). It's also just about impossible for anyone else to buy me a book (my favourite gift), because I might already have it (unless it's on my [Amazon](http://amazon.com/) [wish-list](http://www.amazon.com/gp/registry/wishlist/24BWRXYO4KVFG/), which I keep fairly up-to-date). I guess it's also nice to keep track of books I've lent out, but that isn't so common that I need software for it.
Just putting the books in the Delicious database covers most of these, apart from the issue of avoiding purchasing duplicates. Delicious Library can sync to an [iPod](http://www.apple.com/itunes/) (I don't have one, but my wife does, so with a bit of work copying the library across accounts, that can be done), so that somewhat solves the issue of buying duplicates myself. It's not perfect, though - for a start, I need to ensure that I have the iPod with me (easy to do for planned purchases, but not impulse buys). In addition, it seems that only 1000 books were sync'd - I'm not sure if the iPod is limited in the length of "notes" it can display, or if Delicious Library is limited in the number of books it can sync, or if something just went wrong in the process. This doesn't at all help anyone else, of course, unless I give them a list.
Putting the list online is possible, through third-party utilities, but the one that I found that worked resulted in [a page with so many images it would take forever to load](http://tangomu.com/books/), and while I put [a custom-made version](http://tangomu.com/books.html) online that would load more quickly, printing the list out and taking it with you, or waiting until you could look at it online, isn't particularly practical.
What I needed was a way to query the list using something that I and others would always have on hand. That's really only a cellphone, either via voice (complex) or SMS (simple). [ipipi](http://ipipi.com), which I used in the past to send SMS messages from a computer, allows me to receive email from an SMS, which I could use to trigger an Applescript. While I could probably have done the whole job in [Applescript](http://www.apple.com/macosx/features/applescript/), writing the search in [Python](http://python.org) was much simpler.
Originally, the plan was to only respond via SMS if my laptop was at home, because only [Skype](http://skype.com) for [Windows](http://www.microsoft.com/windows) allowed sending SMS messages, and so I had a rather complex script half written that would switch the input device and use text-to-speech over a Skype voice call if the laptop wasn't available. Happily, the latest beta of Skype for [OS X](http://www.apple.com/macosx/) does allow SMS sending, so the response is always via SMS now.
I don't know if this will be of use to anyone, and it's pretty simple stuff (this is why scriptability is good - if Delicious Library had proper scriptability, I wouldn't have to bother with the Python script at all), but here it is:
`using terms from application "Mail"
on perform mail action with messages theMessages for rule theRule
tell application "Mail"
repeat with thisMessage in theMessages
set msgSource to source of thisMessage
try
do shell script "echo " & quoted form of msgSource & "| /Library/Frameworks/Python.framework/Versions/Current/bin/python2.5 /Users/tameyer/book_sms.py"
on error errMsg number exitCode
display dialog "Something unexpected has happened to search: Exit Code = " & exitCode
display dialog "Error Message:" & errMsg
end try
end repeat
end tell
end perform mail action with messages
end using terms from`

```
import sys
import email
import string
import xml.etree.cElementTree as et

def parse_msg(fp):
    msg = email.message_from_file(fp)
    # Subject will look like "SMS from +6421XXXXXX"
    to = msg["Subject"][9:]
    # Body will be the title to look for.
    search_for = msg.get_payload().strip()
    return to, search_for

table = ""
for i in xrange(256):
    if chr(i) in string.letters:
        table += chr(i)
    else:
        table += " "
def normalise(text):
    return text.translate(table).replace(" ", "").lower()

if sys.platform == "win32":
    library = "Library Media Data.xml"
else:
    library = r"/Users/tameyer/Library/Application Support/Delicious " 
              r"Library/Library Media Data.xml"

def find_book(search_text):
    search_text = normalise(search_text)
    tree = et.parse(library)
    matches = []
    for item in tree.getroot().find("items"):
        if item.tag != "book":
            continue
        title = item.attrib.get("title")
        if not title:
            continue
        try:
            title = title.encode("latin-1")
        except UnicodeEncodeError:
            continue
        norm_title = normalise(title)
        if search_text in norm_title:
            matches.append('"%s"' % (title,))
            # Limit the response to one SMS.
            if len(" ".join(matches)) > 160:
                matches.pop()
                break
    if not matches:
        return "No matches found"
    return " ".join(matches)

if sys.platform == "win32":
    import win32com
    import win32com.client
    def sendsms(to, msg):
        skype = win32com.client.Dispatch("Skype4COM.Skype")
        result = skype.SendSms(to, msg, "+64211430994")
        return result.Status != win32com.client.constants.smsMessageStatusFailed
else:
    import appscript
    def sendsms(to, msg):
        app = appscript.app("Skype")
        result = app.send(command="CREATE SMS OUTGOING %s" % (to,),
        script_name="CreateSMS")
        sms_id = result.split()[1]
        app.send(command="SET SMS %s BODY %s" % (sms_id, msg),
                  script_name="BodySMS")
        app.send(command="ALTER SMS %s SEND" % (sms_id,), script_name="SendSMS")

if __name__ == "__main__":
    to, search_for = parse_msg(sys.stdin)
    msg = find_book(search_for)
    result = sendsms(to, msg)
    sys.exit(result)
```

technorati tags:[Delicious Library](http://technorati.com/tag/delicious_library), [Applescript](http://technorati.com/tag/Applescript), [Python](http://technorati.com/tag/Python), [books](http://technorati.com/tag/books), [Skype](http://technorati.com/tag/Skype), [SMS](http://technorati.com/tag/SMS), [ipipi](http://technorati.com/tag/ipipi)
