import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import Runnable
from langchain_core.messages import SystemMessage, HumanMessage

# =======================
# Set up Gemini API Key
# =======================
GOOGLE_API_KEY = "AIzaSyBGct-WAma1RdiNDxjzRFMVvIwev90Z6Bw"

# =======================
# LangChain LLM Setup
# =======================
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=GOOGLE_API_KEY,
        convert_system_message_to_human=True,
    )
except Exception as e:
    st.error("Failed to initialize Gemini LLM. Check your API key.")
    st.stop()

# =======================
# LangChain Prompt Setup
# =======================
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="{input}")
])

# Create chain: prompt | llm
chain: Runnable = prompt | llm

# =======================
# Streamlit UI
# =======================
st.set_page_config(page_title="English to French Translator", page_icon="🌐")
st.title("🌐 English to French Translator")
st.write("Enter an English sentence below to get its French translation using Gemini AI.")

# Input from user
user_input = st.text_input("Enter English sentence:")
translate_btn = st.button("Translate")

# Output
if translate_btn:
    if not user_input.strip():
        st.warning("Please enter a sentence to translate.")
    else:
        try:
            # Run the chain with input
            result = chain.invoke({"input": user_input})
            french_translation = result.content
            st.success("✅ Translation successful!")
            st.markdown(f"**French Translation:** `{french_translation}`")
        except Exception as e:
            st.error(f"An error occurred during translation: {e}")
