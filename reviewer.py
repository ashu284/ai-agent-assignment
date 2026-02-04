def reviewer_agent(content):
    feedback = []

    # Check explanation length (simple rule)
    if len(content["explanation"]) > 300:
        feedback.append("Explanation is too complex for Grade 4")

    # Check if MCQs exist
    if len(content["mcqs"]) == 0:
        feedback.append("No MCQs provided")

    if feedback:
        return {
            "status": "fail",
            "feedback": feedback
        }

    return {
        "status": "pass",
        "feedback": []
    }
