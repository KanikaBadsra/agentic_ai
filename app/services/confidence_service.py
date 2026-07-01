def calculate_confidence(state):

    confidence = 0.5

    if state.get("sql_result") or state.get("result"):
        confidence += 0.2

    if state.get("rag_result") or state.get("documents"):
        confidence += 0.1

    if state.get("analytics_result"):
        confidence += 0.1

    trace_count = len(
        state.get("execution_trace", [])
    )

    if trace_count > 3:
        confidence += 0.1

    confidence = min(confidence, 0.99)

    return confidence

def determine_risk(confidence):

    if confidence >= 0.8:
        return "LOW"

    elif confidence >= 0.6:
        return "MEDIUM"

    return "HIGH"

def requires_human_review(confidence):

    return confidence < 0.6