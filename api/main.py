from fastapi import FastAPI
from routers import rag, search

app = FastAPI(title="Financial Search API")

app.include_router(search.router)
app.include_router(rag.router)


@app.get("/", name="on", description="online")
def root():
    return {"status": "online"}
