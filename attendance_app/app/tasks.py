from app.celery_app import celery_app
from app.redis_client import redis_client

@celery_app.task(name="attendance.process")
def process_attendance(employee_id: str, action: str, timestamp: str):
    key = f"attendance:{employee_id}"

    redis_client.hset(
        key,
        mapping={
            "last_action": action,
            "timestamp": timestamp,
        }
    )

    return {
        "employee_id": employee_id,
        "status": action,
        "timestamp": timestamp,
    }
