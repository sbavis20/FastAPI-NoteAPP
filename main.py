from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

conn = MongoClient("")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs=[]
    for doc in docs:
        newDocs.append({
            "id":doc["_id"],
            "note":doc["note"]
        })
    print(docs)
    return templates.TemplateResponse("index.html", {"request": request,"newDocs":newDocs})
