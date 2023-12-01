import torch
import streamlit as st
from transformers import pipeline

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


# Streamlit app
def main():
    st.title("Спроси у Гайсара")

    # User input
    question = st.text_input("Введите вопрос:")

    if st.button("Получить ответ"):
        # Process the question with the static context
        answer = qa_pipeline(question=question, context=static_context)

        # Display the answer
        st.subheader("Гайсар:")
        st.write(answer["answer"])


if __name__ == "__main__":
    main()

