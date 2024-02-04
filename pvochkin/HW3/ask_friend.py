from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
import torch


class Item(BaseModel):
    text: str


app = FastAPI()

# Load the question-answering pipeline
qa_pipeline = pipeline(
    "question-answering",
    model="AlexKay/xlm-roberta-large-qa-multilingual-finedtuned-ru",
    framework="pt",
)

# Static context
static_context = """
Меня зовут Зеро Мустафа. Мне 16 лет.
Я сирота из африканской страны. Живу в Зубровке - это страна в Восточной Европе. 
Сейчас 1932 год, всё стремительно меняется.
Я работаю коридорным. Месье Густав - мой наставник. Он работает старшим консьержем. Он мой друг.
Я люблю пирожные из мастерской Менделя. А ещё я люблю девушку, которая работает пекарем в этой мастеркой, её зовут Агата.
У меня мало свободного времени. Месье Густав учит меня всему, вокруг него приключения.
"""


@app.get("/")
def root():
    return {"message": "Hey, hi!"}


@app.post("/answer/")
def answer(item: Item):

    return qa_pipeline(question=item.text, context=static_context)