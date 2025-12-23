from fastapi import FastAPI
from app.schemas import AttendanceRequest
from app.tasks import process_attendance

app = FastAPI(title="Employee Attendance App")

@app.post("/attendance")
def mark_attendance(data: AttendanceRequest):
    task = process_attendance.delay(
        data.employee_id,
        data.action,
        data.timestamp.isoformat(),
    )

    return {
        "message": "Attendance submitted",
        "task_id": task.id,
    }
