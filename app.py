import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

# ✅ Ensure API key is securely set
GOOGLE_API_KEY = "API_KEY"
if not GOOGLE_API_KEY:
    st.error("⚠️ Google GenAI API key is missing! Set GOOGLE_API_KEY as an environment variable.")
    st.stop()

# ✅ Function to fetch AI-generated travel options
def get_travel_options(source, destination):
    system_prompt = SystemMessage(
        content="You are an AI travel assistant. Provide different travel options including cab, train, bus, and flight."
    )
    user_prompt = HumanMessage(
        content=f"I am traveling from {source} to {destination}. Suggest travel options including estimated cost, duration, and travel tips."
    )

    # ✅ Use API key instead of ADC
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GOOGLE_API_KEY)

    try:
        response = llm.invoke([system_prompt, user_prompt])
        return response.content
    except Exception as e:
        return f"❌ Error fetching travel options: {str(e)}"

# ✅ Streamlit UI
st.title("🚀 AI-Powered Travel Planner")
st.write("Enter your travel details, and let AI suggest the best options for you!")

# ✅ User Inputs
source = st.text_input("Enter Source Location", placeholder="E.g., New York")
destination = st.text_input("Enter Destination", placeholder="E.g., Los Angeles")

if st.button("Find Travel Options"):
    if source.strip() and destination.strip():
        st.write(f"🔍 Finding best travel options from **{source}** to **{destination}**...")
        travel_info = get_travel_options(source, destination)
        st.write(travel_info)
    else:
        st.warning("⚠️ Please enter both source and destination locations.")

# Run the app using: streamlit run travel_planner.py
