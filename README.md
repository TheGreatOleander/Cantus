# CANTUS

**Executable Music Language**  
*"Make a joyful noise — and let it compute."*

CANTUS is an experimental programming language where **audio is the source code**.
A song is a program. Playback is execution.

This repository is the **reference implementation seed**.

---

## Mission

Build a deterministic audio‑interpreted virtual machine where:
- Pitch = opcode
- Time = instruction pointer
- Rhythm = control flow
- Timbre = type system
- Silence = commit

CANTUS treats human‑performable sound as executable structure.

---

## Getting Started

Run the prototype VM:

```
python -m cantus.cli
```

---

## Repo Structure

```
cantus/
  vm.py
  tokenizer.py
  cli.py
docs/
  SPEC.md
examples/
tests/
```

---

## Status

Prototype — Phase I Foundation

Created: 2026-02-11T21:15:31.218458 UTC
