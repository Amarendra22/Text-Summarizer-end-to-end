from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline
from fastapi.staticfiles import StaticFiles
import os
import uvicorn
import sys

text:str = "What is Text Summarization?"

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/home")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")
    
@app.get("/home", response_class=HTMLResponse, tags=["homepage"])
async def home(request: Request, prediction: str = None):
    return templates.TemplateResponse("index.html", {"request": request, "prediction": prediction})

@app.post("/predict")
async def predict_route(request: Request, text: str = Form(...)):
    try:
        obj = PredictionPipeline()
        prediction = obj.predict(text)
        prediction = prediction.replace('<n>', '\n')
        return templates.TemplateResponse("index.html", {"request": request, "text": text, "prediction": prediction})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "text": text, "prediction": f"Error: {e}"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9082)
