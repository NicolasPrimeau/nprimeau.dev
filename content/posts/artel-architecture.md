---
title: "The word Artel"
date: 2026-05-28
draft: false
tags: ["distributed systems", "artel"]
description: "A note on where the name came from, and a thread that runs from 19th-century Russia to Leslie Lamport."
---

I was reading Kropotkin's *La Conquête du Pain* when I decided what to call the project.

The book is about bread — or rather, about who bakes it and who eats it, and whether those two groups have to be different. Kropotkin's argument is that cooperation is not a civilizational achievement layered on top of competitive human nature. It's the other way around. Cooperation is older, more durable, more productive. The historical record is full of it, if you look at the right things.

One of the things he looks at is the artel.

A historical artel was a Russian worker collective — craftsmen, fishermen, or laborers who organized around a shared task, pooled resources, divided earnings, and held each other accountable without a foreman above them. No central authority. The artel decided things by consensus or custom, worked in parallel, and dissolved when the job was done. It was robust precisely because it had no single point of failure.

Artels were everywhere in pre-industrial Russia. Then central planning arrived, and most of them disappeared. Not because they stopped working. Because the system that replaced them required a different shape.

---

Leslie Lamport's 1978 paper "Time, Clocks, and the Ordering of Events in a Distributed System" opens with a deceptively simple observation: a distributed system has no global clock. There is no shared ground truth about when something happened. Each process has only its own local state and whatever messages it has received.

His answer was logical clocks. Each process keeps a counter. When an event occurs, increment it. When you send a message, attach your counter. When you receive a message, take the max of your counter and the sender's, then increment. That's the whole rule. From this tiny local protocol, you get a consistent global ordering of events — without a coordinator.

This thread runs through everything that came after: vector clocks generalize it to track causality across processes. Gossip protocols spread state through pairwise exchanges, so information diffuses across a network without any node having a global view. CRDTs — Conflict-free Replicated Data Types — go further still: design your data structures so any two replicas can always be merged without conflict, regardless of order. Eventual consistency stops demanding agreement at every moment and asks instead for convergence over time.

The through-line in all of it is the same: coherent collective behavior from local rules. No coordinator required.

What strikes me is that Kropotkin was making the same argument, from history, a hundred years earlier. He was describing artels and mutual aid societies and guild structures and pointing at the same underlying principle: you don't need a central authority to get a system that works. You need the right rules for how the parts interact. The rest emerges.

Kropotkin to Lamport is a straight line. One argued for it philosophically, the other proved it mathematically.

---

When I was naming the project, I wanted a word that carried this idea. Not "mesh" or "swarm" or "cluster" — those are topology words. The artel was about the *arrangement* of work: local, accountable, convergent, without hierarchy.

[Artel](https://github.com/NicolasPrimeau/artel) is a coordination layer for AI agents. Each instance runs its own database and archivist. Instances replicate shared memory to each other over JSON Feed subscriptions — no central server, no shared infrastructure required. An agent on one machine can read and write memories that converge, via gossip, to every other instance that subscribes to its feed. The data model is CRDT-friendly by design: last-write-wins on individual entries, tombstones for deletions, origin-stamped records so loops short-circuit.

The architecture reflects the philosophy because the philosophy came first. The warning is in the name.
