Creating API of our previous model 

##What does this project? 

So we've created API to perfome our model's abilities

##How can I create our own API using this model? 

You only need to import necessary packages from requirements.txt and run a file


```
pip install -r requirements.txt

uvicorn ask_friend:app
```
##How can I interact with model using API?

There are two ways to interact with API:

- Using Postman. You can ask a question sending POST data via raw JSON with Postman. For example:

```
{
    "text":"Где ты учишься?"
}
``` 
Model will answer you:

```
{"score":0.6466110348701477,"start":42,"end":86,"answer":" в Уфимском университете науки и технологий."}
```
- Usind cURL. For example, you can ask it:

```
curl -X 'POST' \
  'http://localhost:8000/answer/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Как дела?"
}

```

It will answer:

```
{
  "score": 0.8254371881484985,
  "start": 24,
  "end": 33,
  "answer": " 22 года."
}
```
