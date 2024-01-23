from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000)
