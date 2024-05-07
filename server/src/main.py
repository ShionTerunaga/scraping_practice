from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware 
from controller.main_news import screping_yahoo_main

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

@app.get("/")
def index():
    return screping_yahoo_main()

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000)