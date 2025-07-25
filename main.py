import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyBfQQcZUGPiejgwe01JHEWz7GDBEKGQ1X0")

# ✅ Use the correct model
model = genai.GenerativeModel("models/gemini-2.5-pro")

# Streamlit UI
st.set_page_config(page_title="Gemini 2.5 Learning Assistant", layout="centered")
st.title("📘 AI-Based Learning Assistant")

# Educational content input
context = st.text_area("📚 Enter Educational Content (Paragraph, Concept, etc.):", height=150)

# Generate a question
if context and st.button("✨ Generate Question"):
    try:
        prompt = f"Generate an exam-style question from this educational content:\n\n{context}"
        response = model.generate_content(prompt)
        st.success("💡 Generated Question:")
        st.markdown(f"**{response.text.strip()}**")
    except Exception as e:
        st.error(f"❌ Error generating question:\n{e}")

# Inputs for answer evaluation
expected = st.text_input("✏️ Reference Answer")
student = st.text_input("🧑‍🎓 Student's Answer")

if expected and student:
    try:
        eval_prompt = (
            f"Compare the student's answer with the reference answer and evaluate it.\n\n"
            f"Reference Answer:\n{expected}\n\n"
            f"Student Answer:\n{student}\n\n"
            f"Format:\nScore: X/10\nFeedback: <brief feedback>"
        )
        eval_response = model.generate_content(eval_prompt)
        st.info("📊 Evaluation Result:")
        st.markdown(eval_response.text.strip())
    except Exception as e:
        st.error(f"❌ Error evaluating answer:\n{e}")
