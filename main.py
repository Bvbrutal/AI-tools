import uvicorn
from fastapi import FastAPI, Request, UploadFile
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from fastapi import File
import whisper

from pdf_summary import pdf_summary


model = whisper.load_model("base")

app = FastAPI()
templates = Jinja2Templates(directory="./templates")
app.mount("/static", StaticFiles(directory="./static"), name="static")


@app.get("/whisper")
def home(request: Request):
    return templates.TemplateResponse(
        "whisper.html",
        {
            "request": request
        }
    )

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request
        }
    )

@app.get("/pdf_summary")
def home(request: Request):
    return templates.TemplateResponse(
        "pdf_summary.html",
        {
            "request": request
        }
    )

@app.post("/test")
def homes():
    return {"statu":200}


@app.post("/file_whisper")
async def get_file(file:UploadFile = File(...)):
    media=file.file.read()
    name=file.filename
    filepath='./static/data/whisper/'+name
    with open(filepath, 'wb') as f:
        f.write(media)
    print(name)
    return {"statu":200,
            "name":filepath}

@app.post("/file_pdf_summary")
async def get_file(file:UploadFile = File(...)):
    media=file.file.read()
    name=file.filename
    filepath='./static/data/pdf_summary/'+name
    with open(filepath, 'wb') as f:
        f.write(media)
    print(name)
    return {"statu":200,
            "name":filepath}


@app.post("/show_whisper_result")
async def show_result(name: str = File(...)):
    text = model.transcribe(name)
    return {'statu':200,
            "message": text['text']}

@app.post("/show_pdf_summary")
async def show_result(name: str = File(...)):
    text = pdf_summary(name)
    return {'statu':200,
            "message": text}

if __name__ == '__main__':

    uvicorn.run(app="main:app", host="127.0.0.1", port=8080, reload=True)