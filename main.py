from fastapi import FastAPI

app = FastAPI()


@app.post("/incoming-sms")
def incoming_sms(message: str):
    return {"message": message}
