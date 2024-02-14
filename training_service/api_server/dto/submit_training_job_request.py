from typing import Optional
from pydantic import BaseModel

class SubmitTrainingJob(BaseModel):
    user_code_encoded: str
