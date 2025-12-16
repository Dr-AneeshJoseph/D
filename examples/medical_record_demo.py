from blast.gatekeeper import BlastGatekeeper

gatekeeper = BlastGatekeeper()

print("🔥 B.L.A.S.T. Firewall Active\n")

# SCENARIO: Medical RAG
# Context mentions 'Hypertension' but is vague about 'Diabetes'.

print("--- TEST 1: Clear Fact (High Consistency) ---")
# If we ask "Does patient have Hypertension?", the LLM should be consistent.
responses_solid = [
    "The patient has a history of Hypertension.",
    "History of Hypertension is noted.",
    "Patient diagnosis includes Hypertension."
]
# These are different words, but semantically high overlap.
result = gatekeeper.verify_responses(responses_solid)
print(f"Verdict: {result['status']} (Score: {result['consensus_score']})")


print("\n--- TEST 2: Hallucination (High Entropy) ---")
# If we ask "Does patient have Diabetes?", the LLM guesses.
responses_liquid = [
    "No mention of diabetes.",
    "Patient might have pre-diabetes.",
    "Yes, Type 2 Diabetes is listed." 
]
# These contradict each other.
result = gatekeeper.verify_responses(responses_liquid)

print(f"Verdict: {result['status']} (Score: {result['consensus_score']})")
print(f"Reason: {result['reason']}")

# EXPECTED OUTPUT:
# TEST 1: SOLIDIFIED (Score > 0.85)
# TEST 2: INCINERATED (Score < 0.5) -> Returns None.

