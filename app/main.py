from fastapi import FastAPI

from app.gatekeeper import Job, review_job

app = FastAPI(title="HVAC Invoice Gatekeeper", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/review")
def review(job: Job):
    return review_job(job)
