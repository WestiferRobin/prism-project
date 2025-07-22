from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid

router = APIRouter()

# Official documented model
class ExampleModel(BaseModel):
    prism_id: uuid.UUID
    message: str
    processed: Optional[bool] = False

# Example POST endpoint
@router.post("/process", response_model=ExampleModel)
async def process_example(data: ExampleModel):
    # Simulate queues processing with external services
    data.processed = True
    return data
