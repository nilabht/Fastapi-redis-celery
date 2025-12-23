# Fastapi-redis-celery
attendence app 


-CLONE THE REPOSITORY

**git clone https://github.com/nilabht/Fastapi-redis-celery.git**
**cd Fastapi-redis-celery**

-START THE APPLICATION

Run this command from the project root (where docker-compose.yml exists):

**docker compose up --build**

This will start:
Redis
FastAPI server
Celery worker

-OPEN THE API

Open a browser and go to:

*http://localhost:8000/docs*

This opens the Swagger UI where APIs can be tested.

-TEST ATTENDANCE API

Endpoint:
POST /attendance

Sample Request:

{
"employee_id": "E826",
"action": "check-in",
"timestamp": "2025-12-23T10:00:11.196Z"
}

Expected Response:

{
"message": "Attendance submitted",
"task_id": "uuid"
}

Flow:
FastAPI receives request
Celery processes it asynchronously
Redis stores the attendance data

-VERIFY DATA IN REDIS

Open Redis CLI inside container:

**docker exec -it attendance_redis redis-cli**

Then run:

**HGETALL attendance:E826**
