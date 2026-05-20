---
title: "GitHub \"sync fork\" silently failing"
date: 2024-03-03T10:40:26+12:00
slug: "github-sync-fork-silently-failing"
categories:
  - "Tools"
  - "Work"
---
*(Post theme: [Oops! I Did It Again by Britney Spears](https://music.apple.com/nz/album/oops-i-did-it-again/267954486?i=267954487))*

Posting because I've hit this three times now and each time not remembered the solution until I figured it out again, in the hopes that writing it down will prompt my memory next time and avoid a fourth "figure it out fresh" cycle.

At [work](https://canonical.com/) (in the team I'm on), we develop in the open using [public Github repositories](https://github.com/orgs/canonical/repositories). To introduce a change, we fork the repo, create a branch, and submit pull requests to the upstream main branch.

As changes make their way into main, it's handy to be branching off an up-to-date fork, and GitHub has a convenient "sync fork" tool in the web UI to do this. Most of the time, this works perfectly. Unfortunately, a few times I've tried to sync and it silently fails (the cause is user error, but the silent nature of the fail is very poor UX from GitHub, and I feel like they could actually make the whole process work, which would be ideal UX).

The reason it has failed (each time it has happened to me) is that [branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) is enabled for the main branch *on the fork*. I've enabled this to avoid accidentally pushing changes to main (forgetting to create a branch first), which I never want to do - *except* for pulling in upstream changes.

There might be a simpler way to work around this (other than opening a PR from upstream main to the fork main) but I just disable the protection, sync, then enable it again.
