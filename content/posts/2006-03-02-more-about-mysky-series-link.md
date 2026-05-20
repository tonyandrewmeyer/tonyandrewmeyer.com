---
title: "More about MySky Series Link"
date: 2006-03-02T12:09:04+12:00
slug: "more-about-mysky-series-link"
categories:
  - "MySky"
---
In the [comments](http://tonyandrewmeyer.wordpress.com/2006/02/09/on-the-subject-of-mysky/#comments) to an [older post](http://tonyandrewmeyer.wordpress.com/2006/02/09/on-the-subject-of-mysky/), John Porter passed on a very interesting email about how the MySky Series Link feature is implemented.
> Series Link works quite simply. In the XSI (metadata) information transmitted to the EPG there is a single field for âseries IDâ which links together programmes in a series. There is also a âlink flagâ field: if this is set then the green button will be displayed by the planner to enable a series link to be requested. The difficult part for us is in attaching series IDs to programmes and in separating out repeat showings. SKY is linking programmes on SKY-originated channels as quickly as possible. On channels sourced from outside SKY we are at the mercy of the data provided to us.

This is a poorly designed system. For a start, there doesn't need to be a link flag; the system should look to see if there is data in the series tag, and if there is then display the "series link" option, and if not, not display it. More importantly, the problems they are having would be avoided if they had three fields/tags: series_id, season_id, and episode_id. This would allow them to link all episodes in a season, or all episodes in a complete series, and would easily allow filtering of duplicates. Whoever does their design needs some basic training.
Manually identifying episodes is also a terrible idea, and will lead to continued problems. I presume that they have the name of the series and the name of the episode available in other fields/tags. Complete episode lists are available for every series ever made - they just need to do a simple table lookup to fill in this data. Do they employ anyone with any software engineering skills at all?
The email continues:
> There are two issues which the customer seems to have run into:
> 1) We have had a problem that the decoder will record the first programme in a series then fail to book recordings for any other future programmes in any series. This can be fixed by rebooting the decoder and does not seem to recur. (At present if you reboot while you have a PPV movie recorded in the planner you will lose the movie so avoid rebooting in this situation).

I've never come across this one myself. It continues:
> 2) We have another problem on TV1, TV2 and SKY Sports 1,2 and 3 that the decoder will display âsearchingâ? on future bookings. This is due to duplication of services within our transmission. SKY Sports services have been duplicated to create one service for legacy decoders (with SKY bet) and another for MY SKY (without SKY bet which has a bug). We hope to upload a new software version very soon which will enable us to use SKY bet on the PVR and so eliminate the Sports services duplication and the âsearchingâ? error. The same error message occurs on TV1 and TV2 because of the multiple copies transmitted for regionalization. In this case the PVR is supposed to cope with the duplication but does not â we are looking for a solution with the software provider.

"software provider" is interesting. So it appears that they don't do any of the software development themselves. It would be interesting to know whether it's just the same software as used in the UK/Australia or if they have contracted this work out to someone local (if so, it would be good to know who, so that we could all avoid using their inferior service).
The worst part of this is that this email says that they are working on fixing this series link problem (but not any estimated date for the solution) but I have never been told that, in the many emails I have had from Sky. Did the person that sent this know more? Were they making it up? Does anyone at Sky know *anything* about MySky?
technorati tags: [SkyTV](http://technorati.com/tag/SkyTV), [MySky](http://technorati.com/tag/MySky)
