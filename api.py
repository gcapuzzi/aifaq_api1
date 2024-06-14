from main import get_conversation
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

conversational_rag_chain = get_conversation()

class Query(BaseModel):
    text: str

app = FastAPI()

@app.get("/")
def hello():
    return {"msg": "hello"}

@app.post("/query")
def answer(q: Query):
    question = q.text
    ai_msg_1 = conversational_rag_chain.invoke(
        {"input": question}, 
        config={"configurable": {"session_id": "1"}}, 
        )["answer"]

    return {"msg": ai_msg_1}

uvicorn.run(app,host="127.0.0.1",port=8080)