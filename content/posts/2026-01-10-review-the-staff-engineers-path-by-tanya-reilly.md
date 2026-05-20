---
title: "Review: The Staff Engineer’s Path by Tanya Reilly"
date: 2026-01-10T16:25:52+12:00
slug: "review-the-staff-engineers-path-by-tanya-reilly"
---
*(Post theme: [something to my something (feat. Maddy Low) by FDaSavage](https://music.apple.com/nz/album/something-to-my-something-feat-maddy-low/1867696063?i=1867696068&l=en-GB))*

Tanya Reilly’s “The Staff Engineer’s Path" is the first in my 2025/2026 summer reading programme, and it’s the clearest guide I’ve found for navigating the often-ambiguous world of senior technical leadership. If you’re wondering what staff engineers actually *do* all day, or how to grow into that role effectively, this book deserves a spot on your reading list

## What Makes This Book Different

Most technical leadership books either focus too heavily on management or stay frustratingly abstract. Reilly strikes a better balance, addressing the messy reality of being a senior IC: you’re expected to have broad impact, but nobody’s quite sure how. One highlight that captured this perfectly was her observation that staff engineers “take on ambiguous, messy, difficult problems and do just enough work on them to make them manageable by someone else.” That’s the job in a nutshell.

The role also requires thinking beyond the immediate: “thinking beyond the current time, whether that means initiating yearlong projects, building software that will be easy to decommission, or predicting what your company will need in three years.”

## Building Your Mental Maps

The “Three Maps” chapter was a standout for me. Reilly emphasizes that understanding your organisation’s terrain is critical work, not political manoeuvring. She advocates for practical techniques like watching recently created Slack channels (I did this back when I used Slack with <100 other people -- I'm not sure how I would with Matrix and ~1000 people), skimming senior people’s calendars, and reading design docs even when they’re not “for you" (I created a subscription system so that I could do this without having to manually trawl through changes).

> “I asked on Rands Leadership Slack about how everyone approaches knowing things, and a common thread was paying attention to information that isn’t secret exactly, but isn’t necessarily for you. This included reading senior people’s calendars, skimming agendas or notes for meetings you’re not in, and—something that had never occurred to me—looking at the full list of Slack channels sorted by most recently created so you can see what new projects are happening.”

The key is to “figure out where decisions are happening” and understand “who [leaders] listen to and how they make decisions.”

I particularly appreciated her reference to *gemba* from Lean manufacturing—the practice of walking the floor to see how things actually operate. It’s a useful mental model for why we should be deploying and running our own software rather than just writing it (I'm mostly missing this right now, and aim to change that over the next 6 months).

Once you understand the terrain, Reilly notes, “The more you know the terrain, the easier it will be to bridge gaps by sending the email summary nobody is sending, introducing two people who should have spoken a month ago, or writing a document to show how projects connect to each other.”

## Vision and Strategy

On creating technical vision, Reilly is pragmatic: “Writing technical vision or strategy takes time. If you can achieve the same outcome in a more lightweight way, do that instead.”

When you do need to build consensus, she introduces the concept of *nemawashi* from the Toyota Production System—“sharing information and laying the foundations so that by the time a decision is made, there’s already a consensus of opinion.” Or as she puts it more directly: “Don’t call for a vote until you know you have the votes.”

## Time and Energy Management

The chapter on finite time hit home. Reilly is refreshingly direct:

> “You have to make peace with walking past things that are broken or suboptimal (or just really annoying) and taking no action.”

This isn’t permission to ignore problems—it’s recognition that at the staff level, choosing what *not* to work on is as important as choosing what to tackle. She encourages you to “understand what kinds of work are expensive for you, and what kinds will leave you with some smartbrain at the end of the day.”

Before taking on a project, she suggests asking yourself: “Do any of the people you’ll work with leave you exhausted every time you talk to them?” It’s a practical filter I hadn’t considered explicitly before, but have certainly experienced.

By this point in your career, “you will be largely (but probably not entirely) responsible for choosing your own work.” Part of that responsibility includes finding ways to “free up your resources by giving other people opportunities to grow, including starting projects and handing them off.”

## Leading Big Projects

When facing a daunting project, Reilly offers reassurance:

> “The job here is to be the person brave enough to make—and own—the mistakes. You wouldn’t have gotten to this point in your career without credibility and social capital. A mistake will not destroy you. Ten mistakes will not destroy you. In fact, mistakes are how we learn.”

Her approach to feeling overwhelmed is practical: “use your core muscles. If you’re most comfortable with code, jump in. If you tend to go first to relationships, talk to people. If you’re a reader, go get the documents.”

On design work, she advocates for being concrete over being safe:

> “But it’s a better use of your time to be wrong or controversial than it is to be vague. If you’re wrong, people will tell you and you’ll learn something, and you can change direction if you need to.”

And she’s firm about scope creep: “‘We might need it later’ is not a good enough justification.”

For those worried about spending time coding at this level, she quotes another engineer: “If spending a day a week coding keeps you engaged and excited to come to work, you will likely do better in the rest of your job.”

## Unsticking Projects

When blocked by other teams, Reilly emphasises gratitude and making things easy:

> “If someone goes out of their way to help you, say thank you. In companies that have peer bonuses or spot bonuses, there’s already a structure for saying thank you: use it.”

Structure your requests so they’re “easy to say yes to, with as little reading needed as possible.”

On migrations and technical debt, she’s direct about the impact: “The half-migration slows down everyone who has to engage with it. This is a place where a staff engineer can step in and have a lot of impact.”

And remember: “there is no such thing as a temporary solution.”

For documenting decisions, she recommends “Lightweight Architectural Decision Records for showing why you made the choice you did". We noticed other teams at Canonical using these and considered adopting them, but decided against it for now.

## Being a Role Model

The chapter on being a role model contains some of the book’s most quotable wisdom. On competence, Reilly writes:

> “Competence is built on knowledge and experience, but you also need to be able to apply those abilities. That starts with the self-awareness to know what you can do, how long it will take, and what you don’t know.”

She pushes back against imposter syndrome: “Being competent doesn’t mean you need to be the best. I’ve sometimes seen tech people be shy about claiming to be an expert, because they can always think of someone in the industry who is better than they are. Don’t set your bar at ‘best in the industry.’”

And crucially: “Admitting ignorance is one of the most important things we can do as tech leads, senior engineers, mentors, managers, and other influencers of team culture". I have long pushed this myself, not only in these fields but as an educator as well. (Fascinatingly, it's one area where current AI is *terrible*.)

On standards:

> “Your standards will serve as a model for how other people work. Know what high-quality work looks like and aim for that standard in everything you do, not just the parts you enjoy most. Write the clearest documentation you can. Be the first person to know if your software breaks.”

She emphasises that feedback makes your work better: “Your solutions are not you and they don’t define you. Criticism of your work isn’t criticism of you.”

When someone brings you a problem, her advice is to “stay calm. Ask questions. Understand why they’re telling you. Do they just need to vent? Are they hoping you’ll take action?”

She shares a story about making a production mistake early in her career and a colleague’s response: “It’s always interesting to see how new people handle their first screw-up. We’ve all been there.” Then she reflects: “Tim took the time to be kind.”

On team dynamics, she reminds us:

> “While you may be the best coder on the team, the most experienced engineer, or the fastest problem solver, that doesn’t mean you should jump on all of the problems. You’re working as part of a team, not a collection of competing individuals. Don’t become a single point of failure where the team can’t get anything done when you’re not available.”

## Future-Proofing Your Work

Reilly emphasises thinking ahead:

> “So take the time to leave your production environment, codebase, or documentation so that it just works for whoever comes along next. Write tests that will let you refactor your code without breaking things. Follow your style guide so that the people who copy your approach will also be following your style guide.”

She warns: “Every time someone leaves your company, you lose institutional knowledge. If you’re lucky, you have some old-timers storing history in their brains. But eventually, inevitably, you’ll have complete staff turnover.”

And on designing for the long term: “The system will never again be as well understood as it is on the day it’s created.”

She quotes Martin Fowler: “Any fool can write code that a computer can understand. Good programmers write code that humans can understand.”

## Teaching and Influence at Scale

Reilly distinguishes between giving advice and actually teaching: “What’s the difference between telling people things and teaching them things? Understanding. When you’re giving advice, you’re explaining how you relate to the topic, and the receiver can take your advice or leave it. When you’re teaching, you’re trying to have the other person not just receive the information but internalise it for themselves.”

For hands-on teaching: “Successful teaching includes hands-on learning and activating knowledge: the student should be doing as well as listening.”

On delegation, she advocates for messiness:

> “your colleagues won’t learn as much if you only delegate the work after you’ve turned it into ‘beautifully packaged, cleanly wrapped gifts.’ If you instead give them ‘a messy, unscoped project with a bit of a safety net,’ they’ll get a chance to hone their problem-solving abilities, build their own support system, and stretch their skill set.”

Before offering unsolicited advice: “Before you offer your thoughts, think about whether the other person is asking for them. Think too about whether you even have enough context to tell them something that’s both helpful and nonobvious.”

And if you really want to share: “If you’re itching to give unsolicited advice on a topic nobody is asking you about, consider writing a blog post or tweeting about it instead.”

## Career Growth

The final chapter acknowledges that specialisation often happens accidentally: “In fact, it’s easy to gain a specialty accidentally just because it’s what you’re doing at work: one experience leads to another, and next thing you know you have a specialization.”

But she also normalises staying put if your current role is working:

> “If your job is giving you what you need, there’s no need to change anything. I want to emphasize that because our industry puts a lot of focus on changing jobs frequently, and the regular ‘new job’ announcements can make you feel like you should be moving too.”

And success can mean different things, including working less: “Success can mean working less in your current role. One engineer I spoke with, Jens Rantil, swapped a staff engineering role for 80% time and a 20% pay cut at a much smaller company. As he said, ‘Every Thursday is a Friday! It’s amazing!’”

On finding your next role, she quotes Graham: “I’ve found that people that know you well are always going to be the ones that find you the phase 2 roles that are ‘shaped like you.’ People that don’t know you are always going to offer you the job you just had". I've experienced this, too.

## Small Touches I Loved

- “I recommend playing Civilization to understand all things about staff engineering. Tell your boss it’s research.”
- “Being the grizzled, experienced best supporting actor is an amazing role.”
- “In general, if there are more people being the wise voice of reason than there are people actually typing code (or whatever your project’s equivalent is), don’t butt in.”
- The clearest indicator of what a company values: “what gets people promoted.”
- “Think of it as a Ship of Theseus: every individual component may get replaced over the years, but the fundamental system continues. It’s all metaphysical architecture.”

## Should You Read It?

Yes. Whether you’re already a staff engineer trying to figure out the role, or an ambitious senior engineer wondering what’s next, this book provides both frameworks and practical tactics. Reilly’s writing is clear, honest, and grounded in real experience. She acknowledges the uncomfortable parts of the job—the politics, the ambiguity, the need to let some things stay broken—without being cynical about them.

The book won’t give you a prescriptive checklist (staff engineering doesn’t work that way), but it will help you build better mental models for navigating technical leadership. As Reilly reminds us, by this level you’re largely choosing your own work—this book helps you choose wisely.

*(You can also see my [full set of highlights](https://htmlpreview.github.io/?https://github.com/tonyandrewmeyer/tonyandrewmeyer/blob/main/reading-notes/The%20Staff%20Engineer%27s%20Path_%20A%20Guide%20for%20Individual%20Contributors%20Navigating%20Growth%20and%20Change%20-%20Notebook.html) if you'd like).*
