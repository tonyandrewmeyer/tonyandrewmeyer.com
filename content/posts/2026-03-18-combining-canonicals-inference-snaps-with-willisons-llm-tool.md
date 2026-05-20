---
title: "Combining Canonical's Inference Snaps with Willison's LLM tool"
date: 2026-03-18T20:58:25+12:00
slug: "combining-canonicals-inference-snaps-with-willisons-llm-tool"
---
(Post theme: *[I Want You to Know Me](https://music.apple.com/nz/album/i-want-you-to-know-me/1802438597?i=1802438691&l=en-GB)* by Emerson)

Running LLMs locally has a somewhat deserved reputation for being finicky. Download a model, pick a runtime, figure out GPU offloading, wrestle with dependencies, expose an API, and *then* you can start actually using the thing. Canonical's [inference snaps](https://github.com/canonical/inference-snaps) and Simon Willison's [`llm`](https://llm.datasette.io/) tool each solve half of that problem -- and it turns out they snap together (sorry, not sorry) almost effortlessly.

## The Two Pieces

### Canonical Inference Snaps

[Inference snaps](https://github.com/canonical/inference-snaps) are snap packages that bundle a model with an optimised inference runtime. Install one and you get a running local LLM with zero configuration: `sudo snap install gemma3`

(You may need to [snap or apt install a driver first,](https://documentation.ubuntu.com/inference-snaps/how-to/install-drivers/) to get the best experience.)

That's it. The snap detects your hardware (NVIDIA GPU, Intel GPU, CPU -- even Intel NPUs), selects the appropriate engine, downloads the model, and starts serving. Each snap exposes a CLI (`gemma3 chat` for a quick conversation) and, critically, an **OpenAI-compatible API** on localhost. You can check the details with:

```
$ gemma3 status  
engine: nvidia-gpu-amd64  
services:  
    server: active  
endpoints:  
    openai: http://localhost:8328/v1
```

There are currently snaps for [Gemma 3](https://snapcraft.io/gemma3), [DeepSeek-R1](https://snapcraft.io/deepseek-r1), [Nemotron-3-Nano](https://snapcraft.io/nemotron-3-nano), and [Qwen-VL](https://snapcraft.io/qwen-vl), with more on the way.

### Simon Willison's llm

[`llm`](https://llm.datasette.io/) is a command-line tool and Python library for interacting with language models. It supports OpenAI, Anthropic, and dozens of other providers through a plugin system, but the feature that matters here is its built-in support for **any OpenAI-compatible endpoint** -- no plugin required. You just tell it where to find the API.

## Why They Connect So Easily

The inference snaps serve a standard OpenAI-compatible API. The `llm` tool can talk to any OpenAI-compatible API. That's the entire explanation. No adapters, no plugins, no shims (a wee bit of simple config).

## Setting It Up

Install `llm` however you prefer (I used [uv](https://docs.astral.sh/uv/)):

`uv tool install llm`

Then create the file `~/.config/io.datasette.llm/extra-openai-models.yaml` (you may need to `mkdir -p` the directory first). Add an entry for each snap, using the endpoint from `<snap> status`:

```
- model_id: gemma3  
  model_name: gemma-3-4b-it-q4_0.gguf  
  api_base: "http://localhost:8328/v1"  
  api_key: "not-needed"  
- model_id: deepseek-r1  
  model_name: DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf  
  api_base: "http://localhost:8324/v1"  
  api_key: "not-needed"
```

The `model_name` needs to match what the snap is serving -- you can check with `curl http://localhost:8328/v1/models`. The `api_key` field is required by `llm` but the snaps don't enforce authentication, so any non-empty string works.

Verify that `llm` can see them:

```
$ llm models list | grep gemma  
OpenAI Chat: gemma3
```

## Using It

### From the Command Line

```
$ llm -m gemma3 "Explain DNS to a mass of penguins. Two sentences max."  
Imagine you want to visit a fish restaurant, but you only know the restaurant's name, not its exact location. DNS is like a super-smart librarian that translates that name into a specific address so you can find it!  
  
$ llm -m deepseek-r1 "Write a haiku about compiling code on a Friday afternoon."  
Code hums Friday afternoon.  
The machine hums, logic parses, code flows.  
Code flows with a click.
```

(Gemma is not a natural with our penguin friends, and DeepSeek was not designed for its poetry.)

The `llm` tool also gives you conversation logging, templates, and the ability to pipe content in; `cat error.log | llm -m gemma3 "What went wrong here?"` is a useful thing to be able to do with a model running entirely on your own machine.

### From Python

The `llm` Python package makes it just as straightforward to use from code:

```
import llm  
  
model = llm.get_model("gemma3")  
response = model.prompt( "In exactly one sentence, what is the best thing about snap packages?" )  
print(response.text())  
  
# Example output  
  
Snap packages offer a convenient and isolated way to install applications across different Linux distributions without compatibility issues.
```

A slightly more involved example -- querying multiple local models to then compare their answers:

```
import llm  
  
question = "Summarise plot of the book Beak of the Moon. Three paragraphs max."  
  
for model_id in ["gemma3", "deepseek-r1"]:  
  model = llm.get_model(model_id)  
  response = model.prompt(question)  
  print(f"--- {model_id} ---")  
  print(response.text())  
  print()
```

Everything here runs locally. No API keys being sent anywhere, no tokens being metered, no data leaving your machine. Some of the time, that matters.

I've also found `llm` very convenient in the past when prototyping AI features and wanting to easily switch between providers/models. Not everyone provides an OpenAI compatible API, and working just with `llm` (sometimes slightly patched - for example, the Fireworks plug-in is quite out of date) is very handy. Adding the trivial-to-install and matched-to-your-hardware inference snaps and that gets and extra boost.

## Wrapping Up

You can watch me do this (other than the `snap install`, which is constrained by bandwidth, and I live in the middle of nowhere so that's pretty slow).

[![asciicast](https://asciinema.org/a/YdOesQnXOlCm1qIs.svg)](https://asciinema.org/a/YdOesQnXOlCm1qIs)

The setup here is: install a snap, create a four-line YAML file, and you have a local LLM accessible through a well-designed CLI tool and Python library. The entire configuration surface is one file. There is no Docker, no port forwarding, no environment variable archaeology.

The inference snaps handle the hard part (model serving, hardware detection, runtime optimisation, confinement) and expose a clean API. The `llm` tool handles the other hard part (a good user interface, conversation history, a plugin ecosystem) and speaks that same API. Two tools, one (I guess pseudo) standard, no friction.

*(Disclaimer: I work for Canonical ([you could too](https://canonical.com/careers)), but not anywhere near the inference snaps; I'm just a fan. No conection with* `llm` *other than admiration and use)*
