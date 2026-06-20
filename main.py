from fastapi import FastAPI, UploadFile, File
from fastapi import Form

from src.job_parser import parse_job_text
from src.recommender import recommend_skills
import shutil
import os

from src.resume_builder import build_resume


from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from fastapi.staticfiles import StaticFiles
from src.ai_scorer import calculate_ai_score

from src.explainable_job_recommender import recommend_jobs_explainable

from src.career_predictor import predict_top_careers


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

    ai_result = calculate_ai_score(
        resume["skills"],
        job["skills"],
        str(resume),
        job_description
    )

    recommendations = recommend_skills(
        ai_result["missing_skills"]
    )
    job_recommendations = (
        recommend_jobs_explainable(
            resume["skills"]
        )
    )
    top_careers = predict_top_careers(
        resume["skills"]
    )

    predicted_career = top_careers[0]

    other_careers = top_careers[1:]

    score = ai_result["final_score"]

    if score >= 80:
        score_class = "high-score"

    elif score >= 50:
        score_class = "medium-score"

    else:
        score_class = "low-score"

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "candidate": resume["name"],
            "score": ai_result["final_score"],
            "skill_score": ai_result["skill_score"],
            "semantic_score": ai_result["semantic_score"],
            "score_class": score_class,
            "matched_skills": ai_result["matched_skills"],
            "missing_skills": ai_result["missing_skills"],
            "job_recommendations":job_recommendations,
            "predicted_career": predicted_career,
            "other_careers": other_careers,
            "recommendations": recommendations
        }
    )
    



