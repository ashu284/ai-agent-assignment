import streamlit as st
from generator import generator_agent
from reviewer import reviewer_agent

st.set_page_config(page_title="AI Agent Assignment", layout="centered")

st.title("🤖 AI Agent-Based Educational Content Generator")

st.write("This app demonstrates a Generator Agent and a Reviewer Agent working together.")

grade = st.selectbox("Select Grade", [4])
topic = st.text_input("Enter Topic", "Types of angles")

if st.button("Generate Content"):
    input_data = {
        "grade": grade,
        "topic": topic
    }

    st.subheader("📘 Generator Agent Output")
    generated_content = generator_agent(input_data)
    st.json(generated_content)

    st.subheader("🧐 Reviewer Agent Feedback")
    review_result = reviewer_agent(generated_content)
    st.json(review_result)

    if review_result["status"] == "fail":
        st.subheader("🔁 Refined Output (After Review)")
        refined_content = generator_agent(
            input_data,
            feedback=review_result["feedback"]
        )
        st.json(refined_content)
