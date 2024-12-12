# backend/app/models/agent.py
from pydantic import BaseModel
from typing import List, Optional

class Agent(BaseModel):
    name: str
    role: str
    skills: List[str]
    description: Optional[str] = None
    
    def execute_task(self, task: str) -> str:
        return f"Agent {self.name} ({self.role}) is working on: {task}"

# backend/app/routes/agent.py
from fastapi import APIRouter, HTTPException
from typing import List
from ..models.agent import Agent

router = APIRouter()

# 임시 저장소 (실제로는 데이터베이스를 사용해야 합니다)
agents: List[Agent] = []

@router.post("/agents/", response_model=Agent)
async def create_agent(agent: Agent):
    agents.append(agent)
    return agent

@router.get("/agents/", response_model=List[Agent])
async def get_agents():
    return agents

@router.get("/agents/{agent_name}", response_model=Agent)
async def get_agent(agent_name: str):
    for agent in agents:
        if agent.name == agent_name:
            return agent
    raise HTTPException(status_code=404, detail="Agent not found")