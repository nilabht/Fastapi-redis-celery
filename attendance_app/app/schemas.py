from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class AttendanceRequest(BaseModel):
    employee_id: str
    action: Literal["check-in", "check-out"]
    timestamp: datetime
