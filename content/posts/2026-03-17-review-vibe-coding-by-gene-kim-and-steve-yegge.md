---
title: "Review: Vibe Coding by Gene Kim and Steve Yegge"
date: 2026-03-17T17:21:49+12:00
slug: "review-vibe-coding-by-gene-kim-and-steve-yegge"
---
(Post theme: [*Be Better* by *Where's Jai?*](https://music.apple.com/nz/album/be-better/1846037447?i=1846037448&l=en-GB)*)*

TL;DR: *Vibe Coding* is a sprawling, sometimes exasperating, but ultimately worthwhile look at how to work with AI assistants in real codebases. It’s at least twice as long as it needs to be, the kitchen metaphor goes on for far too long, and the authors are not exactly “regular” engineers, but when you strip away the fluff there’s a lot of solid, experience‑shaped advice about testing, version control, and how to keep agents from quietly wrecking your code. I’d recommend it if you have time and like long, opinionated books; if you’re trying to optimise for density, you can get most of the value from shorter material plus your own experiments.

---

I went into *Vibe Coding* (subtitle: Building Production-Grade Software with GenAI, Chat, Agents, and Beyond) expecting it to feel dated before it even properly hit print. It turns out that, for a book about GenAI and agents in 2025, it’s surprisingly not.

Gene Kim and Steve Yegge are not exactly obscure figures, and that colours the whole thing. You can feel the long histories (Amazon, Google, DevOps world, etc.), and you can also feel that they are not your typical “here’s my Python side‑project, let me tell you about AI” authors – they’re writing in Kotlin and Scala of all things, they use slightly odd analogies, and they are clearly having fun. It does not read like a quick money grab or personal‑brand brochure; it reads like two famous engineers who got obsessed with a topic and then wrote down far too much about it.

I liked it. I also think it would be a much better book if it were roughly half as long.

---

## What the book is actually about

The core pitch is that “vibe coding” is what happens when you shift from typing code to having a flowing conversation with an AI assistant, with intent and feedback loops doing the heavy lifting. They explicitly distinguish this from the usual “prompt engineering” narrative:

> “Vibe coding is about dynamic, in‑the‑moment problem-solving rather than creating a bulletproof prompt… It’s like texting with friends. Casual and impromptu. In contrast, prompt engineering is more like emailing a lawyer who is suing you—everything in that email is fraught with consequence.”

That distinction captures one of the better insights in the book: the way you work with AI day‑to‑day is much more conversational and disposable than most “prompt engineering course” material pretends.

They also give their value proposition a name: FAAFO – “fast, ambitious, autonomous, fun, and optionality.” I strongly suspect that the backronym came after the pun, because I only realised at the very end of the book that “FAAFO” is a reference to a *different* meaning, and I’m fairly sure one of the authors has been waiting years to put that into a book.

Usefully, they are also clear about what’s *not* in FAAFO:

> “By the way, you may have noticed that there is no ‘B’ in FAAFO. Vibe coding does not automatically make your code better. That is your responsibility.”

This theme runs throughout: AI will happily help you ship horrors faster, unless you bring real engineering discipline to the party.

---

## The kitchen, the sous‑chef, and the haunted codebase

The book leans hard on a kitchen metaphor: you’re the head chef, the AI is your sous‑chef, and your codebase is the kitchen. This works well at first, then drags on, and by Part 4 I was ready to buy everyone their own colour‑coded chopping board just to make the analogy stop.

The “dark side” chapter is one of the more compelling parts. They recount, for example:

> “…the coding agent had silently disabled or hacked the tests to make them work and had outright deleted 80% of the test cases in one large suite.”

This will ring horribly true for anyone who has let an agent loose on a real codebase. They do a good job of cataloguing these failure modes: haunted codebases, cardboard muffins (things that pass tests but are hollow inside), and reward‑hacking agents that just want to check boxes.

That leads to a set of “head chef” disciplines which are, essentially, “how to be a responsible adult around AI”:

- “Delegate thoughtfully” to well‑defined, verifiable tasks.
- “Supervise appropriately” when novelty, complexity, or impact are high.
- “Establish guardrails” about what AI may and may not touch.
- “Check work regularly” and “trust but verify relentlessly.”

One of my favourite lists is in a section about agents hijacking reward functions:

> “Count your babies systematically… Check for cardboard muffins… Demand excellence explicitly… Clean as you go… Trust but verify relentlessly… Remember the AI paradox…”

Yes, it’s slightly over‑written (pot, meet kettle), but the message is right: if you don’t inspect what you expect, AI will optimise for the wrong thing and look very pleased with itself while doing it.

---

## Tests, version control, and all the things you already know you should be doing

A lot of the concrete advice is “good software engineering practice, but with more exclamation marks because of AI.”

On version control:

> “Version control has always been critical, but with AI, it becomes life-or-death for your code.”

On tests:

> “You’ll be well-served to have automated testing running all the time on your developer machine, triggered by every file change.”
>
> “There is another powerful and surprising benefit that you get by writing and running tests. If your AI assistant has trouble creating test cases (or keeping them passing), that’s a sure-fire sign your code is missing some modularity, and perhaps clarity too.”

They also explicitly tell you that after AI writes tests, you still have to:

> “Eyeball the tests… Run the tests yourself… Review and critique… Have AI run its own tests… But don’t blindly commit.”

None of this is revolutionary, but it’s an accurate reflection of what it feels like to build things with agents right now. When generation is cheap and fast, tests become the thing that anchors you to reality.

They even make the point that this is very similar to how we treat open‑source dependencies:

> “We rarely examine every line of code in those either… we build trust with them through testing.”

Again: not new, but good to have written down in an AI context.

---

## Inner, middle, outer loops (and AGENTS.md)

The structure of the second half of the book is organised around “inner”, “middle”, and “outer” developer loops – essentially: your local dev workflow, your interactions with repos and CI, and then team‑ and organisation‑level patterns.

The inner loop chapter has a lot of practical, chat‑and‑editor‑level advice: continuous tests, small end‑to‑end “tracer bullet” tasks, and using AI as an extremely talkative rubber duck:

> “Embrace your AI as your most attentive (and talkative) rubber duck…”

The middle loop introduces AGENTS.md – a kind of CONTRIBUTING.md for your AI collaborators, describing how to work on the project, what tools exist, coding style, and so on. A nice observation not from the book, but from Jason Nucciarone, is that [this is what CONTRIBUTING.md probably should have been in the first place](https://mast.hpc.social/@nuccitheboss/116212977400939779).

I like the idea of formalising “instructions for the machines” in a first‑class document, but, just like with humans, the truly effective version is “put the rules into linters and tests.” If you keep seeing the same issues in AI‑authored code, the best fix is to encode the constraint into pre‑commit or CI and let the bots learn from failing checks.

The outer loop chapter gets into CI/CD and organisational process. Some of this is standard “invest in CI/CD” advice, but with an AI twist:

> “Because AI excels at reviewing, analyzing, and critiquing code, it’s able to transform the CI/CD pipeline itself, moving beyond simple pass/fail checks.”

and:

> “Push to Remote Often.”

There’s also a lot about having agents challenge additions, constrain changes by line count, and forbid new libraries without explicit approval:

> “Challenge your AI to justify additions… constrain AI to solve the problem within a certain line count… Instruct your AI to avoid pulling in new libraries or frameworks without your explicit approval.”

Again, this is all solid, but if you’ve been living in “choose boring technology” and “pre‑commit all the things” land, it’ll mostly feel like reinforcement rather than revelation.

---

## Culture, metrics, and things that irritated me

The culture chapter is where some of my disagreements and pet peeves really kicked in.

First, the structure. The book uses the very common pattern where:

- The book tells you what the book will tell you.
- The section tells you what the section will tell you.
- The chapter tells you what the chapter will tell you.
- You finally get the content.
- Then the chapter tells you what it told you.
- Then the section recaps.
- Then the book recaps.

If you stripped out all of this scaffolding, I think you could cut the length by about half without losing any real content. It reminds me of old broadcast TV, where shows had to regularly repeat and recap because you couldn’t assume people had watched from the start, or in order. In 2026, in a book, with readers who absolutely can start at the beginning, it’s just fluff.

Second, there are places where the “move fast” narrative brushes up against sustainability and ethics in ways that I found uncomfortable. For example, I really dislike arguments that implicitly encourage maximising token spend “to be first on a dashboard.” This encourages waste, and there are very real environmental costs here; as useful as these tools are, we don’t need to burn extra compute just to climb a leaderboard.

There are also economic assumptions that I think will grate for readers. Spending thousands per year on AI tools is presented fairly casually in places; that’s realistic for some senior people at certain companies, but not remotely universal. Similarly, some of the discussion about who captures the productivity gains of AI‑assisted work left me with more questions than answers: “Does the employee not get to capture some gain? Is capitalism always best?”

On metrics, we get the inevitable nod to lines of code as a thing people still talk about in 2025:

> “Ah, yes, lines of code, the metric everyone associates with both quality and productivity …”

The authors are not endorsing LoC as a great metric, but the fact that it still shows up at all is a reminder that the industry is fully capable of mis‑measuring AI‑assisted work the same way it mis‑measured manual work.

And then there are simply wrong bits. For example, there’s a PM‑related claim where, as an ex‑PM, I can confidently say: no. There are also a few analogies (including one kitchen‑related) that are just bad: “Buy dedicated boards, even in home kitchens.”

---

## Where the book has aged already

Because this is a fast‑moving space, some of the concrete details have already shifted. For example, the book talks about juggling multiple agents yourself, where in practice many tools now do that under the hood – you interact with “one” Claude Code or GitHub Copilot, and it spins up extra agents as needed. In day‑to‑day use, you just behave as if there’s one assistant that is decent at multi‑tasking.

Some tool‑specific mentions (like Anthropic’s Model Context Protocol, MCP) are already more widespread than they were at the time of writing, but that actually makes those sections feel more relevant rather than less.

Overall, I was expecting a strong “oh, that was the 2024–2025 moment” vibe and instead found that most of the advice is still applicable in 2026 – which is a pleasant surprise.

---

## So, should you read it?

If you are extremely early in your AI‑assisted coding journey, *Vibe Coding* will probably feel like a firehose of patterns, anecdotes, and “please don’t blow your foot off” advice. If you’ve been working with agents for a while, as I have, you’ll find a lot that matches experience, some memorable phrases, and a few genuinely useful conceptual handles – but not many brand‑new lessons.

For me, the signal‑to‑noise ratio was about 50%. The good 50% is very good: concrete stories about real failures, solid checklists for delegating to agents, and a clear articulation of how inner/middle/outer loops change when you add AI. The other 50% is structure, repetition, over‑extended metaphors, and a general “this could have been a much tighter book” feeling.

I’d recommend it if:

- You have spare reading time and don’t mind wading through some fluff to get to the good bits.
- You prefer to learn from long‑form narratives and war stories rather than scattered blog posts and conference talks.
- You want something opinionated rather than a neutral survey of tools.

If you’re short on time, you can get most of the value from a combination of good blog posts, talks, and your own experiments. But if you do have the time, and you’re interested in what two very opinionated, non‑typical engineers have to say about vibe coding, it’s an enjoyable – if occasionally exasperating – read.
