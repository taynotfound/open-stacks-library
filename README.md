# The Open Stacks — Library

The data repo behind [**The Open Stacks**](https://github.com/taynotfound/the-open-stacks) — a growing, multi-source anti-censorship library.

Every book is a Markdown file under `books/<category>/`. Binaries (public-domain / at-risk works we intentionally self-host) live under `files/`. The [frontend](https://github.com/taynotfound/the-open-stacks) reads this repo **live**, so dropping a new `.md` in and pushing is all it takes to publish.

## Structure

```
books/<category>/<slug>.md   # metadata + archived body text, images, links, chapters
files/                        # self-hosted binaries (public-domain / at-risk only)
```

Each Markdown file carries front-matter: `title`, `author`, `category`, `source`, `source_name`, `cover`, `page_type`, `mirror_state`, `tags`, `images`, `links`, `files`, plus the archived body.

## Sources

Multi-source by design — every entry credits and links back to where it came from (libcom.org, Project Gutenberg, Marxists.org, and more). We store short metadata/teasers for works mirrored elsewhere, and only self-host full text for public-domain or at-risk works (1984, Animal Farm, ...).

## Download everything

[`open-stacks-library/archive/refs/heads/main.zip`](https://github.com/taynotfound/open-stacks-library/archive/refs/heads/main.zip)

## Stance

We stand for free speech and free access — and against the far right, state control, capitalism, and censorship.

Texts remain © their authors / under each source's terms. Take what you need, give what you can.
