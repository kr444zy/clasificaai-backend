from fastapi import FastAPI

app = FastAPI(title="ClasificaAI Backend")

@app.get("/")
def root():
    return {"msg": "Backend ClasificaAI funcionando"}

@app.get("/health")
def health():
    return {"ok": True}
