---
title: "Corrections to JGC's Spam and Anti-Spam Newsletter #37."
date: 2006-08-08T22:56:13+12:00
slug: "corrections-to-jgcs-spam-and-anti-spam-newsletter-37"
categories:
  - "Work"
---
In [John Graham-Cumming](http://www.jgc.org/)'s [Spam and Anti-Spam Newsletter](http://lists.beasts.org/mailman/listinfo/antispam-news) #37, John printed comments from Gordon Cormark regarding the [TREC](http://trec.nist.gov/) 2005 [Spam Track](http://plg.uwaterloo.ca/~gvcormac/spam/) submissions:
> Several submitted by participants have their heritage in a filter product, but are experimental in the sense I mentioned above, and not available for download or purchase: [...] tamSPAM (spambayes as configured by Tony Meyer)

However, this is not correct. I emailed John the comments below, but it seems he didn't feel they were worthy of including in later issues. This doesn't bother me (it's a minor enough thing), they got lost in his mail. They'll be in a later issue, but for the record, I'll reproduce them here.
[SpamBayes](http://spambayes.org) isn't available for purchase (free, free, free!), but is available for download. The only difference between [the submissions for TREC 2005](http://www.massey.ac.nz/~tameyer/research/spambayes/) and spambayes-1.1a1 is that the former included the TREC scripts (initialize, classify, train, finalize) and modified one server script to output the classification in the TREC format (to save time by avoiding post-processing).
In fact, tamSPAM1 is "all defaults" spambayes-1.1a1; if you download SpamBayes and don't touch the configuration, you'll get the same results as tamSPAM1. The one "except" is that SpamBayes is a "ham/unsure/spam" classifier, and TREC needs a "ham/spam" judgement, so the cutoffs were set to the same value. The scores will be identical, however, which in my opinion makes tamSPAM1 exactly the same as spambayes-1.1a1.
tamSPAM2 simply turns on an option that a large proportion of SpamBayes users use, and changes to a 'train on errors' system that most SpamBayes users use (and we recommend). tamSPAM3 uses a training system that is included in spambayes-1.1a1, but is not widely used, and tamSPAM4 does likewise, but also turns on all available options.
So the tamSPAM submissions are all really available for download; only TREC-specific material was added to the submissions.
