---
title: "Review: Become a SELECT Star - Wizard Zines"
date: 2024-12-02T17:04:54+12:00
slug: "review-become-a-select-star-wizard-zines"
tags:
  - "review"
  - "sql"
  - "zine"
---
*(Post theme: [Call Off the Search by Katie Melua](https://music.apple.com/nz/album/call-off-the-search/292453099?i=292453154&l=en-GB))*

As part of my training allowance for 2024, I purchased all 14 of [Julia Evan](https://jvns.ca/)'s [zines](https://wizardzines.com/). There are definitely ones I expect to learn from more than others, but having the pack appealed, and one of the things I really enjoy about her posts is finding little tidbits of information that I didn't know, even though I would have said I know the topic fairly well in general.

First up: *Become a SELECT Star*, which, as you'd guess from the title, is all about the SELECT statement in SQL. The first dozen pages are a really good summary of the fundamentals: things that I gradually absorbed over the last 20 or so years, and probably would have been better off with having a summary like this rather than a bunch of more traditional reference material.

I really like how the examples work through the query in the logical order rather than the syntax order. It makes it much simpler to follow what's happening.

On pages 14-16, it covers window functions, which I didn't really know at all. I would normally just do this by getting a bunch of the data down into something like Python and calculating there. I'm a big fan of moving computation left where possible, so these seems super useful, and something I hope I remember (although I don't do a huge amount of SQL these days).

The zine continues on to cover NULL and COALESCE, which we used a lot at SpamExperts, so those were pretty familiar, but again a good summary that I could have used many years back! It then covers CASE, and I don't remember if I knew that or not, but also don't think I can think of times I would have wanted it directly in SQL.

After a straightforward page on counting rows, it moves into subqueries. I've used these quite often (I've often had situations where subquery performance was better than joining, for various reasons). However, common table expressions (naming sub queries) is new to me, and look super useful.

It wraps up with a few more useful tips, most of which were things I already knew.

I'd definitely recommend this to anyone that's just starting with SQL. If you're a SQL expert, it's likely not going to be useful, but if you're a casual querier like myself, then there are good tips to pick up, and given how small and inexpensive the zine is, I'd highly recommend picking it up.
