from transformers import pipeline

pipe = pipeline('question-answering','deepset/bert-base-cased-squad2')
print(pipe("Where do you study?","My name is Nurislam. I'm 22 years old and I study MLOps at Ural Federal University"))
