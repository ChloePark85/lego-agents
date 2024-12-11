from fastapi import APIRouter, HTTPException
from ..models.agent import Agent
from typing import List

router = APIRouter()

agents: List[Agent] = []  # 임시 저장소

@router.post("/agents")
async def create_agent(agent: Agent):
    agents.append(agent)
    return agent

@router.get("/agents")
async def get_agents():
    return agents