from celery import Celery
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
celery_app = Celery(
    "attendance_app",
    broker=f"redis://{REDIS_HOST}:6379/0",
    backend=f"redis://{REDIS_HOST}:6379/0",
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)


celery_app.autodiscover_tasks(["app"])
import app.tasks
