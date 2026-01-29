import streamlit as st
from engine import query_sql_agent
from database import get_db_connection

# Page Config
st.set_page_config(page_title="InsightFlow AI", page_icon="📈", layout="wide")

# Custom CSS for a cleaner look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007BFF; color: white; }
    .stTextInput>div>div>input { border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.title("📈 InsightFlow AI")
st.subheader("Your Intelligent Business Data Assistant")
st.write("Empowering non-technical teams to query databases using simple English. Get instant insights without writing a single line of SQL.")
st.markdown("---")

# Layout
col1, col2 = st.columns([1.2, 0.8])

with col1:
    st.info("💡 **How to use:** Simply type a question about your sales, customers, or products below and press Enter.")
    user_input = st.text_input("Example: 'Which 5 countries generated the most profit last year?'", key="query_input")
    
    if st.button("Get Instant Insight"):
        if user_input:
            with st.spinner("🤖 AI Analyst is calculating results..."):
                result = query_sql_agent(user_input)
                st.success("Analysis Ready!")
                st.markdown("### 📊 AI Summary")
                st.write(result)
        else:
            st.warning("Please enter a question to get started.")

with col2:
    with st.container():
        st.subheader("🛠 System Capabilities")
        st.markdown("""
        - ✅ **Multi-Table Joins:** Automatically connects Sales, Customers, and Tracks.
        - ✅ **Self-Correction:** AI fixes its own logic errors in real-time.
        - ✅ **Plain English:** Translates raw data into human-readable summaries.
        """)
        
        with st.expander("📂 View Connected Database Structure"):
            try:
                db = get_db_connection()
                st.code(db.get_table_info())
            except:
                st.error("Connection busy. Try again in a second.")

    st.subheader("🚀 Popular Queries")
    st.button("Total revenue by country", on_click=lambda: st.write("Ask this in the box!"))
    st.button("Top selling music genres", on_click=lambda: st.write("Ask this in the box!"))