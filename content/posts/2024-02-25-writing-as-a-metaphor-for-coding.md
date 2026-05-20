---
title: "Writing as a metaphor for coding"
date: 2024-02-25T23:59:25+12:00
slug: "writing-as-a-metaphor-for-coding"
categories:
  - "Work"
---
At [work](https://canonical.com/), our book club is reading [Code Complete](https://www.goodreads.com/book/show/4845.Code_Complete), and had our first discussion session today. I first read this in early 2011 - roughly 6 years into professional software development - and remember thinking quite positively of it at the time. We're only three chapters in, but I'm decidedly more mixed on it this time around - I've had a lot more varied experience with development projects than in those early years, and a lot of the book lands quite differently (I do suspect that the later chapters will have stood the test of time better).

The second chapter of the book is focused on the importance of choosing a metaphor for software development - it ends strongly suggesting that building construction is an elegant metaphor. I agree that metaphor can be useful (but is also easily overused, and people get fixated with the imperfection of the chosen metaphor - "But if you extend them too far or in the wrong direction, they'll mislead you", as the author says) and that construction can work as one for software development.

However, the author, says:

> For an individual's work or for small-scale projects, the letter-writing metaphor works adequately, but for other purposes it leaves the party early—it doesn't describe software development fully or adequately.
>
> Steve McConnell, Code Complete, Chapter 2 "Software Penmanship: Writing Code"

This struck me as deeply ironic. Writing is an **excellent** metaphor for software development, and the author of a book - especially a large technical one - should be extremely aware of this.

The author seems to only consider the analogy of the metaphor to be of "writing a casual letter", rather than writing in general. This is unfair to the metaphor and not applied to that of construction (which covers all sizes, not just flat-pack assembly). Writing ranges from a succinct social media post to a [collection of textbooks](https://www.oreilly.com/products/books-videos.html) or connected story that ranges over dozens over books by multiple authors ([Wild Cards](https://en.wikipedia.org/wiki/Wild_Cards), [Cosmere](https://www.brandonsanderson.com/what-is-the-cosmere/), [Marvel](https://en.wikipedia.org/wiki/Marvel_Universe), [Riftwar](https://en.wikipedia.org/wiki/The_Riftwar_Cycle), to name a few). This is hardly unique to writing - construction, farming, and other metaphors the chapter explore all range in sizes.

> Writing is usually a one-person activity, whereas a software project will most likely involve many people with many different responsibilities.
>
> Steve McConnell, Code Complete, Chapter 2

This quote was particularly interesting, as one of my colleagues brought it up in our discussion as an example of how McConnell was correct about writing being a poor metaphor, whereas I read it as an example of how wrong he was.

The "many people with many different responsibilities" absolutely applies to (non letter!) writing - you have editors, alpha and beta readers, illustrators, publicists, and many more. A lot of these work well in the software development metaphor - early readers are code reviewers, illustrators are designers, publicists are, well, publicists, and so on. This is the aspect that I was focused on when I read it.

My colleague, however, saw the truth in the "one-person activity". It's true that a lot of writing is done by one person. There are a lot of examples where this is not the case (co-authoring, anthologies, shared universes, ghostwriting, a lot of journalism, etc), but it's probably safe to say that there's less cowriting (particularly of the same block of text, however you define "block") in code than other writing. I think where we differ is that I see this as one area where the metaphor is weak, but the rest is so strong that it outweighs that.

I also do suspect that that there's an awful lot of software that is written by a single person. This isn't just sole-developer products, but also components of large, multi-person, systems where there's a single person that does nearly all the writing and maintenance of that one component (or module or library or micro-service or ...). This isn't *good* software development, but in my experience it is, unfortunately, fairly common. Often there are other people involved, but only lightly, in the same way that an editor or sub-editor might be with other writing.

> In writing, a high premium is placed on originality. In software construction, trying to create truly original work is often less effective than focusing on the reuse of design ideas, code, and test cases from previous projects.
>
> Steve McConnell, Code Complete, Chapter 2

I'm not sure that originality is that much of a premium in letter writing - but then I never did much of that. More broadly, originality has a "premium" in some forms of writing, but not in others - people are generally looking for the same broad style in a new romance novel, they find it easiest to read news articles that are structured in the same way, the latest *[Reacher](https://www.jackreacher.com/us/books/)* novel is not that different from the previous one (or the last *[Will Robie](https://www.davidbaldacci.com/landing-page/david-baldacci-will-robie-series/)*, or the last *[Alex Cross](https://www.jamespatterson.com/landing-page/james-patterson-books-alex-cross/)*, and so on)[1](#79e552e2-0b20-4978-8193-87021559053d).

There's a concept in software development that you get [three "innovation tokens"](https://mcfunley.com/choose-boring-technology). Similarly, when writing a novel or series of novels, you can have a truly original character, or world, or plot, or theme, but you almost always need to have the majority of the work be fairly familiar to the reader (particularly a reader who is familiar with the genre). Just as with software development, you can go wild with innovation and originality, but it's high risk and makes it harder for readers/users.

> When you finish writing a letter, you stuff it into an envelope and mail it. You can't change it anymore, and for all intents and purposes it's complete.
>
> Steve McConnell, Code Complete, Chapter 2

This is true of a letter, but untrue of most modern writing. Pushing the irony more, this is a quote from the **second edition** of *Code Complete*. Writing that ends up in print often is in a final form - but there's also a lot of software out there that just runs without any updates.

To be fair to McConnell, 30 years ago there was a lot less revision of writing - no editing Wikipedia, pushing out ebook updates, rapidly revised news articles, or tweaked blog posts. On the other hand, there was also a lot of "finalised" software back then too, where you'd buy a box with a disk or cartridge and, unless you did buy an updated version, you'd have that same version forever.

> But extending the metaphor of "writing" software to a plan to throw one away is poor advice for software development, where a major system already costs as much as a 10-story office building or an ocean liner.
>
> Steve McConnell, Code Complete, Chapter 2

I'm very much in favour of a reasonable level of well-executed planning and design, but beginning a software project without being willing to throw away any dead ends would strike me as a huge red flag. Defining the role of a software architect is complicated (see also [this great Charity Majors post](https://charity.wtf/2023/03/09/architects-anti-patterns-and-organizational-fuckery/)) but I maintain that the core task of an architect is working with people to minimise the number of decisions that are regretted in the future. That might be a wonderful design where almost nothing is thrown away. It might also be settings things up so that throwing things away is inexpensive and experimentation leads to market success.

I'd argue that with the really huge projects, we have plenty of examples ([Novopay](https://en.wikipedia.org/wiki/Novopay), [INCIS](https://en.wikipedia.org/wiki/INCIS), and others just in Aotearoa New Zealand) that show that big upfront planning with a reluctance to throw anything away leads to terrible cost overruns and missed deadlines.

> Building software implies various stages of planning, preparation, and execution that vary in kind and degree depending on what's being built.
>
> Steve McConnell, Code Complete, Chapter 2

This is exactly what writing is like. Just like when writing a small "throw-away" software script, almost no planning goes into a social media post. When writing a novel, there's a huge amount of planning, preparation, and execution (here's [a series going into it from one author](https://mattgemmell.com/podcast/) - there are many, many, others - books on how to write books are almost as common as podcasts about making podcasts!). I find it difficult to believe that this was not the case for writing *Code Complete* itself.

McConnell extends that argument to compare the cost of making a mistake on a small project with one on a large project (ignoring any learning that may have come from making the mistake) - this equally applies in writing. If I end up rewriting a section of a blog post, that's fairly trivial. If I have to restructure the entire third act of a novel, that's a bigger issue, and if I have already finished two books in a trilogy and need to make changes to them to make the final volume complete, that's very expensive to fix.

> In building a house, you won't try to build things you can buy already built. You'll buy a washer and dryer, dishwasher, refrigerator, and freezer. Unless you're a mechanical wizard, you won't consider building them yourself. You'll also buy prefabricated cabinets, counters, windows, doors, and bathroom fixtures. If you're building a software system, you'll do the same thing. You'll make extensive use of high-level language features rather than writing your own operating-system-level code.
>
> Steve McConnell, Code Complete, Chapter 2

When writing a novel, you don't start from first principles. You'll probably have a [three-act structure](https://en.wikipedia.org/wiki/Three-act_structure), your story probably fits - at least somewhat - into one of [seven basic plots](https://en.wikipedia.org/wiki/The_Seven_Basic_Plots), and you'll build on top of whatever [tropes](https://tvtropes.org/) are appropriate to the world you're writing about. You don't need to explain enemies-to-lovers or the misdirects in a mystery story, and you can call your Hobbits "halflings" and most readers will immediately have the right characteristics to mind. Just as in McConnell's example of luxury housing having some of these fittings custom-made, the highest quality novels often deviate from the norms in a few specific areas (an imaginative magic system, a innovative take on local history, an unusual prediction about the future, and so on).

> Finally, the construction analogy provides insight into extremely large software projects. ... [Builders] build in margins of safety; it's better to pay 10 percent more for stronger material than to have a skyscraper fall over. A great deal of attention is paid to timing. When the Empire State Building was built, each delivery truck had a 15-minute margin in which to make its delivery. If a truck wasn't in place at the right time, the whole project was delayed.
>
> Steve McConnell, Code Complete, Chapter 2

Cost and timing are important in extremely large writing projects too. Delays in editing or proofing or illustration or printing or many other things can delay an entire book launch (the *Potter* books have apparently reached nearly US$8B in sales, the Empire State Building cost under US$1B to build, adjusted for inflation). When a book is very high profile, it's worth spending extra to have additional early readers and editors, just as you build with stronger material (obviously an unsuccessful book is less significant than a collapsing building).

Overall, I do agree with some of the core takeaways of the second chapter - that there's value in metaphor, that they are "a little sloppy", and that you should use the best (mix) of metaphors that work in the context. I just can't agree that construction is a better metaphor for writing code than writing (non-code) is.

This chapter might have hit the sweet spot for me - the combination of reading/writing and software development - but I'm hopeful that the upcoming ones will also be as thought-provoking and enjoyable to discuss with my colleagues. If you don't have a work book club, I highly recommend starting one! ([Non-work book clubs](https://www.goodreads.com/review/list/2229155?shelf=j-tolhopf-book-club) are great too!).
