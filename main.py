import streamlit as st
from dotenv import load_dotenv

from src.graph_function import build_reflexion_agent


def main():
    load_dotenv()

    builder = build_reflexion_agent()
    graph = builder.compile()

    # Streamlit app title
    st.title("Reflexion Agent")

    # User input text field
    user_input = st.text_input(
        "Enter your prompt:",
        value="Write about AI-Powered SOC / autonomous SOC problem domain, list startups that do that and raised capital.",
    )

    # Submit button
    if st.button("Submit"):
        with st.spinner("Processing..."):
            try:
                # Invoke the graph with user input
                res = graph.invoke(user_input)
                # Extract and display the answer
                answer = res[-1].tool_calls[0]["args"]["answer"]
                st.write(answer)
            except Exception as e:
                st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
