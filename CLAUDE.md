# nprimeau.dev

Personal blog for Nicolas Primeau. Hugo + PaperMod, deployed to Vercel at nprimeau.dev.

## Stack

- **Hugo** with PaperMod theme
- **Vercel** for hosting (`vercel.json` configured)
- **Namecheap** for DNS (credentials in `~/.env` symlinked from `../Nimbus/.env`)

## Content

Posts live in `content/posts/`. New posts default to `draft: false`.

## Project management — use Artel

All tasks, memories, and project context live in **Artel**, not in local files or CLAUDE.md.

At the start of every session:
1. Call `session_context()` — loads last handoff and memory changes
2. Call `message_inbox()` — check for messages from other agents
3. Join the `blog` project — `project_join("blog")`

At the end of every session:
4. Call `session_handoff()` — save what you did so the next session can continue

Use `task_list(project="blog")` to find open work. Claim tasks before starting, complete or fail them when done. Write findings to Artel memory — not here.

## Deployment

Vercel deployment is not yet connected (task open in Artel). DNS is pending Vercel setup.

To preview locally:
```
hugo server -D
```
