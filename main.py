from fastapi import FastAPI, UploadFile, File
from fastapi import Form
from requests import request

from src.job_parser import parse_job_text
from src.resume_scorer import score_resume
from src.recommender import recommend_skills
from src.models import AnalysisResponse
import shutil
import os

from src.resume_builder import build_resume
from src.skill_extractor import extract_skills


from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="AI Career Assistant",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")



templates = Jinja2Templates(
    directory="templates"
)

@app.get("/web",response_class=HTMLResponse)
async def web_home(
    request: Request
):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.get("/")
def home():
    return {
        "message": "AI Career Assistant API Running"
    }


@app.post("/parse-resume")
async def parse_resume(
    file: UploadFile = File(...)
):
    
   # Upload resume and return structured data.


    # Create uploads folder
    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = f"uploads/{file.filename}"

    # Save uploaded file
    with open(file_path,
        "wb" # write in binary mode
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    # Parse resume
    resume = build_resume(
        file_path
    )

    return resume



@app.post("/analyze-resume")
async def analyze_resume(
    request: Request,
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = f"uploads/{file.filename}"

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    resume = build_resume(
        file_path
    )

    job = parse_job_text(
        job_description
    )

    result = score_resume(
        resume["skills"],
        job["skills"]
    )

    recommendations = recommend_skills(
        result["missing_skills"]
    )

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "candidate": resume["name"],
            "score": result["score"],
            "matched_skills":
                result["matched_skills"],
            "missing_skills":
                result["missing_skills"],
            "recommendations":
                recommendations
        }
    )
    



