from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from engine import query_sql_agent

# 1. Initialize FastAPI
app = FastAPI(
    title="Enterprise Text-to-SQL AI API",
    description="REST API to query SQL databases using Natural Language and LangChain Agents.",
    version="1.0.0"
)

# 2. Add CORS Middleware (Essential for connecting to React/Frontend apps)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Define the Request Model (Pydantic)
class QueryRequest(BaseModel):
    question: str

# 4. Root Endpoint
@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "Welcome to the Text-to-SQL AI Agent API",
        "docs": "/docs"  # Link to FastAPI's auto-generated documentation
    }

# 5. The Main Query Endpoint
@app.post("/query")
async def ask_database(request: QueryRequest):
    """
    Takes a natural language question, processes it via the LangChain Agent,
    and returns the answer generated from the SQL database.
    """
    if not request.question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    try:
        # Call the engine logic
        answer = query_sql_agent(request.question)
        
        return {
            "status": "success",
            "question": request.question,
            "answer": answer
        }
    
    except Exception as e:
        # Log the error and return a 500 status code
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# 6. Run the API (For local development)
if __name__ == "__main__":
    import uvicorn
    # Run using: python main.py
    # API will be available at: http://127.0.0.1:8000
    uvicorn.run(app, host="127.0.0.1", port=8000)