import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_core.messages import SystemMessage, HumanMessage

# =======================
# Set up Gemini API Key
# =======================
GOOGLE_API_KEY = "AIzaSyCTpId2pXWyh90xTGZLtxS5TqWbH9hJE98"  # Replace with your actual Gemini API key

# =======================
# LangChain LLM Setup
# =======================
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=GOOGLE_API_KEY,
        convert_system_message_to_human=True,
    )
except Exception as e:
    st.error(f"❌ Failed to initialize Gemini LLM. Error: {e}")
    st.stop()

# =======================
# LangChain Prompt Setup
# =======================
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful assistant that translates English to French. Provide only the French translation of the input sentence, nothing else."),
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
user_input = st.text_input("Enter English sentence:", placeholder="e.g., The sun is shining today.")
translate_btn = st.button("Translate")

# Output
if translate_btn:
    if not user_input.strip():
        st.warning("⚠️ Please enter a sentence to translate.")
    else:
        try:
            # Run the chain with input
            result = chain.invoke({"input": user_input})
            french_translation = result.content.strip()
            st.success("✅ Translation successful!")
            st.markdown(f"**French Translation:** `{french_translation}`")
        except Exception as e:
            st.error(f"❌ An error occurred during translation:\n\n{str(e)}")
