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
Меня зовут Гайсар. Мне 22 года. 
Я учусь в Уфимском университете науки и технологий. 
Работаю в правительстве республики Башкортостан в экономическом отделе.
По вечерам играю в Age of Empires 2.
Записываю ролики на ютуб, смотрю Джинса.
"""


@app.get("/")
def root():
    return {"message": "Hello, Prepod"}


@app.post("/answer/")
def answer(item: Item):

    return qa_pipeline(question=item.text, context=static_context)
