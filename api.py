from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def get_led():
    return {"led": random.choice(["true", "false"])}
