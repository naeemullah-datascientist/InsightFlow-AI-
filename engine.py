import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.agent_toolkits import create_sql_agent
from database import get_db_connection  # <--- THIS WAS MISSING

load_dotenv()

def query_sql_agent(user_question):
    # 1. Connect to Database
    db = get_db_connection()
    
    # 2. Setup LLM
    llm = ChatGroq(
        model="llama-3.3-70b-versatile", 
        temperature=0, 
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    # 3. Industry-Standard Instructions
    custom_prefix = """
    You are an expert SQL analyst for a Music Store.
    - 'revenue' or 'sales' = 'Total' column in 'Invoice' table.
    - 'billing country' or 'country' = 'BillingCountry' column in 'Invoice' table.
    - 'customer' = 'Customer' table.
    - 'genre' = 'Genre' table.
    - 'track' = 'Track' table.
    - When asked for 'most' or 'top', always use COUNT() or SUM() with GROUP BY and ORDER BY DESC.
    - Always limit results to top 10 unless asked for more.
    - Provide the final answer in a clear, formatted summary.
    """

    # 4. Create Agent
    agent_executor = create_sql_agent(
        llm=llm,
        db=db,
        agent_type="tool-calling",
        verbose=True,
        prefix=custom_prefix
    )

    # 5. Execute
    try:
        response = agent_executor.invoke({"input": user_question})
        return response["output"]
    except Exception as e:
        return f"Error: {str(e)}"