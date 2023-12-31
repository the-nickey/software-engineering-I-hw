from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()

pipe = pipeline("text-generation", model="Nehc/gpt2_lovecraft_ru")

@app.get("/")
def root():
    return {"message": "Привет, эта модель дописывает текст в стиле Лавкрафта. Она работает с API."}

@app.post("/answer/")
def answer(item: Item):
    return pipe(item.text)[0]