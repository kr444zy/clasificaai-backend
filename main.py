from fastapi import FastAPI

app = FastAPI(title="ClasificaAI Backend")

@app.get("/")
def root():
    return {"msg": "Backend ClasificaAI funcionando"}

@app.get("/health")
def health():
    return {"ok": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
