# Contributing to the Sledgehammer Suite

You are contributing to a module of the **SLEDGEHAMMER ORACLE v1** architecture. 
This is not standard software; it is "Cognitive Engineering."

## The "Loop" Philosophy
Every tool in this suite corresponds to a specific reasoning loop from the core protocol.
* **Crucible** = Loop 1.5 (Evidence Weighing)
* **Inferno** = Loop 5.5 (Consequence Simulation)
* **Scar** = Loop 10 (Persistent Memory)

## Contribution Rules

### 1. No "Black Box" Logic
We do not trust the LLM to "just figure it out."
* **Bad:** Asking the LLM "Is this claim true?"
* **Good:** Asking the LLM to extract the *Source Type* and *Year*, then using Python to calculate the truth score.
* **Rule:** All critical logic must happen in Python (The Lens), not in the Prompt.

### 2. The "Annihilation" Standard
Our tools are designed to filter noise.
* If you add a feature to **Crucible**, it must make the filter *stricter*, not looser.
* If you add a feature to **Inferno**, it must catch *more* risks, not fewer.

### 3. Red Team Testing
Every Pull Request must include a "Adversarial Test Case."
* Example: "Here is a fake scientific paper that looks real. Does Crucible catch it?"
* Example: "Here is a strategy that makes $1B tomorrow but bankrupts us in 3 years. Does Inferno flag it?"

## Style Guide
* Use `[T1]`, `[T2]` notation for evidence.
* Keep prompts in `prompts/*.md` (Do not hardcode strings in Python).
* Use Type Hinting in all Python code.

Thank you for building with the Hammer.
