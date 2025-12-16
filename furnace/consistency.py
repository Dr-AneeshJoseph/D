from difflib import SequenceMatcher

class ConsistencyArbiter:
    """
    Implements Loop 6: Self-Consistency Check.
    """
    
    def calculate_consensus(self, responses: list):
        """
        Compares N responses against each other.
        Returns a 'Confidence Score' (0.0 to 1.0).
        """
        if not responses:
            return 0.0
            
        # Strategy: Compare every response to the first one (The Anchor).
        # In production, you might do N*N comparison or embedding similarity.
        anchor = responses[0]
        total_similarity = 0
        
        for i, resp in enumerate(responses):
            # SequenceMatcher gives a float 0.0-1.0 similarity ratio
            sim = SequenceMatcher(None, anchor, resp).ratio()
            total_similarity += sim
            
        # Average similarity
        consensus_score = total_similarity / len(responses)
        return round(consensus_score, 3)

    def validate_batch(self, responses: list, threshold=0.85):
        """
        The Blast Furnace.
        If Consensus < Threshold, the batch is incinerated.
        """
        score = self.calculate_consensus(responses)
        
        if score < threshold:
            return {
                "status": "INCINERATED",
                "reason": f"High Entropy (Score: {score}). Model is hallucinating.",
                "consensus_score": score,
                "final_output": None
            }
        
        return {
            "status": "SOLIDIFIED",
            "reason": "High Consistency.",
            "consensus_score": score,
            "final_output": responses[0] # Return the anchor response
        }
      
