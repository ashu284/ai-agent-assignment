def generator_agent(input_data, feedback=None):
    grade = input_data["grade"]
    topic = input_data["topic"]

    # Default explanation
    explanation = (
        "An angle is made when two lines meet at a point. "
        "There are three main types of angles. "
        "An acute angle is less than 90 degrees. "
        "A right angle is exactly 90 degrees. "
        "An obtuse angle is more than 90 degrees."
    )

    # If reviewer gives feedback, simplify explanation
    if feedback:
        explanation = (
            "An angle is made when two lines meet. "
            "Acute angles are small. "
            "Right angles are exactly 90 degrees. "
            "Obtuse angles are bigger than 90 degrees."
        )

    mcqs = [
        {
            "question": "Which angle is exactly 90 degrees?",
            "options": ["Acute", "Obtuse", "Right", "Straight"],
            "answer": "Right"
        },
        {
            "question": "Which angle is smaller than 90 degrees?",
            "options": ["Right", "Obtuse", "Acute", "Straight"],
            "answer": "Acute"
        }
    ]

    return {
        "explanation": explanation,
        "mcqs": mcqs
    }
