from pydantic import BaseModel
from typing import List, Optional

class Agent(BaseModel):
    name: str
    role: str
    skills: List[str]
    description: Optional[str] = None