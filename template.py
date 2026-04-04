from langchain_core.prompts import PromptTemplate




template = PromptTemplate(
    template="""
Summarize the research paper titled "{paper_input}" according to these specific guidelines:

1. **Format & Tone**:
   - Explanation Style: {style_input}
   - Explanation Length: {length_input}

2. **Technical Content**:
   - **Mathematical Details**: Include any relevant mathematical equations found in the paper using LaTeX format. 
   - **Code Intuition**: Explain complex math using simple, intuitive Python code snippets where applicable.

3. **Clarity & Analogies**:
   - Use relatable analogies to simplify complex technical ideas.

4. **Strict Accuracy**:
   - If specific information is not found in the paper, respond exactly with: "Insufficient information available." Do not hallucinate or guess.

Ensure the final summary is clear, accurate, and strictly aligned with the requested style and length.
""",
input_variables=["paper_input", "style_input", "length_input"],
validate_template=True
)

template.save("template.json")



