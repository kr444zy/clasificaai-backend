from fastapi import FastAPI

app = FastAPI(title="ClasificaAI Backend")

from ClasificaAI-IA-Base.ai_service import router as ai_router
app.include_router(ai_router, prefix="/ai")

@app.get("/")
def root():
    return {"msg": "Backend ClasificaAI funcionando"}

@app.get("/health")
def health():
    return {"ok": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
