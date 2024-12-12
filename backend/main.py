# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.agent import router as agent_router

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 추가 - 여기서 prefix 끝에 슬래시를 제거
app.include_router(agent_router, prefix="/api")

@app.get("/")
async def read_root():
    return {"message": "Welcome to Lego Agents API"}