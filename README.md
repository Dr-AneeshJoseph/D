# 🔥 B.L.A.S.T. (Binary Logic Assurance & Sincerity Test)

> **The Hallucination Firewall for High-Stakes RAG.**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## ⚠️ The Problem
In Retrieval-Augmented Generation (RAG), a single "Confidently Wrong" answer can be disastrous (e.g., misdiagnosing a patient or citing a fake law).

## 🛡️ The Solution
**B.L.A.S.T.** implements **Loop 6 (Self-Consistency)**.
Instead of asking the LLM once, it asks **N times** (default: 3).
* If the answers align (High Consensus), the output is solidified.
* If the answers diverge (High Entropy), the output is **incinerated**.

We prefer "No Answer" over a "Wrong Answer."

## 🚀 Quick Start
```python
from blast.gatekeeper import BlastGatekeeper

# Run your query 3 times
responses = [llm.call(prompt) for _ in range(3)]

# Check consistency
result = BlastGatekeeper().verify_responses(responses)

if result['status'] == "SOLIDIFIED":
    print(result['final_output'])
else:
    print("Error: Model is hallucinating.")
