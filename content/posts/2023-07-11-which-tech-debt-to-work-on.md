---
title: "Which Tech Debt to Work on?"
date: 2023-07-11T20:28:59+12:00
slug: "which-tech-debt-to-work-on"
draft: true
---
*(Post Theme: [Death By A Thousand Cuts by Taylor Swift](https://music.apple.com/nz/album/death-by-a-thousand-cuts/1468058165?i=1468058185))*

If we start with some assumptions around technical debt, such as:

- [Tech debt as a concept is something that exists, within some sort of definition](https://ieeexplore.ieee.org/document/9585142);
- Every project will build-up tech debt, starting essentially immediately;
- Some tech debt is worth having, because resources are not infinite;
- It's worth investing some regular engineering time to removing some existing tech debt;
- Someone in the team is able to identify tech debt in the project;

then the questions that naturally arises are how to choose which tech debt to work on (which code, or perhaps processes, to improve, and how much of it given a time period). The latter question (how much) I'll leave for another day, but before we get to that, we need to essentially create a prioritised backlog of tech debt.

In my experience, there are three key identifiers of work that is worth doing sooner: something that gets harder to solve over time, something that slows down work that's important to do now, and the stereotypical low-effort/high-value work.

## Harder to solve over time

Sometimes, tech debt becomes easier to solve over time; for example: difficult to maintain code that's needed for performance is no longer required because compute/memory decreases in cost; a problematic subsystem is no longer required because of changing business needs or because a third-party service can be used instead; or new language/library/framework features remove the need for complicated workarounds.

If you're able to see these changes coming - at least vaguely, or that there's a strong possibility of them - then these are good examples of tech debt that should *not* be worked on. Just like a no-interest loan will get smaller without any repayments (in real terms) due to inflation, the tech debt also reduces without any specific effort.

Most of the time, the amount of work required stays fairly constant. Assuming that the issues are fairly isolated, improving the code (or processes) is roughly the same complexity if you do it tomorrow or you do it next year. It's generally best to leave these improvements until they hit some other criteria.

The cases you want to target are the ones where removing the tech debt gets *more* difficult over time.

A classic example of this is where it's part of a public API (even if "public" is only for your users). An API that's only consumed internally - even if it's by multiple teams across multiple products - can have updates forced, with minimum or even no backwards compatibility period (as long as you can get buy-in from the right person). With a public API, however, you've got a bunch of people using the existing system and this comes with a host of difficulties, such as:

- **Who is using it?** Maybe you can determine this via logs or authenticated access, or similar, but that's not always the case.
- **How do you inform everyone that's using it that they need to make changes?** Release notes are critical but also not widely read. Deprecation warnings when using an API can work well but are also often funnelled into a logging system that no-one ever looks at.
- **How do you convince people that it's worth making the change?** For a lot of them, the existing system is probably working perfectly fine (you're solving tech debt, not introducing user-facing improvements). Requiring this change is essentially *creating* tech debt for your users. You can simply force them to by making the new way the only way, but you'll almost certainly break at least some API use, and make at least some of your users unhappy that they have to pick up this extra work.
- **You're going to have to have some sort of backwards compatibility period.** Backwards compatibility code is also tech debt, so you've really just transmuted a bunch of it rather than removed it (and transferred some of it to your users). How long do you need to keep this around (hint: far longer than you think), how much of a problem is it going to be maintaining it, and how do you figure out when you can finally remove it?

It's obviously far easier to do this when you have a handful of API users than when you have hundreds, millions, or some unknown number. It's worth prioritising the clean-up work while it's (comparatively) simpler to do - remembering that this only applies to the actual API and not implementation details that don't impact the API.

There are other cases like this as well; for example: code that *isn't* nicely isolated, so over time the problems spread into more and more parts of the system; processes that are used by entire teams and get engrained as the team sizes grow; or code that relies on software or hardware that is going to be discontinued without a clean upgrade path.

A lot of these situations are predictable - at least by the more senior engineers who are familiar with your project - and should be strong candidates for being resolved as soon as possible.

## Problems that slow you down

A second form of tech debt that's worth concentrating on is code or processes that make your team less productive.

## Low effort, high value

There's definitely value in working on tech debt even when you don't have any that fall into the above categories. The financial analogy falls away a bit here, in that you can't really say that you have a specific range of leverage that's acceptable, and I don't really believe it's common for projects to fail because of the amount of tech debt (before you get to that point, some of the drivers increasing it will have contributed to earlier failure). However, your engineering team will be happier if there's regular clean-up, and you do avoid small problems becoming larger ones.

The obvious way to prioritise here is much like the obvious (not only!) way to prioritise user-facing improvements: map the possibilities on an axis of amount of work/complexity (whether that's t-shirt sizing or person-hours or story points or whatever else), and an axis of value (which in this case is probably going to be highly subjective, so you should just go with the average judgement of the people you trust most).

High value, high effort work can be worth doing, but you probably want to find some way to break it down or get it to be less effort or tie it to specific business goals. Low value, low effort work doesn't have to be avoided, but there's almost certainly something else that people could be better spending their time on. This sort of work can sometimes be good for people new to a project as a way to get familiar with the project, code, and processes.

High effort, low value work is the obvious work to avoid. The big challenge here is how "value" is defined, of course - something that often falls into this area is polish, where making something really perfect will be noticed by almost no-one and make no difference to the business goals. Sometimes the value is simply in how it makes you feel, knowing that you've put in the effort - this is much easier in solo or passion projects. Marco Arment and David Smith talk about this type of work in [a recent Under the Radar episode](https://overcast.fm/+FgnZqN2Zc).

Clearly, the work to target first, most of the time, is the items that fall into the high value, low effort quadrant.
