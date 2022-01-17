from fastapi import FastAPI

app = FastAPI()
import redis
from rq import Queue

r = redis.Redis(host='redis', port=6379)
job_queue = Queue(connection=r)