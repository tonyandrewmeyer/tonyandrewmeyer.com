---
title: "Sleep Cycle Alarms for Two"
date: 2011-01-05T18:40:52+12:00
slug: "sleep-cycle-alarms-for-two"
tags:
  - "development"
  - "idea"
  - "ios"
  - "sleep"
  - "sleep cycle"
---
My body clock works well - I almost always wake up each morning on time, feeling refreshed and well rested.  I only use an alarm when there's something I absolutely can't be late for, and even then I set the time to be the last possible moment because I'll always wake up before it goes off [1].
If this was also true for Olyvia, there would be no problem.  If I wake up before her, she doesn't wake up - I quietly spend 30 minutes or so going over [email](mailto:tony.meyer@gmail.com), news, [FaceBook](http://facebook.com/tonyandrewmeyer), [Twitter](http://twitter.com/tonyandrewmeyer), work, etc in bed, and even if I get up before her it's unlikely to wake her up.  Unfortunately, Olyvia does not wake up well naturally, and so she does use an alarm whenever she needs to get up at a particular time (which is often at the moment).
Recently, she has started using [an iOS app to wake her (with an alarm) at the ideal point in her sleep cycle](http://mdlabs.se/sleepcycle/) (i.e. the app is helping her do what I do naturally).  She says that this works extremely well for her.  Unfortunately, I believe it does work, because it's waking me up too and I feel terrible (I'm clearly **not** in the right state to be waking up).
[![](http://imgs.xkcd.com/comics/cant_sleep.png)](http://xkcd.com/571/)
It seems a significant flaw in these sorts of applications - whenever you wake up the user, it's quite likely to be a poor time to wake up whoever they are sleeping with (unless there's some sort of odd synchronising of sleep cycles that I am unaware of).
However, this seems easy to solve (and if anyone can take this idea and implement it, please do so - free! - so that I can sleep well again).  iOS provides simple-to-use APIs for communicating with other local iOS devices.  I, like many people, have many iOS devices lying around.  If you can solve the "when to wake" problem given a fixed point and a sleep state, it seems likely that solving the problem given two sleep states (presumably overlapping somewhat at times) and a fixed point cannot be too difficult (probably less optimal, but better two near-winners than a winner and a loser).
This would be simple to use - you set the alarm to coordinate with another local device, and when it is ready to wake you up, it confirms with that device first.  They negotiate the ideal time given the two sleepers, and the alarms go off simultaneously (I'd set my alarm to silent since I don't need it).  They can communicate with Bluetooth or WiFi, whichever is less likely to fry my brain by having it under the pillow.
