from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

class ReviewRequest(BaseModel):
    review_text: str

@app.post("/predict-sentiment/")
def get_sentiment(request: ReviewRequest):
    result = classifier(request.review_text)
    return {"label": result[0]['label'], "score": float(result[0]['score'])}
