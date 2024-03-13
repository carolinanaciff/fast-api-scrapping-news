from fastapi import FastAPI
from routers import router

app = FastAPI()

@app.get('/')
def health_check():
    return 'Application is up!'

app.include_router(router)